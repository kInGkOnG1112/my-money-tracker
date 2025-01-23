from flask import url_for


def get_global_context(context):
    """
    retrieves all the global variables includes
    navigation items for rendering and displaying them
    :param context: context in routes
    :return: merged context
    """
    navigations = get_navigation_items()
    page = context.get("page")
    filtered_navigations = [{**navigation, 'is_active': (page == navigation['id'])} for navigation in navigations]
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
    navigation_items = [
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

    Also this serve as the base class for
    responses to avoid redundancy
    """

    @staticmethod
    def error(message, user_message='Unable to process at the moment!'):
        """
        This function returns for all error messages
        :param message:
        :param user_message:
        :return: json
        """
        return {
            'success': False,
            'error': message,
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