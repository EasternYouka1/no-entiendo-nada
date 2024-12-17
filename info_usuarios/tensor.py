import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Datos de entrenamiento
X_train = np.array([[25, 70, 3], [30, 80, 1], [22, 60, 2]])  
y_train = np.array([[2000], [2200], [1800]])  

# Definir el modelo
modelo = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(3,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)  
])

# Compilar el modelo
modelo.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar el modelo
modelo.fit(X_train, y_train, epochs=350)

# Guardar el modelo
modelo.save('modelo_calorias.h5')