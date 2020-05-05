from flask import render_template, request, Blueprint
from flaskblog.models import Blog
from flaskblog.utils import get_tags

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    blogs = Blog.query.order_by(Blog.date_blogged.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', blogs=blogs)


@main.route("/about")
def about():
    return render_template('about.html', title="About")


@main.route('/initialize_db')
def initialize_db():
    page = request.args.get('page', 1, type=int)
    blogs = Blog.query.order_by(Blog.date_blogged.desc()).paginate(page=page, per_page=5)
    from flaskblog.scripts.db_scripts import db_init
    db_init()
    return render_template('home.html', blogs=blogs)
