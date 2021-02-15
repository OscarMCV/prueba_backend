Prueba Backend 
======
Backend developer position challenge

We require to develop an API for e-learning courses to integrate in our system. The purpose
of this tool is for us, as professors to manage courses configuration and performance
reviews and, for our students, to take courses when using our frontend.
Our PM is a very busy person, so we don’t have detailed tasks but only the business rules to
work with. Here they are:
1. We have courses that contain lessons and lessons that contain questions
2. The courses are correlative with previous ones
3. The lessons are correlative with previous ones
4. The questions for each lesson have no correlation
5. All questions for a lesson are mandatory
6. Each question has a score
7. Each lesson has an approval score that has to be met by the sum of correctly
answered questions to approve it
8. A course is approved when all lessons are passed.
9. There’s no restriction on accessing approved courses
10. Only professors can create and manage courses, lessons and questions
11. Any student can take a course
12. Initially, we’ll need to support these types of questions:
	
	* Boolean
	* Multiple choice where only one answer is correct
	* Multiple choice where more than one answer is correct
	* Multiple choice where more than one answer is correct and all of them must
	be answered correctly

13. Frontend guys specifically asked for these endpoints for the students to use:
	* Get a list of all courses, telling which ones the student can access
	* Get lessons for a course, telling which ones the student can access
	* Get lesson details for answering its questions
	* Take a lesson (to avoid several requests, they asked to send all answers in
	one go)

Codebase rules:
1. The API must be developed using Python
2. There must be a readme file documenting installation and usage.
3. You can use any frameworks and libraries you want, but they must be included in the
readme file documenting its purpose and a brief explanation with the reasoning for
your choice.


## Requeriments 
* Python 3.6
* Django 2.2
* Django Rest Framework 3.9.2
## Instalation

1. Execute the following lines 
```bash 
#Before installation, make sure you have any python3 installed in your system
sudo add-apt-repository ppa:deadsnakes/ppa 
sudo apt-get update 
sudo apt-get install python3.6
sudo apt-get update
sudo apt-get install python3-pip 
python3 -m pip install virtualenv
```
2. Download the repositry:
```bash
https://github.com/OscarMCV/prueba_backend.git
```
3. Into the repository folder execute the follow lines:
```bash
python3 -m virtualenv env3.6 -p /usr/bin/python3.6
#This create the virtualenv of the project
```
4. Activate the virtualenv
```bash
source /env3.6/bin/activate 
#You have to be placed into the repository folder
python -m pip install -r requierements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
#This is the acount of the API manager, by default a super user hs ALL the permissions
python manage.py runserver 0.0.0.0:8000
#Now, the API is running!!

#This API doesn't need any third party aditional module!!!. 
```

## Using the API
1. This api uses token authentication. go to 
```bash
http://127.0.0.1:8000/users/login/
#Introduce your credential and get you token
```
The token authentication shoul be in the header of all the requests whit the follow format:
```bash 
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

#For more information about how to athenticate yourself: 
#https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
```
2. Now your super user is authenticated. You can use the admin site in order to manage the values of the system directly:
```bash
http://127.0.0.1:8000/admin
```
 