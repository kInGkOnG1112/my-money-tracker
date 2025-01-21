from app import app, db

from app_main import routes, models

# ^ Custom import of routes from each application
# above is necessary as this must be defined during initialization


# Create the database and tables within the app context
with app.app_context():
    try:
        db.create_all()
        print("Database and tables created successfully.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    app.run(debug=True)
