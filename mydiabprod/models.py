from django.db import models
import datetime
from django.db import models
from django.utils import timezone

class Mydiabusers(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100)
    EntryDate = models.DateTimeField('date published')
    def __str__(self):
        return self.UserName
    def sell(self):
        return self.UserName, self.Password

class Mydiabresults(models.Model):
    UserName = models.ForeignKey(Mydiabusers, on_delete=models.CASCADE)
    DateTime= models.CharField(max_length=100)
    HGB = models.IntegerField(default=0)
    TypeOf = models.CharField(max_length=50)
    DeployDate = models.DateTimeField('date published')
    def __str__(self):
        return self.TypeOf

class Mydiabwelcome(models.Model):
    WelcomeText = models.CharField(max_length=200)
    WelcomeOrigin = models.CharField(max_length=200)
    EntryDate = models.DateTimeField('date published')
    def __str__(self):
        return self.WelcomeText

class Mydiabdocuments(models.Model):
    Filename = models.CharField(max_length=200)
    Fileurl = models.CharField(max_length=200)
    Description = models.CharField(max_length=400)
    DocumentDate = models.CharField(max_length=100)
    Dokuowner = models.CharField(max_length=100)
    EntryDate = models.DateTimeField('date published')
    def __str__(self):
        return self.Filename

class Mydiabevents2(models.Model):
    EventName = models.CharField(max_length=200)
    Eventowner = models.CharField(max_length=100)
    EventDate = models.DateField(null=True)
    EventTime = models.TimeField(null=True)
    EventDescription = models.CharField(max_length=400)
    EntryDate = models.DateTimeField('date published')
    def __str__(self):
        return self.EventName

class Mydiaborder(models.Model):
    OrderID = models.IntegerField(default=0)
    OrderDate = models.DateField(null=True)
    OrderRef = models.CharField(max_length=200, null=True)
    OrderForeignRef = models.CharField(max_length=200, null=True)
    OrderInitiator = models.CharField(max_length=200, null=False)
    OrderUser = models.CharField(max_length=200, null=False)
    OrderStatus = models.IntegerField(default=21, null=False)
    OrderSubmitDate = models.DateField(null=True)
    OrderCancellationDate = models.DateField(null=True)
    OrderCloseDate = models.DateField(null=True)
    OrderIntegrationRequestID = models.CharField(null=True, max_length=200)
    OrderSession = models.CharField(max_length=200, null=False)
    OrderCC = models.CharField(max_length=200, null=False)
    OrderOwner = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.OrderID

class Mydiabautorization(models.Model):
    UserName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_visitor = models.BooleanField(default=True)
    EntryDate = models.DateTimeField('date published')
    def __str__(self):
        return self.UserName
    def rolex(self):
        self.is_admin = True
        #return is_admin
    def rolexnot(self):
        self.is_admin = False
    def roley(self):
        self.is_doctor = True
        #return is_doctor
    def rolez(self):
        self.is_visitor = False
        #is_visitor=True
        #return is_visitor
class Mydiabrichblog(models.Model):
    BlogName = models.CharField(max_length=200)
    BlogEntry = models.DateTimeField('date published')
    BlogRich = models.TextField()
    BlogHtml = models.TextField()
    is_private = models.BooleanField(default=False)
    BlogOwner = models.CharField(max_length=200, default='public')
    AdminRight = models.CharField(max_length=20, default='A')
    #A Admin, B SuperUser, C User
    def __str__(self):
        return self.BlogName
    def setprivate(self):
        self.is_private = True
    def revokeprivate(self):
        self.is_private = False
class MydiabComments(models.Model):
    BlogName = models.ForeignKey(Mydiabrichblog, on_delete=models.CASCADE)
    CommentDate = models.DateTimeField('date published')
    CommentRich = models.TextField()
    is_private = models.BooleanField(default=False)
    CommentOwner = models.CharField(max_length=200, default='public')
    def __str__(self):
        return self.CommentRich
    def setprivate(self):
        self.is_private = True
    def revokeprivate(self):
        self.is_private = False
    
