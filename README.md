# Codegram - Social media website for developers

1. In this website users/developers can post code just like posting photos on instagram, written in python/django (just not that good of UI though).
2. A user can also comment on another user or one's own post.
3. A user needs to be logged in to perform above actions.

## To get the website running after you've cloned it...

1. Create and activate a virtual environment in the repository through commandline using the command

if on mac/linux
`$ python3 -m venv venv`\
`$ source venv/bin/activate`

if on windows:
`python -m venv venv`\
`venv\Scripts\activate`

2. After activating virtual environment install the required packages for this project through requirements.txt file (in the root directory of the project, where **manage.py** lies):

`(venv) $ pip install -r requirements.txt`

3. After installing all packages and virtual environment still activated, type this 2 command to initialize your database(make sure to be in the root directory):

`(venv) $ python manage.py makemigrations`\
`(venv) $ python manage.py migrate`

4. After above steps are completed, you can run the website by typing the following command in the command line:

`(venv) $ python manage.py runserver`

5. Now simply navigate to **http://127.0.0.1:8000** or **http://localhost:8000** on your browser
