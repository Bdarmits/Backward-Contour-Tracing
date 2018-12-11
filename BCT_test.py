from BackwardContourTracing import *
from PIL import Image

def test(path):
    img = Image.open(path)
    BCT(img, [120, 120])
