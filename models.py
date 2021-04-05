"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Make a relation for cupcakes."""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, nullable = False, default = 'https://tinyurl.com/demo-cupcake')

    def serialize_cupcake(self):
        """Turn cupcake instance into a JSONifiable dictionary."""

        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
