import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from handlers import BaseHandler
from google.appengine.api import users
from models import Post

class PostAjaxPage(BaseHandler):
	def get(self):
		q = Post.query().order(-Post.post_date).fetch(100)
		self.render("postajax.html", {'posts': q})
	def post(self):
		q = Post.query().order(-Post.post_date).fetch(100)
		self.redner("postajax.html", {'posts': q})