from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import numpy as np
from .apps import EmoclConfig
from PIL import Image
import io
import json
# from skimage.transform import resize

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def classify(request):
    if request.method == 'POST':
        image_bytes = request.FILES['image'].read()
        image_stream = io.BytesIO(image_bytes)
        image = Image.open(image_stream)
        image = np.asarray(image, dtype=np.double)
        image /= 255
        #n = min(image.shape[0], image.shape[1])
        #image = image[:n, :n]
        #img_size = 48
        #image = resize(image, (img_size, img_size)).reshape(1, img_size, img_size)
        res = EmoclConfig.model.predict(image)
        print(res)
        return HttpResponse(json.dumps(res.tolist()), content_type="application/json")
    else:
        return HttpResponse("Only supports POST requests")
