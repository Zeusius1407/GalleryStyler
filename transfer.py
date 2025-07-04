import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
from PIL import Image
import os

def load_image(path, target_size=(512, 512)):
    img = Image.open(path).convert('RGB')
    img = img.resize(target_size)
    img = np.array(img) / 255.0
    return tf.constant(img, dtype=tf.float32)[tf.newaxis, :]

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def stylize(content_path, style_path, output_path):
    content = load_image(content_path)
    style = load_image(style_path)
    output = model(content, style)[0]
    tf.keras.preprocessing.image.save_img(output_path, output[0])

try:
    os.mkdir("outputs")
except FileExistsError:
    shutil.rmtree('outputs')
    os.mkdir("outputs")

for style_name in os.listdir("styles"):
    save_name = style_name.split('.')[0]
    for img_name in os.listdir('images'):
        content_path = f'images/{img_name}'
        style_path = f'styles/{style_name}'
        output_path = f'outputs/{save_name}_{img_name}'
        stylize(content_path, style_path, output_path)
