import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from handlers import BaseHandler
from google.appengine.api import users
from models import Post


CATEGORIES = [
    'Home, Garden & Tools',
    'Books',
    'Clothing, Shoes & Jewelry',
    'Movies, Music & Games',
    'Sports & Outdoors',
    'Beauty',
    'Electronics & Computers',
    'Automotive',
    'Pets',
    'Free'
]

class CreateFormPage(BaseHandler):
	def get(self):
	    user = users.get_current_user()
	    if not user:
	        self.redirect(users.create_login_url(self.request.url))
	        return                 
	    data = {'user': user.nickname(), 'categories': CATEGORIES}
	    if self.request.get("key"):
	        # Updating post
	    	key = self.request.get("key")
	        post = ndb.Key("Post", int(key)).get()
	        if post:
	        	data['post'] = post
	    self.render("form.html", data)

	def post(self):
		if self.request.get("key"):
			key = self.request.get("key")
			post = ndb.Key("Post", int(key)).get()
		else:
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
		if self.request.get('picture') == '':
			self.response.out.write('No image')
		else:
			post.picture = self.request.get('picture')
		

		post.put()
		self.redirect("/")
