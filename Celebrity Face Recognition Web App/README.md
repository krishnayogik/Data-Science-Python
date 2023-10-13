# Celebrity Identifier Web App

This web application uses machine learning to identify Bollywood celebrities from uploaded photos. It leverages a dataset containing localized faces of 100 Bollywood celebrities for training and classification purposes.

## Dataset

Link: https://www.kaggle.com/datasets/sushilyadav1998/bollywood-celeb-localized-face-dataset

The dataset used for training contains localized face images of 100 Bollywood celebrities. Each class has samples of size 64 X 64 pixels, with varying conditions such as different orientations, illuminations, age transitions, and more. This dataset is ideal for testing generative and face recognition models, and it can also be used to reconstruct image samples using generative models like Variational Autoencoders and Generative Adversarial Networks.

## Installation

To run the application, you'll need to install the following dependencies using pip:

```
pip install mtcnn==0.1.0
pip install tensorflow==2.3.1
pip install keras==2.4.3
pip install keras-vggface==0.6
pip install keras_applications==1.0.8
```
## Demo 


https://github.com/krishnayogik/Data-Science-Python/assets/7524417/00e27217-3514-4460-8f81-d35827133b0e

## Usage
- Clone this repository to your local machine.
- Install the required dependencies using the provided pip commands.
- Run the Streamlit web app using the following command:
  
```
streamlit run app.py
```

## Model Architecture
We'll use a pre-trained VGGFace model for feature extraction and then train a classifier on top of these features to identify Bollywood celebrities. Here's a high-level model architecture:

- Pre-trained VGGFace Model:
  Base Model: VGGFace pre-trained on a large face recognition dataset.
  We use this model to extract features from the face images.

- Additional Classifier:
  We add a classifier on top of the pre-trained VGGFace model to classify the features into Bollywood celebrities.

## Entertainment and Engagement:

The app can entertain users by providing a fun way to identify celebrities, encouraging them to share the results and engage with the app.






