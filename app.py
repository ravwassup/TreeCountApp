import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="TreeCountApp – Test", layout="wide")

st.title("🌳 TreeCountApp – Testowy podgląd mapy")
st.markdown("Wgraj ortofotomapę (plik `.jpg`, `.png`) i wyświetl ją poniżej.")

# Wczytanie pliku graficznego
uploaded_file = st.file_uploader("Wybierz plik z ortofotomapą", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Przekształcenie na obraz (PIL -> OpenCV)
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    st.subheader("Podgląd mapy:")
    st.image(image_np, use_column_width=True, caption="Wczytana ortofotomapa")

    # Informacyjnie: rozmiar
    h, w, _ = image_np.shape
    st.write(f"Rozdzielczość obrazu: {w} x {h}")
    