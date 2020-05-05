from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import User, Blog, Tag, Comment
from flaskblog.comments.forms import CommentForm
from flaskblog.utils import get_tags

comments = Blueprint('comments', __name__)


@comments.route("/blog/<int:blog_id>/comment/new", methods=['POST', 'GET'])
@login_required
def new_comment(blog_id):
    form = CommentForm()
    if form.validate_on_submit():
        blog = Blog.query.get(int(blog_id))
        comment = Comment(comment=form.comment.data,
                          sentiment=form.sentiment.data,
                          blog=blog,
                          commentedBy=current_user)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been created!', 'success')
        print(blog.comment)
        # return redirect(url_for('blogs.blog'), blog=blog, blog_id=blog_id, comments=blog.comment)
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
