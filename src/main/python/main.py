import tensorflow as tf 
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input

def getPrediction(filename):   
    model = tf.keras.models.load_model('src/main/python/model/ModelF.h5')
    path = 'src/main/python/images/'+filename
    img = image.load_img(path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) 
    img_data = preprocess_input(x)
    class_names = ['Covid', 'Normal', 'Pneumonia', 'Tuberculosis']
    predictions = model.predict(img_data)
    newpred = np.argmax(predictions, axis=1)
    z=newpred[0]
    return (class_names[z])