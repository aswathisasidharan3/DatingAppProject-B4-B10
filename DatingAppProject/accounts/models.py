from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator





class Location(models.Model):
    id=models.AutoField(primary_key=True)
    CITY_CHOICES = (('KNR','Kannur'),('KH','Kochi'))
    city = models.CharField(max_length=3,choices=CITY_CHOICES)
    def __str__(self):
        return self.city

class Interest(models.Model):
    id=models.AutoField(primary_key=True)
    INTEREST_CHOICES = (('NR','Nature'),('TL','Travel'),('WR','Writing'),('AT','ART'),('PL','People'),('GF','Gym&Fitness'),('MC','Music'))
    interest = models.CharField(max_length=2,choices=INTEREST_CHOICES)
    def __str__(self):
        return self.interest    
    
class Hobbies(models.Model):
    id=models.AutoField(primary_key=True)
    HOBBY_CHOICES = (('CK','Cooking'),('TLG','Traveling'),('RD','Reading'),('DC','Dancing'),('GM','Gaming'))
    hobby = models.CharField(max_length=3,choices=HOBBY_CHOICES)
    def __str__(self):
        return self.hobby
		
		
class Habbit(models.Model):
    id=models.AutoField(primary_key=True)
    HABBIT_CHOICES = (('R','Regularly'),('O','Occasionally'),('Q','Quitting'),('N','Never'))
    habit=models.CharField(choices=HABBIT_CHOICES,max_length=1)	
    def __str__(self):
        return self.habit	

class Qualification(models.Model):
    id=models.AutoField(primary_key=True)
    QUALIFICATION_CHOICES = (('G','Graduation'),('PG','Post Graduation'),('D','Diploma'))    
    qualification=models.CharField(choices=QUALIFICATION_CHOICES,max_length=3)
class User(AbstractUser):
    GENDER_CHOICES=(('F','Female'),('M','Male'),('O','Others'))
    EXPERTISELEVEL_CHOICES=(('B','Beginner'),('I','Intermediate'),('E','Expert'))
    JOB_CHOICES = (('ER','Employer'),('EE','Employee'),('JS','Jobseeker'))
    
    age=models.SmallIntegerField(null=True,blank=True,
                                validators=[MinValueValidator(18),MaxValueValidator(34)])
    dob=models.DateField(null=True)
    phone=models.CharField(max_length=10,blank=True)
    dob=models.DateField(null=True,unique=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)	
    location=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True,blank=True,related_name="user_location")
    
    
    smoking_habits = models.ForeignKey(Habbit,on_delete=models.SET_NULL,null=True,related_name="user_smoking_habit")
    drinking_habits = models.ForeignKey(Habbit,on_delete=models.SET_NULL,null=True,related_name="user_drinking_habit")
    interest = models.ForeignKey(Interest,on_delete=models.SET_NULL,null=True,related_name="user_interest")
    hobbies = models.ForeignKey(Hobbies,on_delete=models.SET_NULL,null=True,related_name="user_hobbies")
    qualification=models.ForeignKey(Qualification,on_delete=models.SET_NULL,null=True,related_name="user_qualification")
    
    
    job_status = models.CharField(choices=JOB_CHOICES,max_length=2,null=True)
    company_name=models.CharField(null=True,max_length=100)
    designation=models.CharField(null=True,max_length=100)
    work_location=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True,blank=True,related_name="user_work_location")
    
    jobtitle=models.CharField(null=True,max_length=100)
    expertise_level=models.CharField(choices=EXPERTISELEVEL_CHOICES,max_length=1,null=True,blank=True)

    profile_pic=models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    short_reel=models.FileField(upload_to='short_reel/',null=True,blank=True)
    
    
    @property
    def is_employer(self):
        return self.company_name is None and self.designation is None
    
    @property
    def is_jobseeker(self):
        return self.jobtitle is None and self.expertise_level is None
    
