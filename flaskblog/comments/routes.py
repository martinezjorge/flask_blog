from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Blog, Tag, Comment
from flaskblog.comments.forms import CommentForm
from flaskblog.utils import get_tags

comments = Blueprint('blogs', __name__)


@comments.route("/blog/<int:blog_id>/new")
@login_required
def new_comment(blog_id):
    form = CommentForm()
    if form.validate_on_submit():
        tags = [Tag(tag=tag) for tag in form.tags.data.split()]
        blog = Blog(subject=form.subject.data, description=form.description.data, writtenBy=current_user, tag=tags)
        db.session.add(blog)
        db.session.commit()
        flash('Your blog has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_blog.html', subject='New Blog', form=form, legend='New Blog')


def delete_comment():
    pass


def update_comment():
    pass
