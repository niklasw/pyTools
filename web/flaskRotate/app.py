import os,glob
from os.path import join as pjoin
from flask import Flask,url_for
from jinja2 import Template

# This is from template.py in this folder
from template import template

app = Flask(__name__)

# Create the actual html that is sent to the client (browser)
# It just replaces three keywords in the string defined in template.py
def mkImgPage(imgPaths):
    t = Template(template)
    page = t.render(image     = imgPaths[1], \
                    nextImage = imgPaths[2], \
                    prevImage = imgPaths[0])
    return page

# Grab all .jpg images in the static/images/ folder
def getImageList(imgPath):
    return [os.path.basename(i) for i in glob.glob(pjoin('static','images','*.jpg'))]

def rotate(L, n):
    return L[n:] + L[:n]


# All these app.route decorators are Flask stuff.
@app.route('/')
def showPage():
    global imageNames

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    imgPaths = [pjoin('images',imageNames[i]) for i in (0,1,2)]

    return mkImgPage([ url_for('static',filename=imgPaths[0]),
                       url_for('static',filename=imgPaths[1]),
                       url_for('static',filename=imgPaths[2])])

@app.route('/backward/',methods=['POST'])
def bwdPage():
    global imageNames
    imageNames = rotate(imageNames,1)
    return showPage()

@app.route('/forward/',methods=['POST'])
def fwdPage():
    global imageNames
    imageNames = rotate(imageNames,-1)
    return showPage()

if __name__ == '__main__':
    imageNames = getImageList(pjoin('static','images'))

    app.run(host="127.0.0.1", port=5000, debug=True)

