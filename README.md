# Blog Website Based on Django Framework

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Introduction:
* It is a user blog posting website based on Django Framework.
* The version I used of Django in this project is ```5.0```.
* There are two models:
  * The first one is Home, in this the user writes our blog's title and about the blog.
  * The second one is See Blogs, in this the user sees all the posted blogs there.
  * If the user clicks on a single blog it goes to the single page of blog and reads briefly.
* The database I used is SQLite, the Django framework's default database.
* For frontend I used HTML & CSS only.
* The username and the passsword for admin panel is ```blog``` & ```blog```.

## Technology Used:
* HTML
* CSS
* Python
* Django Framework
* VSCode
* SQLite

## Installation

```
git clone https://github.com/dragonwolf1o1/Blog-Website-Django-Framework.git

cd Blog-Website-Django-Framework

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```

