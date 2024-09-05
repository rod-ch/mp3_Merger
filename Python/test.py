from pydub import AudioSegment
import os
import time

def merge_audio_files(directory, output_file=None):
    combined = AudioSegment.empty()

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        if os.path.isfile(file_path) and file_name.lower().endswith(('.mp3', '.wav')):  # Check if it's a valid audio file
            audio_file = AudioSegment.from_file(file_path)
            combined += audio_file

    if not combined:
        print("No valid audio files found in the directory.")
        return

    output_file_path = output_file if output_file else os.path.join(os.path.dirname(directory), f"{os.path.basename(directory)}.mp3")

    # Create the output directory if it doesn't exist
    output_directory = os.path.dirname(output_file_path)
    os.makedirs(output_directory, exist_ok=True)

    combined.export(output_file_path, format="mp3")
    print(f"Combined audio exported to: {output_file_path}")

start_time = time.time()

files_directory = r"E:\Downloads\Crucial Conversations - Tools for Talking When Stakes are High_"
merge_audio_files(files_directory)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
