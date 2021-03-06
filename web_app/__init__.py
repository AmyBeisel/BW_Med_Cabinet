# __init__.py



# Imports

from flask import Flask
from web_app.routes.Directory import Directory
from web_app.routes.GET_PUT_API import GET_PUT_API


# Create Flask app

def create_app():
    
    app = Flask(__name__)

    app.register_blueprint(Directory)
    app.register_blueprint(GET_PUT_API)
    
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
