import numpy as np
import cv2
from PIL import Image

def load_image(uploaded_file):
    image = Image.open(uploaded_file).convert("RGB")
    image = image.resize((512, 512))
    return np.array(image)

def kaleidoscope_effect(img, segments=6):
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    result = np.zeros_like(img)
    angle = 360 // segments

    for i in range(segments):
        M = cv2.getRotationMatrix2D(center, i * angle, 1.0)
        rotated = cv2.warpAffine(img, M, (w, h))
        mask = np.zeros((h, w), dtype=np.uint8)
        cv2.ellipse(mask, center, (w//2, h//2), 0, i*angle, (i+1)*angle, 255, -1)
        for c in range(3):
            result[:, :, c] = np.where(mask == 255, rotated[:, :, c], result[:, :, c])
    return result

def apply_trippy_colormap(img, colormap):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    colorized = cv2.applyColorMap(gray, colormap)
    return cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)
