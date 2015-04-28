# this .py file is just like urls.py in django setup



import webapp2
from google.appengine.ext import ndb
from handlers import SplashPage
from handlers import LogoutPage




app = webapp2.WSGIApplication([
    ('/', SplashPage),
    ('/logout', LogoutPage)
], debug=True)
