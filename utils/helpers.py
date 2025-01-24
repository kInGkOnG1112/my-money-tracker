from flask import url_for


def get_global_context(context):
    """
    retrieves all the global variables includes
    navigation items for rendering and displaying them
    :param context: context in routes
    :return: merged context
    """
    page = context.get("page")
    filtered_navigations: list[dict] = [{**navigation, 'is_active': (page == navigation['id'])} for navigation in get_navigation_items()]
    global_context = {
        'g_navigations': filtered_navigations,
    }
    return {**context, **global_context}


def get_navigation_items():
    """
    initialize all the navigation items
    based on the number of pages
    :return: navigation list
    """
    navigation_items: list[dict] = [
        {
            "name": "Dashboard",
            "id": "dashboard",
            "url": url_for('main.dashboard'),
            "icon_class": "lni lni-dashboard",
            "is_active": False,
        },
        {
            "name": "Records",
            "id": "records",
            "url": url_for('main.records'),
            "icon_class": "lni lni-agenda",
            "is_active": False,
        },
        {
            "name": "Analysis",
            "id": "analysis",
            "url": url_for('main.analysis'),
            "icon_class": "lni lni-graph",
            "is_active": False,
        },
        {
            "name": "Accounts",
            "id": "accounts",
            "url": url_for('main.accounts'),
            "icon_class": "lni lni-wallet",
            "is_active": False,
        },
        {
            "name": "Categories",
            "id": "categories",
            "url": url_for('main.categories'),
            "icon_class": "lni lni-tag",
            "is_active": False,
        },
    ]
    return navigation_items


class GenericResponse:
    """
    This class is for handles the
    generic response of each request.

    Also, this serve as the base class for
    responses to avoid redundancy
    """

    @staticmethod
    def error(message=None, user_message='Unable to process at the moment!'):
        """
        This function returns for all error messages
        :param message:
        :param user_message:
        :return: json
        """
        return {
            'success': False,
            'error': message if message else user_message,
            'message': user_message
        }

    @staticmethod
    def success(message):
        """
        This function returns for all success responses
        :param message:
        :return:
        """
        return {
            'success': True,
            'message': message
        }


def get_pagination_details(page_number: int, page_size: int, queryset):
    """
    This function returns a pagination details for a queryset.
    :param page_number: page number (int)
    :param page_size: total page size (int)
    :param queryset: actual query object
    :return: queryset and pagination details
    """
    start: int = (page_size * page_number) - page_size
    end: int = page_size * page_number
    total: int = queryset.count()
    pages: int = max(1, -(-total // page_size))

    pagination_details = {
        'page': page_number,
        'perpage': page_size,
        'start': start,
        'end': end,
        'total_page': pages,
        'total': total,
        'pages': range(page_number, (1 + pages)),
    }
    return queryset[start:end], pagination_details
