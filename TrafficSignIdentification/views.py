# coding:utf-8
# 导入
from flask import render_template, flash, request, \
    jsonify, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from TrafficSignIdentification import app
import json
import time
import os
import sys
from data import getImage

# Bootstrap 支持
bootstrap = Bootstrap(app)
moment = Moment(app)
# 用户时间本地化工作

@app.route('/', methods=[u'GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=[u'POST'])
def handler():
    print(request.form)
    img = getImage(**request.form)
    return jsonify({"address": url_for('static', filename="pictures/"+img)})