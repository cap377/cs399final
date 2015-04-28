import os
import webapp2
import jinja2



jinja_environment = jinja2.Environment(
	extensions=['jinja2.ext.autoescape'],
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__) + "/../templates"),
	autoescape=True)

from google.appengine.ext import ndb

class BaseHandler(webapp2.RequestHandler):

	def __init__(self, request=None, response=None):
		super(BaseHandler, self).__init__(request, response)

		# own code for every page here

	def render(self, template_name, template_values):
		template = jinja_environment.get_template(template_name)
		self.response.out.write(template.render(template_values))

