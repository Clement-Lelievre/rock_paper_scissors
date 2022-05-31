import numpy as np
#import cv2
from tensorflow.keras.models import load_model
import streamlit as st

def load_preproc_img(img: np.array) -> np.array:
    new_h, new_w = 300,300
    img = cv2.resize(img, (new_w, new_h))
    img = img / 255 #normalize pixel values
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