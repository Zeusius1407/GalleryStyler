# GalleryStyler
This is a tool which applies styles to any photo as required by the user.
# Tech stack used:
Image processing: Pillow \
User Interface: Streamlit \
Style Transfer: TensorFlow \
Scripting: Python 

# Working
It leverages Neural Style Transfer and uses a pre-trained arbitrary-image-stylization-v1-256 from TensorFlow Hub which can be found [here](https://www.kaggle.com/models/google/arbitrary-image-stylization-v1/tensorFlow1/256/2?tfhub-redirect=true). There are 3 directories present in this repo, an images directory containing sample images which are to be used as content_img, a styles directory containing sample styles which are to be transfered to the content_img, and finally an output directory containing the stylized images.
The scrpit transfer.py is responsible for style transfer and the script app.py is responsible for diplaying the output stylized images.

# How to run the model

Download the images, styles and outputs repository along with both the python scripts.\
Run the transfer.py file by using this command in the terminal
```
python transfer.py
```
Now to display the output images run the following command in the terminal
```
streamlit run app.py
```
This will open a new tab in the user's browser where they can select the content image and style image as per their liking.
