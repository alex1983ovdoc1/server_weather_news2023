from flask import Blueprint, redirect, flash, render_template
from flask_login import current_user, login_required

from webapp.user.decorators import admin_required
from webapp.user.forms import LoginForm
from webapp.user.models import User
from webapp.utils import get_redirect_target

# from user.decorators import admin_required
# from user.forms import LoginForm
# from user.models import User
# from utils import get_redirect_target

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


# page for admin
# @app.route('/admin')
@blueprint.route('/')
# @login_required
@admin_required
def admin_index():
    if current_user.is_admin:
        flash('/ Hello admin! (admin/views)')
        # return "Hello admin! (admin/views)'" 
        # return redirect(get_redirect_target())

        # return redirect(url_for('user.login'))
        # title = 'Authorization'
        # login_form = LoginForm()
        # return render_template('user/login.html', page_title=title, form=login_form)

        title = 'This page is for Administrators only'
        name_user = User.query.filter(User.username.isnot(None)).all() 

        return render_template('admin/info.html', page_title=title, name_user=name_user)
    else:
        # return "You aren't admin."
        flash("/ You aren't admin.")
# # -------------



# from flask import Blueprint
# from flask_login import current_user
# from webapp.user.decorators import admin_required


# blueprint = Blueprint('admin', __name__, url_prefix='/admin')


# # page for admin
# @blueprint.route('/')
# @admin_required
# def admin_index():
#     if current_user.is_admin:
#         return "Hello admin!"
