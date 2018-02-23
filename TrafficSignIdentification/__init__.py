# coding:utf-8
from flask import Flask
app = Flask(__name__)
app.config["TEMPLATE_AUTO_RELOAD"]=True
import TrafficSignIdentification.views
