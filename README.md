# MY TODO-S

MY TODO-S is a webapp that allows users to put down their task in a to-do format.

## Screenshots
![image](https://user-images.githubusercontent.com/29266211/194055214-d1148840-f7a7-48f3-9b95-aef367b72f76.png)

![image](https://user-images.githubusercontent.com/29266211/194055353-ff57e42e-f1bc-48af-940c-e5c336d6cd8b.png)

![image](https://user-images.githubusercontent.com/29266211/194055728-23c9f543-1928-4e9f-a9e2-3176ca6b0805.png)


## Features
1. User Registration, Login and Logout
2. Create, Update and Delete to-do items
3. Mark a completed task
4. Pagination

## Demo
  MY TODO-S link: https://mytodos-application.herokuapp.com/

## Technologies

1. Python
2. Django
3. HTML
4. CSS
5. Javascript


## How to setup locally
1. Clone repo
  ```bash
  git clone https://github.com/chukaibejih/todo_app.git
  ```
  
2. Create a new virtual environment for this project. *Virtualenv* and *anaconda* are popular choices. ***Please make sure to create a new environment for this project.***
  Recommended : 
  ```bash
  pip install pipenv
  ```
  ```bash
  cd <project directory>
  ```
  Install from Pipfile
  ```bash
  pipenv install
  ```
  Next, activate the Pipenv shell:
  ```bash
  pipenv shell
  ```
  This will spawn a new shell subprocess, which can be deactivated by using exit.
  
3.  Setup database migrations:

     ```bash
     python manage.py migrate
    ```
4. Start the server:

   ```bash
   python manage.py runserver
   ```
   
5. OPTIONAL: Create a super admin account

   ```bash
   python manage.py createsuperuser
   ```

   Visit `/admin/` and login with credentials to have access to the admin dashboard.
  
## Deploy
  This project was deployed to Heroku
