import numpy as np
#import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from PIL import Image


def load_preproc_img(img: str) -> np.array:
    new_w, new_h = 300,300
    img = np.array(Image.open(img).resize((new_w, new_h)))
    img = img / 255 #normalize pixel values; img /= 255. wouldn't work here
    img = np.expand_dims(img, axis=0)
    img = np.vstack([img])
    return img

@st.experimental_singleton
def get_model():
    return load_model('rock_paper_scissors_CNN.h5')

@st.experimental_memo
def save_image(file) -> None:
    '''Saves locally the attached file.'''
    with open(file.name,"wb") as f:
        f.write(file.getbuffer())
    return file.name