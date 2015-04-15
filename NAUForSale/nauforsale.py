#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

## This is an example of reading the html directly from this file
##SPLASH_HTML = """\
##<html>
##	<b> This is a test of the splash page taking in html </b>
##</html>
##"""



class SplashHandler(webapp2.RequestHandler):

    def get(self):
        # this response(SPLASH_HTML) will load the html directly
        #self.response.write(SPLASH_HTML)
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('test.html')
        self.response.write(template.render(template_values))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Login Page Here!')

app = webapp2.WSGIApplication([
    ('/', SplashHandler),
    ('/login', LoginHandler)
], debug=True)
