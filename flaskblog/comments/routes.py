from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import User, Blog, Tag, Comment
from flaskblog.comments.forms import CommentForm
from flaskblog.utils import get_tags
from datetime import datetime

comments = Blueprint('comments', __name__)


@comments.route("/blog/<int:blog_id>/comment/new", methods=['POST', 'GET'])
@login_required
def new_comment(blog_id):
    form = CommentForm()
    if form.validate_on_submit():
        blog = Blog.query.get(int(blog_id))
        coments = Comment.query.filter_by(user_id=current_user.id).all()
        commented_today = []
        blog_ids = []
        for comment in coments:
            if datetime.utcnow().__str__()[:10] in comment.date_commented.__str__():
                commented_today.append(comment)
                blog_ids.append(comment.blog_id)

        if blog.bloggedBy == current_user:
            flash('You cannot comment on your own blog', 'danger')
        elif len(commented_today) >= 3:
            flash('You cannot comment more than three times per day', 'danger')
        elif blog_id in blog_ids:
            flash('You cannot comment on a particular blog more than once per day', 'danger')
        else:
            comment = Comment(comment=form.comment.data,
                              sentiment=form.sentiment.data,
                              blog=blog,
                              commentedBy=current_user)
            db.session.add(comment)
            db.session.commit()
            flash('Your comment has been created!', 'success')
        return render_template('blog.html', blog=blog, blog_id=blog_id, comments=blog.comment)

    return render_template('create_comment.html',
                           subject='New Comment',
                           form=form,
                           legend='New Comment',
                           blog_id=blog_id)


@comments.route("/blog/<int:blog_id>/comment/<int:comment_id>/edit", methods=['GET', 'POST'])
def edit_comment(blog_id, comment_id):
    blog = Blog.query.get_or_404(blog_id)
    comment = Comment.query.get_or_404(comment_id)
    if comment.commentedBy != current_user:
        abort(403)
    form = CommentForm()
    if form.validate_on_submit():
        comment.sentiment = form.sentiment.data
        comment.comment = form.comment.data
        db.session.commit()
        flash('Your comment has been edited!', 'success')
        return render_template('blog.html', blog=blog, blog_id=blog_id, comments=blog.comment)
        # return redirect(url_for('blogs.blog', blog_id=blog.blog_id))
    elif request.method == 'GET':
        form.sentiment.data = comment.sentiment
        form.comment.data = comment.comment
    return render_template('create_comment.html', title='Update Comment', form=form, legend='Update Comment')


@comments.route("/blog/<int:blog_id>/comment/<int:comment_id>/delete", methods=['POST', 'GET'])
@login_required
def delete_comment(blog_id, comment_id):
    comment = Comment.query.get_or_404(comment_id)
    blog = Blog.query.get(int(blog_id))
    if comment.commentedBy != current_user:
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash('Your comment has been deleted!', 'success')
    return render_template('blog.html', blog=blog, blog_id=blog_id, comments=blog.comment)
