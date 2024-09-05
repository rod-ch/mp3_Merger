from pydub import AudioSegment
import os
import time
from concurrent.futures import ThreadPoolExecutor

def merge_audio_files(files, output_file = None):
    start_time = time.time()
    files_paths = files
    combined = AudioSegment.empty()
    file_list = os.listdir(files_paths)

    def load_audio(file_name):
        return AudioSegment.from_file(os.path.join(files_paths, file_name))

    with ThreadPoolExecutor() as executor:
        audio_segments = list(executor.map(load_audio, file_list))

    combined = sum(audio_segments)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

    if output_file != None:
        combined.export(output_file, format="mp3")
        print(f"Combined audio exported to: {output_file}")

    else:
        parent_path = os.path.dirname(files_paths)
        output_file_name = os.path.basename(parent_path) +'.mp3'
        output_file_path = os.path.join(parent_path, output_file_name)
        combined.export(output_file_path, format="mp3")
        print(f"Combined audio exported to: {output_file_path}")

files_paths = r"E:\Downloads\Extreme Ownership"

merge_audio_files(files_paths)
