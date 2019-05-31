import os,glob
from os.path import join as pjoin
from flask import Flask,url_for,request
from jinja2 import Template

# This is from template.py in this folder
from template import template

app = Flask(__name__)

# Create the actual html that is sent to the client (browser)
# It just replaces three keywords in the string defined in template.py
def mkImgPage(imgPaths):
    cssFile = url_for('static',filename=pjoin('css','styles.css'))
    t = Template(template)
    page = t.render(image     = imgPaths[1],
                    nextImage = imgPaths[2],
                    prevImage = imgPaths[0],
                    css = cssFile,
                    client_ip = request.remote_addr)
    return page

# Grab all .jpg images in the static/images/ folder
def getImageList(imgPath):
    return [os.path.basename(i) for i in glob.glob(pjoin('static','images','*.png'))]

def rotate(L, n):
    return L[n:] + L[:n]

def rotI(iMax,i,nSteps):
    out = i+nSteps
    if out > iMax:
        out -= iMax+1
    elif out < 0:
        out += iMax+1
    return out

def vRotI(iMax,ivec,nSteps):
    return [rotI(iMax,i,nSteps) for i in ivec]


# All these app.route decorators are Flask stuff.
@app.route('/')
def showPage(step=0):
    global imageNames
    global sessionDict
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    nImg0 = len(imageNames)
    sessionID = request.remote_addr
    i0 = 0

    if not sessionID in sessionDict:
        sessionDict[sessionID] = {"index0":i0}
    else:
        i0 = sessionDict[sessionID]["index0"]
        i0 = rotI(nImg0-1,i0,step)
        sessionDict[sessionID]["index0"] = i0
    indices = vRotI(nImg0-1,(i0,i0+1,i0+2),step)
    print(indices,i0)

    imgPaths = [pjoin('images',imageNames[i]) for i in indices]

    return mkImgPage([ url_for('static',filename=imgPaths[0]),
                       url_for('static',filename=imgPaths[1]),
                       url_for('static',filename=imgPaths[2])])

@app.route('/backward/',methods=['POST'])
def bwdPage():
    return showPage(step=1)

@app.route('/forward/',methods=['POST'])
def fwdPage():
    return showPage(step=-1)

if __name__ == '__main__':
    imageNames = getImageList(pjoin('static','images'))
    sessionDict = {}

    app.run(host="127.0.0.1", port=5000, debug=True)

