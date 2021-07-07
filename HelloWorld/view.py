from django.shortcuts import render
from PIL import Image
import pytesseract
import os
import numpy as np
from django.conf import settings
import cv2
import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


def runoob(request):
    return render(request, 'base.html')

@csrf_exempt 

def ocrDetect(request):
    result = {"code": None}
    if request.method == "POST":
        if request.FILES.get( "image", None) is not None:
            img = request.FILES.get("image");
            img_path = os.path.join(settings.IMG_UPLOAD, "sss.png")
            with open(img_path, 'wb+') as destination:
                for chunk in img.chunks():
                    destination.write(chunk)
            pytesseract.pytesseract.tesseract_cmd = r'tesseract\tesseract.exe'
            img = Image.open(img_path)
            code = pytesseract.image_to_string(img, lang= 'chi_sim')
            result.update({ "output": code})
            return JsonResponse(result)