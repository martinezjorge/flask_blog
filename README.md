99% of this code came from Corey Shafer's Flask Course on YouTube.

You can find it here in the following link:
    
    https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH


This is going to be a basic login page using Flask as the back end and some HTML and CSS 
in the Front End using Flask's Ninja Template Engine.

I developed this on Ubuntu 18.04 using Python 3.6. If you happen to have Ubuntu 18.04 that would
be great because it already comes with Python 3.6; otherwise, you'll have to install it in order to
run this project.

There is a requirements.txt that you can use to set up a virtual environment by running

> python -m venv create virtual

then to activate it run

> source virtual/bin/activate

then you can install the dependencies

> pip install requirements.txt


Then there is still some setup to do so that you can the backend can do encryption and be able to
send emails to users in case they forgot their passwords and want to change them. The following
data is meant to be private but since this is just a school project I don't think there's really 
an issue.

If you're on Ubuntu 18.04 you have to export some variables to the environment.

Just copy and paste the following lines to your .bashrc file. 

I set up an email with no personal information that is just for sending automated responses.

> export EMAIL_USER="emailforflaskemails@gmail.com"
>
> export EMAIL_PASS="testing1!"
>
> export SECRET_KEY='08c35dc5534510722c45cbc8445411ae'
>
> export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'

