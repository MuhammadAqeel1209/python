from detector.emotion_detector import detect_emotion
from detector.voice_emotion import detect_emotion as detect_emotion_voice
from detector.text_emotion import detect_emotion as detect_emotion_text
from player.music_player import play_music

def main():
    source = input("Enter input source (face/voice/text): ").strip().lower()

    if source == "face":
        emotion = detect_emotion()
    elif source == "voice":
        audio_path = input("Enter path to audio file (WAV format): ").strip()
        emotion = detect_emotion_voice(audio_path)
    elif source == "text":
        text = input("Enter text: ").strip()
        emotion = detect_emotion_text(text)
    else:
        print("Invalid source selected.")
        return

    print(f"Detected emotion: {emotion}")
    play_music(emotion)

if __name__ == "__main__":
    main()
