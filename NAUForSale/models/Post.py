from google.appengine.ext import ndb

class Post(ndb.Model):
    title = ndb.StringProperty(required=True)
    author = ndb.UserProperty(requred=True)
    post_date = ndb.DateProperty(auto_now=True)
    description = ndb.TextProperty(required=True)
    price = ndb.StringProperty(required=True)
    picture = ndb.BlobProperty()
    contact_email = ndb.Email(required=True)
    contact_phone = ndb.PhoneNumberProperty()
    category = ndb.StringProperty(choices=('Home, Garden & Tools', 'Beauty', 'Electronics & Computers', 'Clothing, Shoes & Jewelry',
                                           'Books', 'Movies, Music & Games', 'Sports & Outdoors', 'Automotive', 'Pets', 'Free'), required=True)
