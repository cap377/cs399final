import webapp2
from google.appengine.ext import ndb
from handlers import BaseHandler
from google.appengine.api import users


class MyPostsPage(BaseHandler):
	def get(self):

		user = users.get_current_user()

		if user:
			self.render("myPosts.html", {})
		else:
			self.redirect(users.create_login_url(self.request.url))
