from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Blog, Tag
from flaskblog.blogs.forms import BlogForm
from flaskblog.utils import get_tags
from datetime import datetime

blogs = Blueprint('blogs', __name__)


@blogs.route("/blog/new", methods=['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():

        blogs = Blog.query.filter_by(user_id=current_user.id).all()

        blogged_today = []
        for blog in blogs:
            if datetime.utcnow().__str__()[:10] in blog.date_blogged.__str__():
                blogged_today.append(blog)

        if len(blogged_today) > 1:
            flash('You can only create two blogs per day!', 'danger')
        else:
            tags = [Tag(tag=tag) for tag in form.tags.data.split()]
            new_blog = Blog(subject=form.subject.data, description=form.description.data, bloggedBy=current_user, tag=tags)
            db.session.add(new_blog)
            db.session.commit()
            flash('Your blog has been created!', 'success')

        return redirect(url_for('main.home'))
    return render_template('create_blog.html', subject='New Blog', form=form, legend='New Blog')


@blogs.route("/blog/<int:blog_id>", methods=['GET', 'POST'])
def blog(blog_id):
    current_blog = Blog.query.get_or_404(blog_id)
    tags = get_tags(current_blog.tag)
    return render_template('blog.html',
                           subject=current_blog.subject,
                           blog=current_blog,
                           tags=tags,
                           comments=current_blog.comment)


@blogs.route("/blog/<int:blog_id>/update", methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if blog.bloggedBy != current_user:
        abort(403)
    form = BlogForm()
    if form.validate_on_submit():
        blog.subject = form.subject.data
        blog.description = form.description.data
        blog.tag = [Tag(tag=tag) for tag in form.tags.data.split()]
        db.session.commit()
        flash('Your blog has been updated!', 'success')
        return redirect(url_for('blogs.blog', blog_id=blog.blog_id))
    elif request.method == 'GET':
        form.subject.data = blog.subject
        tags = get_tags(blog.tag)
        form.tags.data = tags
        form.description.data = blog.description
    return render_template('create_blog.html', title='Update Blog', form=form, legend='Update Blog')


@blogs.route("/blog/<int:blog_id>/delete", methods=['POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if blog.bloggedBy != current_user:
        abort(403)
    db.session.delete(blog)
    db.session.commit()
    flash('Your blog has been deleted!', 'success')
    return redirect(url_for('main.home'))
