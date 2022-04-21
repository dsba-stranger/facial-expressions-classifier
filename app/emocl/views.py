from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import numpy as np
from .apps import EmoclConfig
from PIL import Image
import io



def index(request):
    return render(request, 'index.html')


@csrf_exempt
def classify(request):
    if request.method == 'POST':
        image_bytes = request.FILES['image'].read()
        image_stream = io.BytesIO(image_bytes)
        image = Image.open(image_stream)
        image = np.asarray(image, dtype=np.double).reshape((1, 48 * 48))
        image /= np.linalg.norm(image)
        res = EmoclConfig.clf.predict(EmoclConfig.pca.transform(image))
        return HttpResponse(res)
    else:
        return HttpResponse("Only supports POST requests")
