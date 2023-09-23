print("hello world")
with open('yourfile.mp3', 'rb') as mp3_file:
  mp3_data = mp3_file.read()

# Save the binary MP3 data to a file
with open('saved_file.mp3', 'wb') as saved_file:
  saved_file.write(mp3_data)
