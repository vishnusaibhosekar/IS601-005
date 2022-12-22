from flask import Blueprint, current_app, render_template, flash, redirect, session, url_for
from auth.forms import LoginForm, ProfileForm, RegisterForm
from roles.models import Role
from sql.db import DB

from flask_login import current_user, login_user, login_required, logout_user
from auth.models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

from flask_principal import Identity, AnonymousIdentity, \
    identity_changed

auth = Blueprint('auth', __name__, url_prefix='/',template_folder='templates')

def check_duplicate(e):

    import re
    r = re.match(".*IS601_Users.(\w+)", e.args[0].args[1])
    if r:
        flash(f"The chosen {r.group(1   )} is not available", "warning")
    else:
        flash("Unknown error occurred, please try again", "danger")
        print(e)

@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        username = form.username.data
        try:
            hash = bcrypt.generate_password_hash(password)
            result = DB.insertOne("INSERT INTO IS601_Users (email, username, password) VALUES (%s, %s, %s)", email, username, hash)
            if result.status:
                flash("Successfully registered","success")
        except Exception as e:
            check_duplicate(e)
    return render_template("register.html", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        is_valid = True
        email = form.email.data
        password = form.password.data
        if is_valid:
            try:
                result = DB.selectOne("SELECT id, email, username, password FROM IS601_Users where email= %(email)s or username=%(email)s", {"email":email})
                if result.status and result.row:
                    hash = result.row["password"]
                    if bcrypt.check_password_hash(hash, password):
                        del result.row["password"]
                        user = User(**result.row)
                        result = DB.selectAll("""
                        SELECT name FROM IS601_Roles r JOIN IS601_UserRoles ur on r.id = ur.role_id WHERE ur.user_id = %s AND r.is_active = 1 AND ur.is_active = 1
                        """, user.id)
                        if result.status and result.rows:
                            print("role rows", result.rows)
                            user.roles = [Role(**r) for r in result.rows]
                        print(f"Roles: {user.roles}")

                        success = login_user(user)
                        
                        if success:
                            session["user"] = user.toJson()
                            flash("Log in successful", "success")
                            return redirect(url_for("auth.landing_page"))
                        else:
                            flash("Error logging in", "danger")
                    else:
                        flash("Invalid password", "warning")
                else:
                    flash("Invalid user", "warning")

            except Exception as e:
                flash(str(e), "danger")
    return render_template("login.html", form=form)

@auth.route("/landing-page", methods=["GET"])
@login_required
def landing_page():
    return render_template("landing_page.html")

@auth.route("/logout", methods=["GET"])
def logout():
    logout_user()
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
        
    identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())
    flash("Successfully logged out", "success")
    return redirect(url_for("auth.login"))

@auth.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user_id = current_user.get_id()
    form = ProfileForm()
    if form.validate_on_submit():
        is_valid = True
        email = form.email.data
        username = form.username.data
        current_password = form.current_password.data
        password = form.password.data
        confirm = form.confirm.data
        
        if current_password and password and confirm:
            try:
                result = DB.selectOne("SELECT password FROM IS601_Users where id = %s", user_id)
                if result.status and result.row:
                    if bcrypt.check_password_hash(result.row["password"], current_password):
                        hash = bcrypt.generate_password_hash(password)
                        try:
                            result = DB.update("UPDATE IS601_Users SET password = %s WHERE id = %s", hash, user_id)
                            if result.status:
                                flash("Updated password", "success")
                        except Exception as ue:
                            flash(ue, "danger")
                    else:
                        flash("Invalid password","danger")
            except Exception as se:
                flash(se, "danger")
        
        if is_valid:
            try:
                result = DB.update("UPDATE IS601_Users SET email = %s, username = %s WHERE id = %s", email, username, user_id)
                if result.status:
                    flash("Saved profile", "success")
            except Exception as e:
                check_duplicate(e)
    try:
        result = DB.selectOne("SELECT id, email, username FROM IS601_Users where id = %s", user_id)
        if result.status and result.row:
            user = User(**result.row)
            print("loading user", user)
            form.username.data = user.username
            form.email.data = user.email
            current_user.email = user.email
            current_user.username = user.username
            session["user"] = current_user.toJson()
    except Exception as e:
        flash(e, "danger")
    return render_template("profile.html", form=form)
