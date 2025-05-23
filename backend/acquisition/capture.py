import cv2
import os
from datetime import datetime

# Define path where images will be saved
SAVE_DIR = os.path.join(os.path.dirname(__file__), '..', 'captures')
os.makedirs(SAVE_DIR, exist_ok=True)

# Initialize default webcam (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit()

print("Press SPACE to capture the image, ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to read frame.")
        break

    cv2.imshow("Press SPACE to capture", frame)
    key = cv2.waitKey(1)

    if key == 27:  # ESC key
        break
    elif key == 32:  # SPACE key
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cover_{timestamp}.jpg"
        filepath = os.path.join(SAVE_DIR, filename)
        cv2.imwrite(filepath, frame)
        print(f"Image saved to: {filepath}")

cap.release()
cv2.destroyAllWindows()
