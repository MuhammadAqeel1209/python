
import text2emotion as te

def detect_emotion(text):
    emotions = te.get_emotion(text)
    if not emotions:
        return 'neutral'
    return max(emotions, key=emotions.get)
