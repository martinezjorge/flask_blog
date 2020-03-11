# Overview

99% of this code came from Corey Shafer's Flask Course on YouTube.

You can find it here in the following link:
    
    https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

******************************************************************************************************

#### Installation

This is going a blog with a login page and other functionality that was created using Flask as the 
back end and with HTML and CSS in the Front End using Flask's Ninja Template Engine.

I developed this on Ubuntu 18.04 using Python 3.6. If you happen to have Ubuntu 18.04 that would
be great because it already comes with Python 3.6; otherwise, you'll have to install it in order to
run this project. I recommend a virtual environment.

> python -m venv create virtual

then to activate it run

> source virtual/bin/activate

There is a requirements.txt that you can use to set up a virtual environment by running

> pip install requirements.txt


Then there is still some setup to do so that you can the backend can do encryption and be able to
send emails to users in case they forgot their passwords and want to change them. The following
data is meant to be private but since this is just a school project I don't think there's really 
an issue.

If you're on Ubuntu 18.04 you have to export some variables to the environment.

Just copy and paste the following lines to your .bashrc file. 


> export EMAIL_USER="emailforflaskemails@gmail.com"
>
> export EMAIL_PASS="testing1!"
>
> export SECRET_KEY='08c35dc5534510722c45cbc8445411ae'
>
> export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'

I set up an email with no personal information that is just for sending automated responses.

The secret key is for hashing, and the database uri specifies the type of database that it
is. In this case its using a sqlite database.

Now with the environment variables set up. In a terminal run

> cd flask_blog

Now to run the web app type: 

> python run.py

And it will give you url from localhost where you can see the webapp.

******************************************************************************************************

##### Notes

If you want to see how the schema was set up you can see it at the following link:

    https://github.com/martinezjorge/flask_blog/blob/master/flaskblog/models.py
    
Inside of the User class, it meets all the requirements that you specified except that I made
the length of the password longer because the encrypted password is 60 characters long rather
than the 25 you specified.

This is actually  a blog web app so if you get it set up you can use it and create and delete posts.
I'm not sure what you wanted the rest of the project to be but with this as a starting base, I'm
sure I can pivot in whatever direction you were planning for the class. If it would have been a blog
then the next thing I would do is allow administrator accounts to be able to delete and edit
any posts as right now users are the only ones who can delete their posts.