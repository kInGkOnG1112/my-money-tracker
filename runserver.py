from app import app

from app_main import routes
from app_expense_management import routes
from app_users import routes

# ^ Custom import of routes from each application
# above is necessary as this must be defined during initialization

if __name__ == '__main__':
    app.run(debug=True)
