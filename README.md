This is a miniture and basic version of a Twitter-like app made with Django.

This app allows the user to go to the admin page, visit the splash page, login,
sign up for a new account, logout of the account, go to the home page, 
visit their own profile, delete posts, visit other user profiles, see posts
with specific hashtags, and like posts.

To navigate the site, you must first make an account by clicking 
"Create new account". There you can create an account and get logged in. From
there, you will first see the Splash page. There are links to the home page 
and your own profile page. It is also at this page that you can log out. 

The Home page is where users can interact with other posts by liking them.
Clicking "Like" once will like the post and increase the number of likes. 
Clicking it again will remove the like and decrement the like count. 

At the bottom of the Home page is where you can make new posts. Clicking on 
hashtags will lead to a page that only displays posts with that hashtag. 

Clicking on a user's name will take you to their profile page and will display
all the posts that they created. You can navigate back home by clicking "Home"
at the top or go to your own profile page by clicking the "Profile" button.

To run it, go to the root directory of the project and run python3 manage.py runserver
