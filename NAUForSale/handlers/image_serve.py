from google.appengine.ext import ndb
from handlers import BaseHandler

class ImgServe(BaseHandler):
	def get(self, resource):
	    post = ndb.Key('Post', int(resource)).get()
	    self.response.headers[b'Content-Type'] = "image/png"
	    self.response.write(post.picture)
