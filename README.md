# BracuRooms <br>
To start this app or project you have to do: <br>
1. (optional) create a virtualenvioronmet in pyhton by using <br> 
`virtualenv venv`
then activate the virtualenvironment <br>
for windows: <br>
`venv\Scripts\activate` <br>
for unix based systems(linux & macos): <br>
`source venv/bin/activate`<br>

**In case you do not virtualenv, use** <br>
`pip install virtualenv` <br>


2. Then install all the requirements: <br>
   `pip install -r requirements.txt`
   <br>

3. Then run the app:<br>
   `python manage.py runserver`
   
4. You can use sqlite3(no more configuration required)<br> But if you are using Mysql/Postgre/Oracle then you can follow this [link](https://docs.djangoproject.com/en/4.0/ref/settings/#databases)
5. The make migrations and migrate the migrations to the database: <br>
`python manage.py makemigrations` <br>
`python manage.py migrate`

6. Create a super ueser :<br>
   `python manage.py createsuperuser`

## Mysql Configuration 
First log in to your mysql database and then crate **BracuRooms** database then execute this lines of sql:
<br>
`CREATE USER 'group3'@'localhost' IDENTIFIED BY 'group3';`
<br>
`GRANT ALL PRIVILEGES ON BracuRooms.* TO 'group3'@'localhost' WITH GRANT OPTION;`
<br>
`FLUSH PRIVILEGES;`
