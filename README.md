Dummy Task: Multi DB Router

Requirements:
1) Databases: PostgreSQL DB and My SQL DB.
2) Django 1.10 with Python.
3) Multi setting for local and production environments.
4) Proper Readme file with setup instruction.


Description: 
- Project has 2 roles Admin and User
- PostgreSQL has 2 database: database1, database2
- My SQL has 3 database: database3, database4, database5

You need to create a django application where admin can add users and assign multiple database (database1, database2, database3, database4, database5 ) to a user and when user is created, he should get Email for login and password(or any other way to handle this flow).
When user performs login, he can see the database list, which admin assigned to him.

Then user can create Product by selecting database from the List. Product should be save under selected database.
There should be one page where user can see all product list with database name.

Admin has one page, where he can see all user's and their product details.
(CRUD operation should follow by default.)

Any complicated UI is not needed, just a well documented code for Python following PEP8 standards is needed.



Implementation: 

I. Admin: Admin need to configure directly in the database. No UI is provided for Admin registration.

UserLogin:  Need to enter  
