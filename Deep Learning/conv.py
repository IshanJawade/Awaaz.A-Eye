import tensorflow as tf 

model = tf.keras.models.load_model("/home/ishan/Documents/yolo_v2.pb")
var = tf.lite.TFLiteConverter.from_keras_model(model)
conv = var.convert()
with open('yolo_v2.tflite','wb') as f:
    f.write(conv)
