# user_profiles/models.py

from django.db import models

# Connect all users to schools
class School(models.Model):
	# go through and adjust field lengths later (zip&phone don't need 200)
	street_address = CharField(max_length=200)
	city = CharField(max_length=200)
	state = CharField(max_length=200)
	zip_code = CharField(max_length=200)
	phone = CharField(max_length=200)
	website = URLField()
	# also?  admin_faculty

class Teacher_Talk_User(models.Model):
	django_user = models.ForeignKey(User, on_delete=models.CASCADE)
	school = models.ForeignKey(school, on_delete=models.SET_NULL, null=True)
	
class Student(Teacher_Talk_User):
	date_of_birth = DateField() # need to check age
	year_graduation = DateField(null=True) # ask directly or derive from grade level?
	
class Faculty(Teacher_Talk_User):
	# specific to faculty
	# use a boolean for "admin"?