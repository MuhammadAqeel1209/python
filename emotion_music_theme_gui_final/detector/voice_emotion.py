
import librosa
import numpy as np
import joblib  # For loading pretrained model

# Load a dummy trained model (included as a file in the zip)
model = joblib.load('detector/voice_emotion_model.pkl')

def extract_features(file_path):
    y, sr = librosa.load(file_path, duration=3, offset=0.5)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

def detect_emotion(audio_path):
    features = extract_features(audio_path)
    features = features.reshape(1, -1)
    emotion = model.predict(features)[0]
    return emotion
