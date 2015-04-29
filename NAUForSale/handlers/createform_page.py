import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from handlers import BaseHandler
from google.appengine.api import users
from models import Post


class CreateFormPage(BaseHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.render("form.html", {'user': user.nickname()})
		else:
			self.redirect(users.create_login_url(self.request.url))
	def post(self):
		post = Post()
		#if users.get_current_user():
		#	post.author = Post(author = users.get_current_user())
		user = users.get_current_user()
		post.author = user
		post.contact_phone = self.request.get('contact')
		post.contact_email = self.request.get('email')
		post.title = self.request.get('title')
		post.description = self.request.get('description')
		post.price = self.request.get('price')
		post.category = self.request.get('category')
		post.picture = self.request.get('picture')
		post.put()
		self.redirect("/")
