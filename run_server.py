import os

from src.app import app
from src.auth import auth_bp
from src.views import blueprint

app.register_blueprint(auth_bp)
app.register_blueprint(blueprint)
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='localhost', port=port)
