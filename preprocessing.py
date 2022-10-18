from pydub import AudioSegment

def preprocessing(path):
    # CONVERT MP3 -> WAV
    type_file = path.split(".")[-1]
    sound = AudioSegment.from_file(path, type_file)
    sound.export("audio.wav", format="wav")

    # SPLIT AUDIO
    time_audio = int(sound.duration_seconds / 30) + 1
    for i in range(time_audio):
        t1 = i * 30 * 1000
        t2 = (i+1) * 30 * 1000
        newAudio = sound[t1:t2]

        newAudio.set_channels(0)   # single channel --> mono channel
        newAudio = newAudio.set_frame_rate(16000)    # convert frequency : mọi freq --> 16000kHz
        print(newAudio.frame_rate)
        print(newAudio.split_to_mono())
        newAudio.export('new_audio' + str(i) + '.wav', format="wav") 

preprocessing("file.mp3")



