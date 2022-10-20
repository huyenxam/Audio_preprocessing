
import os
from pydub import AudioSegment

directory = '99'
new_directory = 'audio'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    sound = AudioSegment.from_file(f, "wav")

    file_name_audio = filename.split(".")[0] + ".mp3"
    f_new = os.path.join(new_directory, file_name_audio)
    print(f_new)
    sound.export(f_new, format="mp3")
