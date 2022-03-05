import os
import argparse
import errno
from pathlib import Path
from typing import final
import cv2
import numpy as np
from keras.models import load_model

os.system("cls")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group('required named arguments')
    
    requiredNamed.add_argument("-ds_p", "--dataset_path", help="Path to Image file", type=Path, required=True)
    requiredNamed.add_argument("-m_p", "--model_path", help="Path to model", type=Path, required=True)
    requiredNamed.add_argument("-op_p", "--output_path", help="Destination Path", type=Path, required=True)
    # parser.parse_args(['-h'])
    
    p = parser.parse_args()
    model_path = p.model_path

    if p.dataset_path.exists() == False:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), p.dataset_path)
    
    elif p.dataset_path.exists() == True:
        print(f"Dataset Path = {p.dataset_path}")    
        final_dataset_path = p.dataset_path

    if p.output_path.exists() == False:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), p.dataset_path)

    elif p.output_path.exists() == True:   
        print(f"Output Path = {p.output_path}")
        final_output_path = p.output_path       
    
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

image,processed_img = preprocess_image(f'{final_dataset_path}')

model=load_saved_model(f'{model_path}')

# predict
d1,d2,d3,d4,d5,d6,d7 = model.predict(processed_img)

mask = get_mask(d1)
out = get_output(image,mask)

image,processed_img = preprocess_image(f'{final_dataset_path}')