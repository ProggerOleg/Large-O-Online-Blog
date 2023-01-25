# Large-O-Online-Blog

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ProggerOleg/Large-O-Online-Blog.git
$ cd Large-O-Online-Blog
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
Once you have downloaded dependencies, go to the cloned repo directory and run the following command

```bash
(env)$ python3 manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
(env)$ python3 manage.py migrate
```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
(env)$ python3 manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```bash
(env)$ python3 manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000/ for the App.

Cheers and Happy Coding :)

