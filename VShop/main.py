import os
import sys
from flask import Flask, render_template, session
from dotenv import load_dotenv
load_dotenv()
import flask_login
from flask_login import current_user
from flask_principal import identity_loaded, RoleNeed, UserNeed, Principal
from flask_caching import Cache

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
print(CURR_DIR)
sys.path.append(CURR_DIR)

def page_not_found(e):
    return render_template('404.html'), 404

def permission_denied(e):
    return render_template("403.html"), 403

def unauthorized(e):
    return render_template("401.html"), 401


login_manager = flask_login.LoginManager()

def create_app(config_filename=''):
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, permission_denied)
    app.register_error_handler(401, unauthorized)
    app.secret_key = os.environ.get("SECRET_KEY", "missing_secret")
    app.cache = Cache(app,config={'CACHE_TYPE': 'SimpleCache'})
    login_manager.init_app(app)
    
    with app.app_context():
        from auth.auth import auth
        app.register_blueprint(auth)
        from roles.roles import roles
        app.register_blueprint(roles)
        from shop.shop import shop
        app.register_blueprint(shop)
        
        principals = Principal(app)
        
        @login_manager.user_loader
        def load_user(user_id):
            if user_id is None:
                return None
            print("login_manager loading user")
            from auth.models import User
            if session["_user_id"] == user_id and "user" in session.keys():
                print("loading user from session")
                
                import jsons
                return jsons.loads(session["user"], User)
            from sql.db import DB
            try:
                result = DB.selectOne("SELECT id, email, username FROM IS601_Users WHERE id = %s", user_id)
                if result.status:
                    return User(**result.row)
            except Exception as e:
                print(e)
            return None

        @identity_loaded.connect_via(app)
        def on_identity_loaded(sender, identity):
            
            identity.user = current_user
            
            if hasattr(current_user, 'id'):
                identity.provides.add(UserNeed(current_user.id))
                
            if hasattr(current_user, 'roles'):
                for role in current_user.roles:
                    identity.provides.add(RoleNeed(role.name))
                    
        @app.teardown_request 
        def after_request_cleanup(ctx):
            from sql.db import DB
            DB.close()
        return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))