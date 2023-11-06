import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing import image
import numpy as np

model=  keras.models.load_model("static/PredictModel/model.h5")
model.load_weights("static/PredictModel/model_weight.h5")
def prediksi(path):
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)

  images = np.vstack([x])
  classes = model.predict(images, batch_size=10 )
  
  if classes[0][0]==1:
    x = 'Tangan Ini Diprediksi Sebagai Bentuk KERTAS'
    return x
  elif classes[0][1]==1:
    x = 'Tangan Ini Diprediksi Sebagai Bentuk BATU'
    return x
  elif classes[0][2]==1:
    x = 'Tangan Ini Diprediksi Sebagai Bentuk GUNTING'
    return x
  else:
    x = 'Tidak Diketahui'
    return x