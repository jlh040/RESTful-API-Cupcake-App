"""Flask app for Cupcakes"""
from flask import Flask, render_template, redirect, flash, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

app.config['SECRET_KEY'] = '3nc7v9a1x'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

def create_cupcake_instance(flavor, size, rating, image):
    """Create a cupcake instance."""
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    return new_cupcake

@app.route('/api/cupcakes', methods = ['GET'])
def get_all_cupcakes():
    """Get all cupcakes from the db."""
    all_cakes = [cupcake.serialize_cupcake() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cakes)

@app.route('/api/cupcakes/<int:id>', methods=['GET'])
def get_single_cupcake(id):
    """Get a cupcake based off of its id."""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize_cupcake())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """Create a single cupcake."""
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image')

    new_cupcake = create_cupcake_instance(flavor, size, rating, image)
    return (jsonify(cupcake=new_cupcake.serialize_cupcake()), 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """Update a cupcake."""
    cupcake = Cupcake.query.get_or_404(id)
    if request.json.get('flavor'):
        cupcake.flavor = request.json['flavor']

    if request.json.get('rating'):
        cupcake.rating = request.json['rating']

    if request.json.get('size'):
        cupcake.size = request.json['size']
    
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize_cupcake())
    
@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Delete a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Cupcake deleted!")

@app.route('/')
def show_homepage():
    """Show the homepage for the cupcake site."""
    return render_template('home.html')
    