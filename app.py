#import cv2
import streamlit as st
from utils import get_model, load_preproc_img, save_image
import numpy as np

st.title('Rock, paper, scissors image recognition')

model = get_model()
preds = ['paper', 'rock', 'scissors']
preds_emoji = ['📜', '⛰️', '✂️']

cam = st.camera_input('Take a screenshot and get a prediction')

if cam:
    filename = save_image(cam)
    ind = np.argmax(model.predict(load_preproc_img(filename), batch_size=1))
    pred_emoji = preds_emoji[ind]
    st.write(pred_emoji)
# run = st.checkbox('run')
# FRAME_WINDOW = st.image([])
# cam = cv2.VideoCapture(0)
    
    
# while run:
#     ret, frame = cam.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     ind = np.argmax(model.predict(load_preproc_img(frame), batch_size=1))
#     pred, pred_emoji = preds[ind], preds_emoji[ind]
#     cv2.putText(frame, pred, (frame.shape[1]//2 - 10,20), cv2.FONT_HERSHEY_TRIPLEX,  0.7, (0, 255, 0), 1)
#     FRAME_WINDOW.image(frame, caption= pred_emoji)

# photo_upload = st.file_uploader('Upload image', type = ['jpg', 'png'])
# if photo_upload:
#     st.write(model.predict(load_preproc_img(photo_upload)))
