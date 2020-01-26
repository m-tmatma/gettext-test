#!/bin/python3
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import os

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    def get(self):
        self.render('index.html')

BASE_DIR = os.path.dirname(__file__)

application = tornado.web.Application(
    [
        (r"/", BaseHandler),
    ],
    template_path=os.path.join(BASE_DIR, 'templates'),
    static_path=os.path.join(BASE_DIR, 'js'),
)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
