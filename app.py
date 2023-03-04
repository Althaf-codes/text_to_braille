from flask import  Flask, request
from imutils.perspective import four_point_transform as FPT
from collections import Counter
from main import getBrailleLetter

import matplotlib.pyplot as plt
from imutils import contours
from skimage import io
import numpy as np
import imutils
import cv2
import re

import warnings
app = Flask(__name__)

@app.route('/')
def home():
    return "hello from home"

@app.route('/getbraille',methods=['POST'])
def getval():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        # print("THE JSON RES IS "+json)
        val = getBrailleLetter(url=json['imageUrl'])
        return val
    else:
        return 'Content-Type not supported!'
     # "../assets/sujaytest4.jpeg

    # val = getBrailleLetter(url=url)
    # return val


if __name__=="__main__":
    app.run(debug=True)