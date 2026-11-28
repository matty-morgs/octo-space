"""Recover a transparent PNG from two Figma renders of the same overlay,
one on a white background and one on black.  alpha = 1 - (W - B) / 255,
colour = B / alpha.  Usage: python3 matte.py white.png black.png out.png"""
import sys
import numpy as np
from PIL import Image
w = np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(np.float32)
b = np.asarray(Image.open(sys.argv[2]).convert('RGB')).astype(np.float32)
a = np.clip(1.0 - (w - b).mean(axis=2) / 255.0, 0, 1)
c = np.clip(np.where(a[..., None] > 1e-3, b / np.maximum(a[..., None], 1e-3), 0), 0, 255)
Image.fromarray(np.dstack([c, a * 255]).astype(np.uint8), 'RGBA').save(sys.argv[3], optimize=True)
