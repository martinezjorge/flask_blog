"""

    Some utility functions for working with Tags

    Maybe more will be added as deemed necessary

"""


def get_tags(tags):
    t = [tag.tag for tag in tags]
    return " ".join(t)


def get_tags_and_blog_ids(tag_objects):
    tags = [tag.tag for tag in tag_objects]
    blog_ids = [tag.blog_id for tag in tag_objects]
    return tags, blog_ids
