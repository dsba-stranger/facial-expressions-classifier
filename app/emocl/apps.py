from django.apps import AppConfig
import os
import pickle


class EmoclConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emocl'

    # create path to models
    path = 'models.p'

    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    pca = data['pca']
    clf = data['clf']