import webapp2
from google.appengine.ext import ndb
from handlers import BaseHandler
from google.appengine.api import users


class LoginPage(BaseHandler):
	def get(self):

		"""
		user = users.get_current_user()

		
		if user:
			self.redirect(users.create_logout_url(self.request.url))

		else:
			self.render("logout.html", {})
		"""

		self.render("login.html", {})