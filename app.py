import streamlit as st
import cv2
import numpy as np
from kaleidoscope_utils import load_image, kaleidoscope_effect, apply_trippy_colormap

st.set_page_config(page_title="AI Kaleidoscope", layout="centered")

st.title("🌀 AI-Powered Kaleidoscope Generator")
st.write("Upload an image to generate symmetrical, trippy patterns!")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = load_image(uploaded_file)
    st.image(img, caption="Original Image", use_container_width=True)

    segments = st.slider("Number of Segments", min_value=4, max_value=12, value=6, step=1)
    kaleido_img = kaleidoscope_effect(img, segments)
    st.image(kaleido_img, caption=f"Kaleidoscope Pattern ({segments} segments)", use_column_width=True)

    if st.checkbox("Add Trippy Colors"):
        colormap_name = st.selectbox("Choose a Colormap", [
            "PLASMA", "INFERNO", "MAGMA", "TURBO", "OCEAN", "RAINBOW"
        ])

        colormap_dict = {
            "PLASMA":  cv2.COLORMAP_PLASMA,
            "INFERNO": cv2.COLORMAP_INFERNO,
            "MAGMA":   cv2.COLORMAP_MAGMA,
            "TURBO":   cv2.COLORMAP_TURBO,
            "OCEAN":   cv2.COLORMAP_OCEAN,
            "RAINBOW": cv2.COLORMAP_RAINBOW
        }

        trippy_img = apply_trippy_colormap(kaleido_img, colormap_dict[colormap_name])
        st.image(trippy_img, caption=f"Trippy Kaleidoscope - {colormap_name}", use_column_width=True)

    st.success("✨ Done! Upload another image to explore more patterns.")
