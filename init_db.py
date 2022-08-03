from url_shortener import db
from url_shortener.models.url import ShortUrls

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()