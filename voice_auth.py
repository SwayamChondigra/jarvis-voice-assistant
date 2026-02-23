from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wavfile
import os

encoder = VoiceEncoder()

def record(filename, seconds=3):
    fs = 16000
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    wavfile.write(filename, fs, audio)

def create_voiceprint():
    record("owner.wav")
    wav = preprocess_wav("owner.wav")
    embed = encoder.embed_utterance(wav)
    np.save("voiceprint.npy", embed)

def authenticate():
    if not os.path.exists("voiceprint.npy"):
        create_voiceprint()

    record("temp.wav")
    wav = preprocess_wav("temp.wav")
    embed = encoder.embed_utterance(wav)

    saved = np.load("voiceprint.npy")
    similarity = np.dot(embed, saved)

    print("Voice similarity:", similarity)
    return similarity > 0.75
