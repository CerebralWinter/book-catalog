from PIL import Image
import pytesseract
import os
from insert import insert_book

# Path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Get latest image
CAPTURE_DIR = os.path.join(os.path.dirname(__file__), '..', 'captures')
images = [f for f in os.listdir(CAPTURE_DIR) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
if not images:
    print("No images found.")
    exit()

latest_image = max(images, key=lambda x: os.path.getctime(os.path.join(CAPTURE_DIR, x)))
image_path = os.path.join(CAPTURE_DIR, latest_image)

# OCR
image = Image.open(image_path)
raw_text = pytesseract.image_to_string(image, lang='ita+eng')

# Heuristic parsing
lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
title_candidates = [line for line in lines if len(line) > 15 and line.isupper()]
author_candidates = [line for line in lines if line.istitle() and 5 <= len(line) <= 30]

title = title_candidates[0] if title_candidates else lines[0] if lines else "UNKNOWN"
author = author_candidates[0] if author_candidates else "UNKNOWN"

# Preview
print(f"\n--- OCR Text ---\n{raw_text}\n")
print(f"→ Parsed title:  {title}")
print(f"→ Parsed author: {author}")

# Confirm (temporary manual confirmation)
input("Press ENTER to save, or CTRL+C to cancel...")

# Insert into DB
insert_book(title, author, image_path)
