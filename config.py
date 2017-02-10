# coding=utf-8
import os
from logging import StreamHandler

DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:root@localhost/test1"
UPLOAD_FOLDER = '/tmp/permdir'
SQLALCHEMY_TRACK_MODIFICATIONS = False

file_handler = StreamHandler()
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)
