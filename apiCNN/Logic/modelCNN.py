from django.db import models
from django.urls import reverse
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer, ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.python.keras.models import load_model, model_from_json
from keras import backend as K
from apiCNN import models
import os
from tensorflow.python.keras.models import Sequential
import pathlib
from PIL import Image
from django.conf import settings

class modelCNN():
    """CNN Class Model"""

    Selectedmodel = Sequential()
    CLASS_NAMES = ['Montaña', 'Calle', 'Glaciar', 'Edificios', 'Mar', 'Bosque']
    IMAGE_SIZE = (150, 150)

    def loadRNN(model_file_name, weight_file_name):
        K.reset_uids()
        with open(model_file_name+'.json', 'r') as f:
            model = model_from_json(f.read())
        model.load_weights(weight_file_name+'.h5') 
        print("Red Neuronal Cargada desde Archivo") 
        return model

    def predictScene(self, path):
        print('MODEL')
        model_file_name = r'apiCNN/Logic/architecture'
        weight_file_name = r'apiCNN/Logic/weight'
        self.Selectedmodel = self.loadRNN(model_file_name, weight_file_name) 
        print(self.Selectedmodel)
        print(self.Selectedmodel.summary())

        img = Image.open(settings.BASE_DIR + path).convert('RGB')

        img = self.preprocesamiento(self, img=img)
        predic_index, maxElement, certainty, prediction_result = self.predict(self, img)
        dbReg = models.Image(image=path, label=prediction_result, probability=maxElement)
        dbReg.save()
        return (certainty, prediction_result)

    def predict(self, imgTrans):
        predic_index = self.Selectedmodel.predict(imgTrans)[0]
        print('Predictions: ', predic_index)
        maxElement = np.amax(predic_index)
        certainty = str(round(maxElement*100, 4))
        print('Certainty: ', certainty+'%')
        result = np.where(predic_index == np.amax(predic_index))
        print('Max: ', maxElement)
        print('List of maximum element indices: ', result[0][0])
        index_sample_label = result[0][0]
        prediction_result = self.CLASS_NAMES[index_sample_label]
        print(self.CLASS_NAMES)
        print('\nPrediction label: ', prediction_result)
        return (predic_index, maxElement, certainty, prediction_result)
        
    def preprocesamiento(self, img):
        arr = np.array(img)
        print('Imagen Shape:', arr.shape)
        arrTrans = arr.reshape(1, self.IMAGE_SIZE[0], self.IMAGE_SIZE[1], 3)
        arrTrans = arrTrans / 255
        return arrTrans
        
        
