import os

from app import app
from auth import auth_bp
from views import blueprint

app.register_blueprint(auth_bp)
app.register_blueprint(blueprint)
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
