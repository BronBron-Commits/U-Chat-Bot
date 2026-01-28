import subprocess
from pathlib import Path
import sys

VOICE = Path("voices/en_US-amy-low.onnx")

def speak(text: str):
    if not VOICE.exists():
        subprocess.run(["espeak-ng", text])
        return

    p1 = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "piper",
            "--model",
            str(VOICE),
            "--output-raw",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    p2 = subprocess.Popen(
        ["aplay", "-r", "22050", "-f", "S16_LE"],
        stdin=p1.stdout,
    )

    p1.stdin.write(text.encode())
    p1.stdin.close()
    p2.wait()
