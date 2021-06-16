# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:58:54 2021

@author: samuel
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))
posts = [
         {
             'name':'samuel faindani',
             'title': 'Mr'
        },
         {
             'name':'jerferson henry',
             'title': 'Mr'
        }
     ]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', posts= posts)


if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=False)
    app.run(host='localhost', debug=False)