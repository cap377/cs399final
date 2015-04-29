import webapp2
from google.appengine.ext import ndb
from handlers import BaseHandler
from google.appengine.api import users
from models import Post


class SplashPage(BaseHandler):
	def get(self):

		user = users.get_current_user()
		q = Post.query().fetch(100)
		if user:
			self.render("splash.html", {
				"title": "Nau For Sale",
				"items": "Electronics, Furniture, Clothes",
				"posts": q
				})
		else:
			self.redirect(users.create_login_url(self.request.url))