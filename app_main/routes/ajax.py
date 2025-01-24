"""
importing all the libraries and modules dependencies
"""
from urllib import request
from flask import request, jsonify, Blueprint, render_template
from extensions import db
from ..models import Category
from utils.helpers import GenericResponse, get_pagination_details
from sqlalchemy import and_

ajax = Blueprint('ajax', __name__)


@ajax.route('/ajax/add-category', methods=['POST'])
def add_category():
    """
    Adds a new category entry to the database
    :return: json response with message and status
    """
    try:
        if request.method == 'POST':
            data = request.form

            if Category.query.filter(Category.category_name == data.get('name')).first():
                return jsonify(
                    GenericResponse.error(
                        user_message='Category name already exists!'
                    )
                )

            new_category = Category(
                type=data.get('type'),
                category_name=data.get('name'),
                icon=data.get('icon')
            )
            db.session.add(new_category)
            db.session.commit()

        return jsonify(
            GenericResponse.success(
                'Category has been successfully added.'
            )
        )
    except Exception as e:
        return jsonify(GenericResponse.error(str(e)))


@ajax.route('/ajax/edit-category', methods=['POST'])
def edit_category():
    """
    Adds a new category entry to the database
    :return: json response with message and status
    """
    try:
        if request.method == 'POST':
            data = request.form
            if Category.query.filter(and_(Category.category_name == data.get('_category_name'), Category.id == data.get('id'))).first():
                return jsonify(
                    GenericResponse.error(
                        user_message='Category name already exists!'
                    )
                )

            category = Category.query.get_or_404(data.get('_id'))
            category.category_name = data.get('_category_name')
            category.type = data.get('_type')
            category.icon = data.get('_icon')
            db.session.commit()

        return jsonify(
            GenericResponse.success(
                'Category has been successfully updated.'
            )
        )
    except Exception as e:
        return jsonify(GenericResponse.error(str(e)))


@ajax.route('/ajax/delete-category', methods=['POST'])
def delete_category():
    """
    Delete category data from the database
    :return: json response with message and status
    """
    try:
        if request.method == 'POST':
            data = request.form
            category = Category.query.get_or_404(data.get('id'))
            db.session.delete(category)
            db.session.commit()

        return jsonify(
            GenericResponse.success(
                'Category has been successfully deleted!'
            )
        )
    except Exception as e:
        return jsonify(GenericResponse.error(str(e)))


@ajax.route('/ajax/get-category/list')
def get_category_list():
    """
    Get a list of all categories
    :return: html response as a subpage content
    """
    data = request.args
    type = data.get('type')
    search = data.get('search')
    page = int(data.get('page', 1))
    perpage = int(data.get('perpage', 10))

    query = Category.query
    query = query.filter(Category.category_name.like(f'%{search}%')) if search else query
    query = query.filter(Category.type == type) if type else query
    queryset, pagination_details = get_pagination_details(page, perpage, query)

    context = {
        'payload_data': data.to_dict(flat=True),
        'queryset': queryset,
        'pagination': pagination_details
    }
    return render_template('subpages/category-list.html', context_data=context)
