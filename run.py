from app_main import app, config

if __name__ == '__main__':
    app.run(
        host=config.get('config-settings', 'host'),
        port=config.get('config-settings', 'port'),
        debug=config.get('config-settings', 'debug')
    )

