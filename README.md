# Social-Network-DJBird

Social Network (Twitter Clone) based on Django1.8 - Python 2.7 

## Features

1. User can post short messages up to 250 characters.
2. User can Like, Dislike, Reply and Retweet.
3. User can Follow other users and get their updates.
4. #Hashtags and @mentions support.
5. Thread of related tweets (Replies, Retweets and Hashtags).
6. User can see up to 50 update on the timeline.
7. Active search that shows users and tweets contain the searching keword.
8. User can see recomendded users to follow on the timeline. 
9. Editable User-profile contains basic information and a profile picture.
10. Registration and login forms. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Create, activate a virtual environment, and cd into it:

```
virtualenv -p python2.7 djbird  
source djbird/bin/activate
cd djbird

```

### Installing

A step by step guide that tell you how to get the development environment running

* Clone the project
```
git clone https://github.com/SamehKhattab/Social-Network.git

```

* Install dependencies 
```
pip install -r requirements.txt

```

* modify the Database configurations in settings.py file

## Start the project

* Creating an admin user:

First we’ll need to create a user who can login to the admin site.

Run the following command:

```
python manage.py createsuperuser
``` 

* Start the development server:

The Django admin site is activated by default. Let’s start the development server and explore it.
```
python manage.py runserver
```

Open http://localhost:8000/ in your browser, where you should be invited to login.


