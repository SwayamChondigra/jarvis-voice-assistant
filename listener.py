import speech_recognition as sr

def listen(timeout=None, phrase_time_limit=6):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = r.listen(source, timeout=timeout,
                             phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            return ""
    try:
        return r.recognize_google(audio).lower()
    except:
        return ""
