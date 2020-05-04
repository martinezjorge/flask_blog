from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    # User can create many blogs
    blogs = db.relationship('Blog', backref='writtenBy', lazy=True)
    # User can create many comments
    comments = db.relationship('Comment', backref='writtenBy', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Blog(db.Model):
    blog_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_blogged = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Blog can have many comments
    comment_id = db.relationship('Comment', backref='blog', lazy=True)
    # Blog can have many tags
    tag = db.relationship('Tag', backref='blog', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_blogged}')"


class Comment(db.Model):
    # Columns
    comment_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.Integer, nullable=False, default=0)
    date_commented = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # One to Many relationship from user to comment
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.blog_id'), nullable=False)

    def __repr__(self):
        return f"Comment('{self.user_id}','{self.blog_id}','{self.comment_id}','{self.sentiment}')"


class Tag(db.Model):
    # Columns
    tag_id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(40), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.blog_id'))

    def __repr__(self):
        return f"Tag('{self.tag}','{self.blog_id}')"


# Many to Many relationship
follows = db.Table('follows',
                   db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                   db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
                   )
