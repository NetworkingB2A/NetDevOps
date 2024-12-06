# Django Structure

You will start at a Overall project level. That will have settings that control all the apps and the overall project
## Project directory
in the project directory you will see the following, (at least if you created the Django project with the Django project commands.)
- Manage.py
  - We shouldn't need to worry about adjusting manage.py at least for this basic training. This will give us access to built-in Django commands.
- project setting directory
  - init.py
    - We currently don't need to use the init file for this project.
  - Asgi and wsgi
    - the asgi file is and the wsgi file are used for deployment for the web server.
  - Settings
    - Settings file contains the a bunch of global settings for this project. the default settings are good at first.
  - URL
    - URLs used when we start adding more and more pages to our web app. we will have to register all of these pages.
## Application Directories
- Migration directory
- Templates Directory
  - Application_name Directory
    - Note: This is standard for Django to have a template/app_name directory structure.
    - HTML or Jinja file
- Init.py
- admin.py
- apps.py
- models.py
  - This is for data models and used for the databases.
- tests.py
- views.py
  - write some logic to determine what we want to so to the users.