import sqlparse
import sqlite3
from flaskblog import db


def db_init():

    print("Hello Nurse!")

    # Connect to the database
    conn = sqlite3.connect('../site.db')
    c = conn.cursor()

    # open the file
    sql_file = open('blog.sql', 'r')

    # file is parsed with a special library for going through sql files
    raw_sql_file = sql_file.read()
    raw_sql_file = sqlparse.split(raw_sql_file)

    # this is the part that takes a loooong time
    # basically goes through all the sql, formats it, and strips off comments but it might unnecessary
    sql_statements = []
    for line in raw_sql_file:
        line = sqlparse.format(sql=line,
                               reindent=False,
                               keyword_case='upper',
                               strip_comments=True)
        sql_statements.append(line)

    # execute the statements
    for statement in sql_statements:
        if len(statement) == 1:
            pass
        elif 'USE' in statement:
            pass
        else:
            c.execute(statement)

    # commit the changes & close the db
    conn.commit()
    conn.close()


def users_with_at_least_two_blogs_with_different_tags():
    pass
