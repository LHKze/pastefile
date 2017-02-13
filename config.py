# coding=utf-8
import os

UPLOAD_FOLDER = '/tmp/permdir'







class HerokuConfig:
	

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