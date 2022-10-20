
import string

def normalize_audio(s):

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    def remove_specialchar(text):
        char_to_replace = {'.': ' ', ',': ' ','?':' '}
        for k, v in char_to_replace.items():
            text = text.replace(k, v)
        return text
    
    return white_space_fix(remove_punc(remove_specialchar(lower(s))))


import csv

list_audio = []
with open("Audio_text - audio.csv", 'r', encoding="utf8") as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    list_audio.append([row[0], row[1], normalize_audio(row[2])])


# SAVE AUDIO
import codecs

audio = codecs.open('audio.csv', 'w', 'utf-8')
with audio:
    writer = csv.writer(audio)
    writer.writerows(list_audio)
