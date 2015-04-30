import webapp2
from google.appengine.ext import ndb
from handlers import BaseHandler
from models import Post
from google.appengine.api import users


class MyPostsPage(BaseHandler):
	def get(self):

		user = users.get_current_user()
		q = Post.query().fetch(100)

		if user:
			self.render("myPosts.html", {
                                "posts": q,
                                "user": user
                                })
		else:
			self.redirect(users.create_login_url(self.request.url))
