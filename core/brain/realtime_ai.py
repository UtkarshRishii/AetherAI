import requests
import json


_FLOXAI_URL = "https://searchfloxai.vercel.app/api/search"


class RealtimeAI:
    """
    Robust real-time web search with automatic failover.
    
    Primary  : SearchFloxAI API (AI-summarized results)
    Fallback : DuckDuckGo via ddgs (raw snippets, always available)
    """

    def __init__(self):
        self.flox_url = _FLOXAI_URL

    # ─── Primary: FloxAI ───────────────────────────────────────────────────────

    def _search_floxai(self, query: str) -> str | None:
        """
        Calls the FloxAI API. Returns the answer string or None on any failure.
        """
        try:
            response = requests.post(
                self.flox_url,
                json={"query": query},
                timeout=8,              # Tight timeout — we'll fallback fast
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()
            data = response.json()
            answer = data.get("text", "").strip()
            return answer if answer else None

        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return None   # Silently trigger fallback
        except requests.exceptions.HTTPError as e:
            status = e.response.status_code
            if status == 429:
                print("  [RealtimeAI] FloxAI rate-limited. Switching to fallback...")
            elif status >= 500:
                print("  [RealtimeAI] FloxAI server error. Switching to fallback...")
            return None
        except (json.JSONDecodeError, Exception):
            return None

    # ─── Fallback: DuckDuckGo ──────────────────────────────────────────────────

    def _search_ddgs(self, query: str) -> str | None:
        """
        Fallback search using DuckDuckGo (ddgs). Always returns results.
        """
        try:
            from ddgs import DDGS
            results = DDGS().text(query, max_results=5)
            if not results:
                return None

            formatted = []
            for r in results:
                title = r.get("title", "").strip()
                body = r.get("body", "").strip()
                if title and body:
                    formatted.append(f"• {title}: {body}")

            return "\n".join(formatted) if formatted else None

        except Exception as e:
            print(f"  [RealtimeAI] DuckDuckGo fallback also failed: {e}")
            return None

    # ─── Public API ────────────────────────────────────────────────────────────

    def search(self, query: str) -> str:
        """
        Main search method with automatic failover.
        1. Try FloxAI (fast, AI-summarized)
        2. Fallback to DuckDuckGo (always-on)
        3. Return informative error if both fail
        """
        if not query or not query.strip():
            return "Error: Empty search query."

        query = query.strip()

        # Stage 1: FloxAI
        result = self._search_floxai(query)
        if result:
            return result

        # Stage 2: DuckDuckGo fallback
        print("  [RealtimeAI] FloxAI unavailable. Using DuckDuckGo fallback...")
        result = self._search_ddgs(query)
        if result:
            return result

        # Both failed
        return (
            "I was unable to retrieve live information at this moment due to connectivity issues. "
            "I'll answer based on my existing knowledge instead."
        )


# ─── Test ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    ai = RealtimeAI()
    print(ai.search("Latest AI news 2026"))
