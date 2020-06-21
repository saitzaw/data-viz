from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context(): 
        from app import urls 
        app.register_blueprint(urls.dashboard)

        return app 


