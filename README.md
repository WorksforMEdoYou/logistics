Logistics management

How to setup?
Install the libuary’s 
1.	Open the terminal or cmd
2.	Pip install virtualenv
3.	Create the virtual env using  python -m venv <name_of_your_venv>
4.	Clone my repo and here you need to install some linuary
Pip install Django Djangorestframework  django-cors-headers djangorestframework-simplejwt mysqlclient Django
5.	Now go the settings.py and configure the databases
6.	Then run the command in the terminal or cmd then run the command 
•	Python manage.py makemigrations
•	Python manage.py migrate
•	After successful of these two commands then run the command
•	Python manage.py runserver
APIS
Customer APIs(MySQL)
method              endpoint                 description                 authentication
GET             /customers/                list all customers                Yes
POST            /customers/                create a new customer             Yes
GET             /custoemrs/{id}/       Retrieve a specific customer          Yes
PUT             /customers/{id}/       update a specific custoemr            Yes
DELETE          /custoemrs/{id}/       delete a specific customer            Yes

Shipper Apis (MySQL)
method              endpoint                 description                 authentication
GET             /shippers/                list all shippers                  Yes
POST            /shippers/                create a new shipper               Yes
GET             /shippers/{id}/       Retrieve a specific shippers           Yes
PUT             /shippers/{id}/       update a specific shippers             Yes
DELETE          /shippers/{id}/       delete a specific shippers             Yes

Condignment APIS (MongoDB)
method              endpoint                 description                 authentication
GET             /condignment/                list all condignment            Yes
POST            /condignment/                create a new condignment        Yes
GET             /condignment/{id}/       Retrieve a specific condignment     Yes
PUT             /condignment/{id}/       update a specific condignment       Yes
DELETE          /condignment/{id}/       delete a specific condignment       Yes

Authentications APIs
method              endpoint                 description                 authentication
GET             /api/token/         generate access and refresh token        Yes
POST            /api/token/refresh  Refresh access token using refresh       Yes
