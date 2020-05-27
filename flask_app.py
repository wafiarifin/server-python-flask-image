# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, Response, render_template
import jsonpickle
import numpy as np
import cv2
# import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    # data = random.choice(10,50,2)
    # return render_template('home.html', data=data)
    return render_template('home.html')

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    cv2.imwrite('mysite/static/test.jpg', img)

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")



