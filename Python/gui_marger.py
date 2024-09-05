from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import os

def merge_audio_files(files, output_file=None):
    combined = AudioSegment.empty()

    for file_path in files:
        if os.path.isfile(file_path):
            audio_file = AudioSegment.from_file(file_path)
            combined += audio_file

    if not combined:
        print("No valid audio files found in the selected files.")
        return

    output_file_path = output_file if output_file else os.path.join(os.path.dirname(files[0]), "merged_output.mp3")
    
    combined.export(output_file_path, format="mp3")
    print(f"Files merged successfully into {output_file_path}")

def select_files_to_merge():
    files = filedialog.askopenfilenames(
        title="Select files to merge",
        filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*"))
    )
    if files:
        listbox.delete(0, tk.END)
        for file in files:
            listbox.insert(tk.END, file)
        StartMarger.config(command=lambda: start_merging(files))

def select_files_path():
    directory = filedialog.askdirectory(
        title="Select Directory to Save Merged File"
    )
    return directory

def start_merging(files):
    output_dir = select_files_path()
    if output_dir:
        output_file = os.path.join(output_dir, "merged_output.mp3")
        merge_audio_files(files, output_file)

window = Tk()
window.geometry("560x540")
window.title("MP3 Merger")

# Button to select what to merge
select_button = Button(window, text="Select MP3 Files", command=select_files_to_merge)
select_button.pack(pady=10)

# Label
label = Label(window, text="Selected MP3 Files:")
label.pack(pady=10)

# Listbox
listbox = Listbox(window, width=50, height=10, activestyle='dotbox')
listbox.pack(pady=10)

# Scrollbar for Listbox
scrollbar = Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Button to start merging
StartMarger = Button(window, text='Start Merging')
StartMarger.pack(pady=10)

window.mainloop()
