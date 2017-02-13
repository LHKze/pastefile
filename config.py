# coding=utf-8
import os









class HerokuConfig:
	DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	    'mysql+pymysql://root:root@localhost/test1'
    UPLOAD_FOLDER = '/tmp/permdir'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def init_app(cls, app):
        

        # handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)

		
config = {
    
    'heroku': HerokuConfig,

}