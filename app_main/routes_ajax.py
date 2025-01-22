"""
importing all the libraries and modules dependencies
"""
from urllib import request
from flask import request, jsonify
from app import app, db
from app_main.models import Category
from utils.helpers import GenericResponse


@app.route('/ajax/add-category', methods=['POST'])
def add_category():
    """
    Adds a new category entry to the database
    :return: json response with message and status
    """
    try:
        if request.method == 'POST':
            data = request.form
            new_category = Category(
                type=data.get('type'),
                category_name=data.get('name'),
                icon=data.get('icon')
            )
            db.session.add(new_category)
            db.session.commit()

        return jsonify(
            GenericResponse.success(
                "Category was successfully added."
            )
        )
    except Exception as e:
        return jsonify(GenericResponse.error(str(e)))