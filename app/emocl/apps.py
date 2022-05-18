from django.apps import AppConfig
import os
import tensorflow as tf


class EmoclConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emocl'

    # create path to models
    path = 'C:/Users/kirill-korolev/ami/facial-expressions-classifier/model/bin/model'

    # load models into separate variables
    # these will be accessible via this class

    model = tf.keras.models.load_model(path)