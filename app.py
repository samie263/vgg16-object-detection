# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:58:54 2021

@author: samuel
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', debug=True)