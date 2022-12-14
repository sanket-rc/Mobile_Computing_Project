#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:34:15 2022

@author: zamaan
"""
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

ALLOWED_FILE_TYPES = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_TYPES

@app.route('/test')
def test():
    return 'test'

@app.route('/uploadImage', methods=['POST'])
def upload_file():
    category = request.form['category']
    print(category)
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        categories = os.listdir(os.path.join(os.getcwd(),'images'))
        if category not in categories:
            os.mkdir(os.path.join(os.getcwd(),'images', category))

        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(),'images', category, filename))
        return 'upload successful'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001)
