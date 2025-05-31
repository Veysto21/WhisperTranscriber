import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import os
os.environ["PATH"] += os.pathsep + r"E:\ffmpeg\ffmpeg-7.1.1-full_build-shared\bin"

import whisper

# Input/output paths
input_path = input("Enter the filename (e.g., Stairway_To_Heaven.wav)and make sure it's in the 'audio' folder: ")
input_path = f"E:/WhisperTranscriber/audio/{input_path}"
output_folder = "E:/WhisperTranscriber/transcripts"
base_name = os.path.splitext(os.path.basename(input_path))[0]
output_file = os.path.join(output_folder, base_name + ".txt")

# Ask before overwriting
if os.path.exists(output_file):
    response = input(f"Warning! '{base_name}.txt' already exists. Overwrite? (y/n): ").strip().lower()
    if response != "y":
        print("Skipping transcription.")
        exit()

# Load model
model = whisper.load_model("base")

# Transcribe
result = model.transcribe(input_path)

# Save output
os.makedirs(output_folder, exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Transcription complete!")
