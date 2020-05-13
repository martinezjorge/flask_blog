from flask import render_template, request, Blueprint
from flaskblog.models import User, Blog, Comment
from flaskblog.utils import get_tags, get_tags_and_blog_ids

main = Blueprint('main', __name__)


@main.route("/")
# @main.route("/home")
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


@main.route('/users_who_posted_at_least_two_blogs_with_different_tags')
def users_who_posted_at_least_two_blogs_with_different_tags():
    users = User.query.all()
    # print(users)

    users_with_two_or_more_blogs = []
    for user in users:
        if len(Blog.query.filter_by(user_id=user.id).all()) > 1:
            users_with_two_or_more_blogs.append(user)
    # print(users_with_two_or_more_blogs)

    # Now I need to check the tags and see if the any tags in one blog are in the other tags
    for user in users_with_two_or_more_blogs:
        # getting all the blogs for a user
        blogs = Blog.query.filter_by(user_id=user.id)

        # then getting all the tags strings from all the blogs from that user in a list
        all_tags = []
        for blog in blogs:
            all_tags.append(get_tags(blog.tag))

        verified_users_who_posted_at_least_two_blogs_with_different_tags = []
        found = False
        # going through all tags strings
        for i, tagstring in enumerate(all_tags):
            # splitting
            tags = tagstring.split()
            for tag in tags:
                for j, other_tagstrings in enumerate(all_tags):
                    if i == j:
                        continue
                    else:
                        if tag in other_tagstrings:
                            break
                        else:
                            verified_users_who_posted_at_least_two_blogs_with_different_tags.append(user)
                            found = True
                            break
                if found:
                    break
            if found:
                break

    return render_template('users.html', users=verified_users_who_posted_at_least_two_blogs_with_different_tags, blogs=[])


@main.route('/blogs_of_a_user_with_all_positive_comments')
def blogs_of_a_user_with_all_positive_comments():
    users = User.query.all()

    users_with_blogs = []
    for user in users:
        if len(Blog.query.filter_by(user_id=user.id).all()) > 0:
            users_with_blogs.append(user)

    print(users_with_blogs)

    positive_blogs = []
    for user in users_with_blogs:
        blogs = Blog.query.filter_by(user_id=user.id)

        for blog in blogs:
            if len(Comment.query.filter_by(blog_id=blog.blog_id).all()) < 1:
                break
            else:
                comments = Comment.query.filter_by(blog_id=blog.blog_id)
                all_positive = True

            for comment in comments:
                if comment.sentiment != 'Positive':
                    all_positive = False
                    break

            if all_positive:
                positive_blogs.append(blog)

    print(positive_blogs)

    return render_template('results.html', blogs=positive_blogs, users=[])


@main.route('/users_who_posted_the_most_blogs_on_feb_10th_2020')
def users_who_posted_the_most_blogs_on_feb_10th_2020():
    pass


@main.route('/users_followed_by_two_accounts_specified_by_user')
def users_followed_by_two_accounts_specified_by_user():
    pass


@main.route('/users_who_never_posted_a_blog')
def users_who_never_posted_a_blog():
    users = User.query.all()
    # print(users)

    users_with_no_blogs = []
    for user in users:
        if len(Blog.query.filter_by(user_id=user.id).all()) < 1:
            users_with_no_blogs.append(user)
    # print(users_with_two_or_more_blogs)

    return render_template('users.html', users=users_with_no_blogs, blogs=[])


@main.route('/users_who_never_posted_a_comment')
def users_who_never_posted_a_comment():
    pass


@main.route('/users_with_only_negative_comments')
def users_with_only_negative_comments():

    all_users = User.query.all()

    negative_users = []

    for user in all_users:
        # grab all user's comments
        user_comments = user.comments

        # check if any users don't have any comments
        if len(user_comments) == 0:
            break

        # check to see if there's one positive comment
        all_negative = True
        for comment in user_comments:
            if comment.sentiment == 'Positive':
                all_negative = False
                break
            else:
                continue

        # if there isn't a single positive comment then we add that user to results
        if all_negative:
            negative_users.append(user)

    return render_template('users.html', users=negative_users, blogs=[])


@main.route('/users_whose_blogs_have_no_negative_comments')
def users_whose_blogs_have_no_negative_comments():

    users = User.query.all()

    users_with_blogs = []
    for user in users:
        if len(Blog.query.filter_by(user_id=user.id).all()) > 0:
            users_with_blogs.append(user)

    print(users_with_blogs)

    users_with_no_negative_comments = []
    for user in users_with_blogs:
        blogs = Blog.query.filter_by(user_id=user.id)

        for blog in blogs:

            comments = Comment.query.filter_by(blog_id=blog.blog_id)
            all_positive = True

            for comment in comments:
                if comment.sentiment != 'Positive':
                    all_positive = False
                    break

            if all_positive:
                users_with_no_negative_comments.append(user)

    print(users_with_no_negative_comments)

    return render_template('users.html', users=users_with_no_negative_comments, blogs=[])


def user_pair_that_always_gave_positive_comments():
    pass
