from flask import Flask, render_template, request, Response
import os
import time
from helpers import todo
# from helpers import gen, get_all_images

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/description')
def description():
    return render_template('description.html')


@app.route('/schedule')
def schedule():
    return render_template('schedule.html')


@app.route('/workshops')
def workshops():
    return render_template('workshops.html')

@app.route('/map')
def map_page():
    return render_template('map.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
# @app.route('/gallery')
# def slideshow():
#     return Response(gen(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/')
# def index():
#     return "<html><head></head><body><h1>slideshow</h1><img src='/gallery' style='width: 90%; height: 90%;'/>" \
#            "</body></html>"

    
if __name__ == '__main__':
    app.run(debug=True)