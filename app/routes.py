from flask import render_template, request, redirect, url_for
from app import app

clothing_items = []

@app.route('/')
def index():
    return render_template('index.html', clothing_items=clothing_items)

@app.route('/add', methods=['POST'])
def add_clothing_item():
    item_name = request.form['name']
    item_color = request.form['color']
    item_image = request.form['image']
    item_category = mock_image_processing(item_name) 
    clothing_items.append({
        'name': item_name,
        'color': item_color,
        'image': item_image,
        'category': item_category
    })
    return redirect(url_for('index'))

def mock_image_processing(item_name):
    if "shirt" in item_name.lower():
        return "Shirt"
    elif "pants" in item_name.lower():
        return "Pants"
    else:
        return "Unknown"
