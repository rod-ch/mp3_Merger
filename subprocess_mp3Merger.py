from pydub import AudioSegment

# Load the mp3 files you want to merge
audio1 = AudioSegment.from_mp3(r"E:\Downloads\The Game Neil Strauss\The_Game_ Penetrating_the_Secret_Society_of_Pickup_Artists_Part_1.mp3")
audio2 = AudioSegment.from_mp3(r"E:\Downloads\The Game Neil Strauss\The_Game_ Penetrating_the_Secret_Society_of_Pickup_Artists_Part_2.mp3")

# Combine them
combined = audio1 + audio2

# Export the combined audio
combined.export(r"C:\Users\rodri\OneDrive\Escritorio", format="mp3")
print("lol")