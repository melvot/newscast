"""Convert text news summary into speech audio file."""

import sys
import os
import io

import elevenlabs
from IPython.display import Audio


def main():
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("Error: ELEVENLABS_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    elevenlabs_client = elevenlabs.ElevenLabs(
        api_key=api_key, base_url="https://api.elevenlabs.io"
    )

    audio = elevenlabs_client.text_to_speech.convert(
        voice_id="hpp4J3VqNfWAUOO0d1Us",  # Use the dynamically selected voice
        output_format="mp3_44100_128",
        model_id="eleven_flash_v2_5",
        text="Hello from newscast! ",
    )

    audio_data = io.BytesIO()
    for chunk in audio:
        audio_data.write(chunk)

    Audio(audio_data.getvalue())

if __name__ == "__main__":
    main()
