import cv2
from deepface import DeepFace
import time
from collections import Counter

def detect_emotion():
    """
    Emotion Detection Using AI Concepts:

    1. Data Collection (Search Tree Nodes):
       - Capture multiple frames (nodes) from webcam representing different states.
    
    2. Preprocessing:
       - Resize frames for uniform input to the ML model.
    
    3. Feature Extraction & ML Prediction:
       - Use DeepFace's pretrained CNN model to extract features and classify emotions.
    
    4. Decision Making using MinMax-like Majority Voting:
       - Treat each frame's detected emotion as a leaf node value.
       - Aggregate using majority voting (like MinMax chooses best move from child nodes).
    
    5. Output:
       - Return the most confident (majority) emotion as the final decision.
    """

    cap = cv2.VideoCapture(0)
    emotions_detected = []
    frame_count = 5

    print("Starting emotion detection. Keep your face clearly visible.")

    for i in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            continue

        # Preprocessing (uniform input)
        frame = cv2.resize(frame, (640, 480))
        temp_path = f"temp_frame_{i}.jpg"
        cv2.imwrite(temp_path, frame)

        try:
            # ML-based emotion prediction from pretrained CNN model
            result = DeepFace.analyze(img_path=temp_path, actions=['emotion'], enforce_detection=False)
            emotions = result[0]['emotion']

            # Dominant emotion from current frame (leaf node value)
            dominant = max(emotions, key=emotions.get)
            emotions_detected.append(dominant)

            print(f"[Frame {i+1}] Detected: {dominant}, Scores: {emotions}")

        except Exception as e:
            print(f"[Frame {i+1}] Detection failed:", e)

        time.sleep(1)

    cap.release()

    if emotions_detected:
        # Decision Making (MinMax analogy):
        # From all leaf nodes (frame emotions), select the most frequent (optimal decision)
        final_emotion = Counter(emotions_detected).most_common(1)[0][0]
        print(f"\n🎯 Final Detected Emotion (majority vote): {final_emotion}")
        return final_emotion
    else:
        print("❌ No emotion detected.")
        return None
