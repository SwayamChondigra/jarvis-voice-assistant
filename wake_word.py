import pvporcupine
import pyaudio
import struct
import os

def wait_for_wake_word():
    porcupine = pvporcupine.create(
        access_key=os.getenv("PICOVOICE_ACCESS_KEY"),
        keywords=["jarvis"]
    )

    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🟢 Waiting for wake word (offline)...")

    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        if porcupine.process(pcm) >= 0:
            break

    stream.close()
    pa.terminate()
    porcupine.delete()
