from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app_main import routes, routes_ajax, models

# ^ Custom import of routes from each application
# above is necessary as this must be defined during initialization

admin = Admin(app, name='My Admin Panel', template_mode='bootstrap4')
admin.add_view(ModelView(models.Category, db.session))
admin.add_view(ModelView(models.Record, db.session))
admin.add_view(ModelView(models.Account, db.session))

# Create the database and tables within the app context
with app.app_context():
    try:
        db.create_all()
        print("Database and tables created successfully.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    app.run(debug=True)
