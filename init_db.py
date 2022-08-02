from url_shortener import db
from url_shortener.models.url import ShortUrls

db.drop_all()

db.create_all()