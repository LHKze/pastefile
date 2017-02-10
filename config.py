# coding=utf-8
import os


DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
UPLOAD_FOLDER = '/tmp/permdir'
SQLALCHEMY_TRACK_MODIFICATIONS = False
