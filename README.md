# WhisperTranscriber

A simple and lightweight Python script that transcribes audio files to text using OpenAI's [Whisper](https://github.com/openai/whisper) speech recognition model.

This tool supports common formats like `.mp3`, `.wav`, `.wma`, `.m4a`, and more — powered by `ffmpeg`.

---

## 📁 Project Structure

WhisperTranscriber/

├── audio/ # Place your audio files here

├── transcripts/ # Transcripts are saved here as .txt

├── transcribe_whisper.py # Main transcription script

├── README.md # You're reading it

---

## 🛠 Requirements

- Python 3.9+
- [OpenAI Whisper](https://github.com/openai/whisper)
- [ffmpeg](https://ffmpeg.org/) (must be installed and added to your system PATH)

---

## 📦 Installation

### 1. Install dependencies:

```bash
pip install git+https://github.com/openai/whisper.git


Place your audio file in the audio/ folder and run the script:
python transcribe_whisper.py

