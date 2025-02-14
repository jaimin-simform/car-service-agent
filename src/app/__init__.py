from flask import Flask
import os
from .config import config  # ✅ Import config settings

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.abspath("src/templates"),
        static_folder=os.path.abspath("src/static")
    )
    
    app.config.from_object(config)  # ✅ Load config settings

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
