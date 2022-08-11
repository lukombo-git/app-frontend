from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from routes import blueprint
from routes import UPLOAD_FOLDER


app=Flask(__name__,static_folder='static')

app.config['SECRET_KEY'] = "_K3bDUnCzOQgH05mqCoC7A"
app.config['WTF_CSRF_SECRET_KEY'] = "6QjdVQs4slE3FRYX6rza_w"

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(blueprint)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_message = 'Please login.'
login_manager.login_view = 'frontend.login'

bootstrap = Bootstrap(app)

@login_manager.user_loader
def load_user(user_id):
    return None

if __name__ == '__main__':
    app.run(debug = True, port=5000)