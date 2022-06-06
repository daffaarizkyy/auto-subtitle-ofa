import subprocess
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import os
from googletrans import Translator
import pandas as pd
import srt
from datetime import timedelta
import audiosegment


class subtitle():
    def __init__(self, filename, filetype):
        self.path = "uploads"
        self.filename = filename
        self.filetype = filetype
        self.videoToWav()
        self.createSubtitle(self.toDataset(self.separateWav()))

    def videoToWav(self):
        command = f"ffmpeg -i \"{self.path}/{self.filename}{self.filetype}\" -ab 160k -ac 2 -ar 44100 -vn \"{self.path}/{self.filename}.wav\""
        subprocess.call(command, shell=True)
        os.remove(f"{self.path}/{self.filename}{self.filetype}")

    def separateWav(self):
        audio = f"{self.path}/{self.filename}.wav"

        sound_file = audiosegment.from_file(audio)
        sound_file = sound_file.resample(
            sample_rate_Hz=48000, sample_width=2, channels=1)
        results = sound_file.detect_voice()

        audio_chunks = [tup[1] for tup in results]

        for i, chunk in enumerate(audio_chunks):
            out_file = f"{self.path}/chunk{i}.wav"
            chunk.export(out_file, format="wav")
        os.remove(f"{self.path}/{self.filename}.wav")
        return len(audio_chunks)

    def toDataset(self, sumChunks):
        translator = Translator()
        r = sr.Recognizer()
        subtitle = []
        duration = []
        translate = []

        for x in range(sumChunks):
            audio = f"{self.path}/chunk{x}.wav"
            with sr.AudioFile(audio) as source:
                r.adjust_for_ambient_noise(source, duration=0)
                audio = r.listen(source)
                try:
                    a = r.recognize_google(audio)
                    subtitle.append(a)
                    duration.append(source.DURATION)
                    result = translator.translate(a, dest='id')
                    translate.append(result.text)
                except:
                    subtitle.append("-")
                    duration.append(source.DURATION)
                    translate.append("-")
            os.remove(f"{self.path}/chunk{x}.wav")
        return pd.DataFrame(zip(subtitle, duration, translate))

    def createSubtitle(self, df):
        sub = []
        now = 0
        for index, row in df.iterrows():
            end = round(row[1] * 1000)

            if(row[2] != '-'):
                tempSrt = srt.Subtitle(
                    index+1, timedelta(milliseconds=now), timedelta(milliseconds=now+end), row[2])
                sub.append(tempSrt)

            now = now + end
        subtitle = srt.compose(sub)
        f = open(f"{self.path}/{self.filename}-subtitle.srt", "w")
        f.write(subtitle)
        f.close()
