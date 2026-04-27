import os
import re
import asyncio
import uuid
import edge_tts
import pygame


class TTSEngine:
    def __init__(self):
        # Choose an advanced sounding voice.
        # Christopher is a good, clear English male voice, analogous to Jarvis
        self.voice = "en-GB-RyanNeural"

        # Initialize pygame mixer for audio playback
        pygame.mixer.init()

    async def _generate_audio(self, text: str, output_file: str):
        """Generates the audio file using edge-tts asynchronously."""   
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(output_file)

    def speak(self, text: str):
        """
        Public synchronous method to speak text.
        It splits the text into sentences to stream the playback and reduce initial latency.
        """
        # Improved sentence splitting
        sentences = re.split(r'(?<=[.!?]) +|\n+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return

        for sentence in sentences:
            # Create a unique temp file for each sentence to avoid locked file errors
            temp_audio_file = f"database/speak_data/temp_{uuid.uuid4().hex[:6]}.mp3"
            
            try:
                # Generate the audio file for this chunk
                asyncio.run(self._generate_audio(sentence, temp_audio_file))

                # Play the audio file
                pygame.mixer.music.load(temp_audio_file)
                pygame.mixer.music.play()

                # Wait for the audio to finish playing
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

                # Unload the music so we can delete the file immediately
                pygame.mixer.music.unload()

            except Exception as e:
                print(
                    f"\n[AETHER TTS ERROR]: Text-to-speech failed for chunk. Error: {e}"
                )
            finally:
                # Clean up the temp file
                if os.path.exists(temp_audio_file):
                    try:
                        os.remove(temp_audio_file)
                    except PermissionError:
                        pass  # File might be locked, clean up next time


if __name__ == "__main__":
    tts = TTSEngine()
    tts.speak("Hello, how are you doing today? I am functioning perfectly. Let's get to work.")