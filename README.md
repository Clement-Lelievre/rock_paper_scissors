# Transfer learning from VGG16 using Tensorflow and Keras. 

The goal is to create an app where the model recognizes hand pose live (rock, paper, or scissor). 
The training dataset has been found on Laurence Moroney's personal website.
The model is stored in a .h5 file that weighs about 170 mB; as this breaches Github's storage limits (100mB), I use git lfs to push it to the repo (https://git-lfs.github.com/)
Also, because the total size of the project exceeds Heroku limits (500 mB), I'll deploy the app on Streamlit cloud (where the limit is 1gB so that fits)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/clement-lelievre/rock_paper_scissors/app.py)

![](https://github.com/Clement-Lelievre/rock_paper_scissors/blob/master/rock-paper-scissor-ft.jpg)
