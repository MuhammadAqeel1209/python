import tkinter as tk
from tkinter import filedialog
import threading

from detector.emotion_detector import detect_emotion
from detector.voice_emotion import detect_emotion as detect_emotion_voice
from detector.text_emotion import detect_emotion as detect_emotion_text
from player.music_player import play_music

class EmotionApp:
    """
    A GUI application that detects emotions from face, voice, or text input
    and plays corresponding music based on the detected emotion.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Music Theme")
        self.root.geometry("600x500")
        self.root.config(bg="#222831")

        self.title_label = tk.Label(root, text="🎵 Welcome to Emotion Music Theme 🎵",
                                    font=("Helvetica", 20, "bold"), fg="#00ADB5", bg="#222831")
        self.title_label.pack(pady=20)

        self.option_label = tk.Label(root, text="Choose Emotion Detection Mode:",
                                     font=("Helvetica", 14), fg="white", bg="#222831")
        self.option_label.pack(pady=10)

        self.btn_face = tk.Button(root, text="Face", font=("Helvetica", 14),
                                  command=self.handle_face, bg="#393E46", fg="white", width=20)
        self.btn_face.pack(pady=10)

        self.btn_voice = tk.Button(root, text="Voice", font=("Helvetica", 14),
                                   command=self.handle_voice, bg="#393E46", fg="white", width=20)
        self.btn_voice.pack(pady=10)

        self.btn_text = tk.Button(root, text="Text", font=("Helvetica", 14),
                                  command=self.handle_text, bg="#393E46", fg="white", width=20)
        self.btn_text.pack(pady=10)

        self.status_label = tk.Label(root, text="", font=("Helvetica", 12), fg="white", bg="#222831")
        self.status_label.pack(pady=20)

    def handle_face(self):
        """Handle face emotion detection button click"""
        self.status_label.config(text="Detecting emotion from face...")
        threading.Thread(target=self.run_face).start()

    def handle_voice(self):
        """Handle voice emotion detection button click"""
        file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if file_path:
            self.status_label.config(text="Detecting emotion from voice...")
            threading.Thread(target=self.run_voice, args=(file_path,)).start()

    def handle_text(self):
        """Handle text emotion detection button click"""
        self.top_text = tk.Toplevel(self.root)
        self.top_text.title("Enter Text")
        self.top_text.geometry("400x200")
        self.top_text.config(bg="#222831")

        label = tk.Label(self.top_text, text="Enter text to analyze:", font=("Helvetica", 12),
                         bg="#222831", fg="white")
        label.pack(pady=10)

        self.text_entry = tk.Entry(self.top_text, font=("Helvetica", 12), width=40)
        self.text_entry.pack(pady=10)

        submit_btn = tk.Button(self.top_text, text="Analyze", command=self.run_text,
                               font=("Helvetica", 12), bg="#00ADB5", fg="white")
        submit_btn.pack(pady=10)

    def run_face(self):
        """Run face emotion detection"""
        emotion = detect_emotion()
        self.display_result(emotion)

    def run_voice(self, file_path):
        """Run voice emotion detection"""
        emotion = detect_emotion_voice(file_path)
        self.display_result(emotion)

    def run_text(self):
        """Run text emotion detection"""
        text = self.text_entry.get()
        self.top_text.destroy()
        emotion = detect_emotion_text(text)
        self.display_result(emotion)

    def display_result(self, emotion):
        """Display detected emotion and play corresponding music"""
        self.status_label.config(text=f"Detected Emotion: {emotion.capitalize()}\nPlaying music...")
        play_music(emotion)

def main():
    """Initialize and run the application"""
    root = tk.Tk()
    app = EmotionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
