from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
import imageio
import numpy as np
import os
from django.conf import settings

def create_text_image(text, height=100, fontsize=40):
    try:
        font = ImageFont.truetype("arial.ttf", fontsize)
    except IOError:
        font = ImageFont.load_default()

    text_bbox = font.getbbox(text)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    img = Image.new('RGB', (text_width + 100, height), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    text_y = (height - text_height) // 2

    draw.text((50, text_y), text, font=font, fill=(255, 255, 255))

    return np.array(img), text_width + 100

def create_video(text):
    fps = 24
    duration = 3
    text_image, text_image_width = create_text_image(text, height=100, fontsize=40)

    frames = []
    total_frames = int(fps * duration)
    shift_per_frame = text_image_width / total_frames

    for i in range(total_frames):
        shift = int(shift_per_frame * i)
        frame = np.roll(text_image, -shift, axis=1)
        frames.append(frame[:, :100])

    # байтовый объект для хранения видео
    video_data = BytesIO()
    with imageio.get_writer(video_data, format='mp4', fps=fps) as writer:
        for frame in frames:
            writer.append_data(frame)

    # байтовое представление видео
    return video_data.getvalue()