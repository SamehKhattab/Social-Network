# Social-Network-DJBird

Social Network (Twitter Clone) based on Django1.8 - Python 2.7 

## Features

1. Users can post short messages up to 250 characters.
2. Users can Like, Dislike, Reply, and Retweet.
3. User can Follow other users and get their updates.
4. #Hashtags and @mentions support.
5. Thread of related tweets (Replies, Retweets, and Hashtags).
6. Users can see up to 50 updates on the timeline.
7. Active search that shows users and tweets contain the searching keyword.
8. Users can see recommended users to follow on the timeline. 
9. Editable User-profile contains basic information and a profile picture.
10. Registration and login forms.  

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Create, activate a virtual environment, and cd into it

```
virtualenv -p python2.7 djbird  
source djbird/bin/activate
cd djbird
```

### Installing


* Clone the project
```
git clone https://github.com/SamehKhattab/Social-Network.git
```

* Install dependencies
```
pip install -r requirements.txt
```
### Start the project

* Start the development server

```
python manage.py runserver
```

Open http://localhost:8000/ in your browser, where you should be invited to Sign in or Sign up.


