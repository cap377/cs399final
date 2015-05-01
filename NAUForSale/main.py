# this .py file is just like urls.py in django setup



import webapp2
from google.appengine.ext import ndb
from handlers import SplashPage
from handlers import LogoutPage
from handlers import MyPostsPage
from handlers import CreateFormPage
from handlers import PostAjaxPage




app = webapp2.WSGIApplication([
    ('/', SplashPage),
    ('/logout', LogoutPage),
    ('/myPosts', MyPostsPage),
    ('/form', CreateFormPage),
    ('/postajax', PostAjaxPage)

], debug=True)
