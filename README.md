# todo-photo-app

You can watch [demo](https://drive.google.com/file/d/15wyRaDFbbhSoIuxyxiwZxgd0MLHKbTaO/view?usp=share_link)

## Technologies I used while developing the project:


- Django
- Docker
- PostgreSQL
- Django Class Based Views
- Django Model Form
- Django Pagination
- Bootstrap


## You can:


- Create a new user.
- Create a new todo
  - Delay the time of the todo
  - Complete the todo
- Upload a new photo
  - Delete photos
  - Update photos


## Download the project (With Docker)

First, create a folder and run
```
git clone https://github.com/bedirhansahin/todo-photo-app.git
cd todo-photo-app
```
:warning: **Don't forget install Docker desktop and create an account**:

After, run the following commands from CMD:
```
$ sh run_project.sh
$ docker-compose up
```

and you can go to [http://127.0.0.1:8090/](http://127.0.0.1:8090/) on your own browser.

:point_up: **You can create a superuser with command (docker-compose run --rm app sh -c "python manage.py createsuperuser")
and visit [admin page](http://127.0.0.1:8090/admin)**
