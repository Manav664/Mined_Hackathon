from importlib.resources import path
import cv2
import numpy as np
from keras.models import load_model
import paths

def preprocess_image(image_path):
    # load image
    image = cv2.imread(image_path)

    # convert to array
    blob = cv2.dnn.blobFromImage(image, 1.0/255, (320, 320), (0, 0, 0), swapRB=True, crop=False)

    return image,blob

def load_saved_model(model_path):
    model = model_path
  
    # load model
    model = load_model(model, compile=False)
  
    return model

def get_mask(d1):
    pred = np.array(d1[:,0,:,:])[0]

    # normalize
    ma = np.max(pred)
    mi = np.min(pred)
    pred = (pred-mi)/(ma-mi)

    pred = pred.squeeze()

    pred = (pred*255).astype(np.uint8)

    mask = cv2.resize(pred, image.shape[1::-1], interpolation=cv2.INTER_CUBIC)
    return mask

def get_output(image,mask):
    b, g, r = cv2.split(image)
    out = cv2.merge((b, g, r, mask))
    return out

def something():
    image,processed_img = preprocess_image(f'{paths.final_dataset_path}')

    model=load_saved_model('/content/drive/MyDrive/temp_data_storage/u2net_keras.h5')

    # predict
    d1,d2,d3,d4,d5,d6,d7 = model.predict(processed_img)

    mask = get_mask(d1)
    out = get_output(image,mask)

image,processed_img = preprocess_image(f'{paths.final_dataset_path}')