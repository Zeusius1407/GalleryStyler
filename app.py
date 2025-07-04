import streamlit as st
from PIL import Image
import os

st.title("Before & After Style Transfer")

# Directory paths
content_dir = "images"
output_dir = "outputs"
style_dir = "styles"

# List of available images (ensure names match)
image_files = [f for f in os.listdir(content_dir) if f.endswith(('.jpg', '.png', 'jpeg'))]
style_files = [s for s in os.listdir(style_dir) if s.endswith(('.jpg', '.png', 'jpeg'))]
# Select image
selected_image = st.selectbox("Choose an image to view:", image_files)
selected_style = st.selectbox("Choose the style:", style_files)
save_style = selected_style.split('.')[0]
selected_output = f'{save_style}_{selected_image}'
# Load before and after
before = Image.open(os.path.join(content_dir, selected_image))
after = Image.open(os.path.join(output_dir, selected_output))

col1, col2 = st.columns(2)
with col1:
    st.subheader("Before")
    st.image(before)
with col2:
    st.subheader("After")
    st.image(after)

