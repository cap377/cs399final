import webapp2
from google.appengine.ext import ndb
from handlers import BaseHandler
from models import Post
from google.appengine.api import users


class MyPostsPage(BaseHandler):
	def get(self):

		user = users.get_current_user()
		q = Post.query().order(-Post.post_date).fetch(100)
		counter = 0
                for post in q:
                        if post.author == user:
                                counter += 1

		if user:
			self.render("myPosts.html", {
                                "posts": q,
                                "user": user,
                                "counter": counter
                                })
		else:
			self.redirect(users.create_login_url(self.request.url))

	def post(self):
		key = self.request.get("key")
		post = ndb.Key("Post", int(key)).get()
		post.key.delete()
		self.redirect("/")
