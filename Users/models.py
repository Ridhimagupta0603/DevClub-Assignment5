from django.db import models
from django.contrib.auth.models import User


class Student(User):
    username=User.username
    password=User.password
    first_name=User.first_name
    def __str__(self):
        return self.username
    

class Instructor(User):
    
    def __str__(self):
        return self.username
   

