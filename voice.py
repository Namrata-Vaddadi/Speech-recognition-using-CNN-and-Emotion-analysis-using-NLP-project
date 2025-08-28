from keras.models import load_model
import librosa
import IPython.display as ipd
import numpy as np
model = load_model(r'C:\Users\namra\Downloads\speech and emotion analysis project\voiceRecModel.keras')

import sounddevice as sd
print(sd.query_devices())

import sounddevice as sd
import soundfile as sf
samplerate=16000
duration=1
filename='voiceRec.wav'
print("start")
mydata=sd.rec(int(samplerate*duration),samplerate=samplerate,channels=1,blocking=True)
print("end")
sd.wait()
sf.write(filename,mydata,samplerate)

samples,sample_rate=librosa.load(filename,sr=16000)
samples=librosa.resample(y=samples,orig_sr=16000,target_sr=8000)
ipd.Audio(samples,rate=8000)

classes=["bed"," bird","cat","dog","eight","down"]
def predict(audio):
    prob=model.predict(audio.reshape(1,8000,1))
    index=np.argmax(prob[0])
    return classes[index]
predict(samples)