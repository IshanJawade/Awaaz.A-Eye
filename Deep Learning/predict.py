import tensorflow as tf 
import numpy as np
import pickle
import cv2

CATEGORIES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q' ,'R' , 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'del', 'nothing', 'space']

model = tf.keras.models.load_model('/home/ishan/Deep Learning/Trained models/ASL_model.pb')

img = "/home/ishan/Deep Learning/asl-alphabet/asl_alphabet_test/asl_alphabet_test/L_test.jpg"

img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)

img = img.astype(float)

img = cv2.resize(img,(50,50))

img = np.reshape(img,(1,50,50,1))

pred = model.predict(img)

ans = CATEGORIES[np.argmax(pred)]

print("The predicted alphabet is '{}' ".format(ans))
