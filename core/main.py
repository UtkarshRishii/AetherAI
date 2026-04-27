import sys
import uuid
sys.stdout.reconfigure(encoding='utf-8')
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich.text import Text
from rich.align import Align
from rich.rule import Rule
from rich import box
from core.brain.brain_service import BrainService
from core.memory.memory_manager import MemoryManager
from core.services.tts import TTSEngine

console = Console()

AETHER_BANNER = r"""
     _    _____ _____ _   _ _____ ____  
    / \  | ____|_   _| | | | ____|  _ \ 
   / _ \ |  _|   | | | |_| |  _| | |_) |
  / ___ \| |___  | | |  _  | |___| _ < 
 /_/   \_\_____| |_| |_| |_|_____|_| \_\
"""

class Aether:
    def __init__(self):
        # Print the boot sequence
        console.print()
        console.print(Align.center(Text(AETHER_BANNER, style="bold cyan")))
        console.print(Align.center(Text("Advanced Entity for Thinking, Heuristics, and Empirical Reasoning", style="dim cyan")))
        console.print(Align.center(Text("Created by Utkarsh Rishi", style="dim white")))
        console.print()
        console.print(Rule(style="cyan"))
        console.print()

        with console.status("[bold cyan]Initializing AETHER core systems...[/bold cyan]", spinner="dots"):
            self.brain = BrainService()
            self.session_id = f"session_{uuid.uuid4().hex[:8]}"
            self.memory = MemoryManager(session_id=self.session_id)
            self.tts = TTSEngine()

        console.print(f"  [bold green]✓[/bold green] Brain Service      [dim]Online[/dim]")
        console.print(f"  [bold green]✓[/bold green] Memory Manager     [dim]Session: {self.session_id}[/dim]")
        console.print(f"  [bold green]✓[/bold green] TTS Engine         [dim]Online[/dim]")
        console.print(f"  [bold green]✓[/bold green] Vector Database    [dim]Long-term memory active[/dim]")
        console.print()
        console.print(Rule("[dim cyan]SYSTEM READY[/dim cyan]", style="cyan"))
        console.print()

    def run(self):
        help_text = (
            "[dim]Commands:[/dim]  "
            "[bold yellow]exit[/bold yellow] / [bold yellow]quit[/bold yellow] — Shutdown  │  "
            "[bold yellow]clear[/bold yellow] — Wipe session memory"
        )
        console.print(Align.center(help_text))
        console.print()

        while True:
            try:
                user_input = Prompt.ask("[bold magenta]⟩ You[/bold magenta]").strip()

                if not user_input:
                    continue

                if user_input.lower() in ["exit", "quit"]:
                    shutdown_msg = "Shutting down all systems. Goodbye."
                    console.print()
                    console.print(Rule("[dim red]SHUTDOWN[/dim red]", style="red"))
                    console.print(f"\n[bold cyan]AETHER:[/bold cyan] {shutdown_msg}\n")
                    self.tts.speak(shutdown_msg)
                    break

                if user_input.lower() == "clear":
                    self.memory.clear_memory()
                    console.print("[bold yellow]  ⚡ Session memory cleared.[/bold yellow]")
                    continue

                # 1. Add user input to memory
                self.memory.add_message("user", user_input)

                # 2. Retrieve context with long-term memory retrieval
                context = self.memory.get_context(current_input=user_input)

                # 3. Process input via Brain (LLM)
                console.print()
                with console.status("[cyan]  AETHER is processing...[/cyan]", spinner="bouncingBall"):
                    response = self.brain.process_input(user_input, chat_history=context)

                # 4. Add AI response to memory
                self.memory.add_message("assistant", response)

                # 5. Output response textually
                console.print()
                console.print(Panel(
                    Markdown(response),
                    title="[bold cyan]AETHER[/bold cyan]",
                    border_style="cyan",
                    box=box.ROUNDED,
                    padding=(1, 2)
                ))
                console.print()

                # 6. Output response audibly
                clean_for_speech = self._sanitize_for_speech(response)
                self.tts.speak(clean_for_speech)

            except KeyboardInterrupt:
                console.print("\n[bold red]  [AETHER] Force quitting...[/bold red]\n")
                break
            except Exception as e:
                console.print(f"\n[bold red]  [AETHER CRITICAL ERROR]: {e}[/bold red]\n")

    def _sanitize_for_speech(self, text: str) -> str:
        """Removes markdown, code blocks, and symbols that shouldn't be read aloud."""
        lines = text.split("\n")
        clean_lines = []
        in_code_block = False

        for line in lines:
            if line.startswith("```"):
                in_code_block = not in_code_block
                if not in_code_block:
                    clean_lines.append("I have provided the code block.")
                continue
            if not in_code_block:
                line = line.replace("**", "").replace("*", "")
                line = line.replace("- ", "").replace("#", "")
                line = line.replace("`", "")
                if line.strip():
                    clean_lines.append(line)

        return " ".join(clean_lines)


def main():
    aether = Aether()
    aether.run()


if __name__ == "__main__":
    main()
