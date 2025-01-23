"""
importing all the libraries and modules dependencies
"""
from urllib import request
from flask import request, jsonify, Blueprint, render_template
from extensions import db
from ..models import Category
from utils.helpers import GenericResponse, get_pagination_details

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
            new_category = Category(
                type=data.get('type'),
                category_name=data.get('name'),
                icon=data.get('icon')
            )
            db.session.add(new_category)
            db.session.commit()

        return jsonify(
            GenericResponse.success(
                'Category was successfully added.'
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
