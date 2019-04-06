import csv #moduel
import mydiabprod
#import sys import django import datetime
from django.db import models 
#from mydiabprod.models import Husers, Hresults 
from mydiabprod.models import Mydiabresults, Mydiabusers, Mydiabwelcome, Mydiabdocuments, Mydiabevents2, Mydiabautorization, Mydiabrichblog
from django.utils import timezone
#from mydiab.models import HgbControl, Users
from django.utils import timezone 
csvfile=open("results_29102018.csv", "r+", encoding="UTF-8") 
lines=csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE) 
for row in lines:
    deploy1 = row[0]+ " " + row[1]
    deploy2 = row[2]
    deploy3 = row[3]
    qq = Mydiabresults(DateTime=str(deploy1), HGB=str(deploy2), TypeOf=str(deploy3), DeployDate=timezone.now(), UserName_id=1)
    print("A: " + row[0] + " B: " + row[1] + " C: " + row[2] + " D: " + row[3])
    qq.save()
