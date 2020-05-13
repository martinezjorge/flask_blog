from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Blog, Comment, Tag
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from flaskblog.users.utils import save_picture, send_reset_email
from flaskblog.utils import get_tags, get_tags_and_blog_ids

search = Blueprint('search', __name__)


@search.route('/search/', methods=['GET', 'POST'])
def search_by_tag():
    tag = request.args.get('tag', 1, type=str)
    print(f"This value of tag is: {tag}")
    # tags, blog_ids = get_tags_and_blog_ids(Tag.query.all())
    blog_ids = []
    for tag_object in Tag.query.all():
        if tag in tag_object.tag:
            blog_ids.append(tag_object.blog_id)
    print(f"These are the blog ids: {blog_ids}")
    blogs = []
    for blog_id in blog_ids:
        blogs += Blog.query.filter_by(blog_id=blog_id)
    print(f"This the list of blogs: {blogs}")
    return render_template('results.html', blogs=blogs)
