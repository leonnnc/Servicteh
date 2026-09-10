# -*- coding: utf-8 -*-
"""Genera iconos PNG de Servitech (192 y 512) con Pillow."""
from PIL import Image, ImageDraw

TEAL = (14, 107, 102, 255)
WHITE = (255, 255, 255, 255)

# polígono de rayo (lucide zap) en viewBox 24
BOLT = [(13, 2), (3, 14), (10, 14), (9, 22), (21, 10), (14, 10), (13, 2)]


def make(size, path):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # fondo redondeado teal
    rad = int(size * 0.22)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=rad, fill=TEAL)
    # rayo blanco centrado
    u = size / 24.0
    pts = [(x * u, y * u) for (x, y) in BOLT]
    d.polygon(pts, fill=WHITE)
    img.save(path, 'PNG')


for s in (192, 512):
    make(s, 'assets/icon-%d.png' % s)
print('OK iconos generados')
