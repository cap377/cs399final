from google.appengine.ext import ndb

class Post(ndb.Model):
    title = ndb.StringProperty(required=True)
    author = ndb.UserProperty(required=True)
    post_date = ndb.DateTimeProperty(auto_now=True)
    description = ndb.TextProperty(required=True)
    price = ndb.StringProperty(required=True)
    picture = ndb.BlobProperty(default="")
    contact_email = ndb.StringProperty(required=True)
    contact_phone = ndb.StringProperty(default="")
    category = ndb.StringProperty(choices=('Home, Garden & Tools', 'Beauty', 'Electronics & Computers', 'Clothing, Shoes & Jewelry',
                                           'Books', 'Movies, Music & Games', 'Sports & Outdoors', 'Automotive', 'Pets', 'Free'), required=True)
