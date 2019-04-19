##das external root cause causes uhrsache
###
from django.http import Http404
from django.template import loader
# Create your views here.
from .models import Mydiabresults, Mydiabusers, Mydiabwelcome, Mydiabdocuments, Mydiabevents2, Mydiabautorization, Mydiabrichblog, MydiabComments
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Max
from django.db.models import Avg
import random
from django.http import JsonResponse
import json
from django.core import serializers
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
import calendar
from django.shortcuts import render_to_response
import datetime
from django.utils.dateparse import parse_datetime
from django.utils.dateparse import parse_date
import holidays
import os
from django.core.files import File
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.paginator import Paginator
#def index(request):
    #return HttpResponse(template.render(contex, request))

def results(request):
    if request.method == 'POST':
        qq=Mydiabusers.objects.filter(UserName=request.POST.get('username')).filter(Password=request.POST.get('password'))
        qt=Mydiabwelcome.objects.all().aggregate(Max('id'))
        qt1=(qt['id__max'])
        qt2=random.randint(1, qt1)
        qt3=Mydiabwelcome.objects.get(id=qt2)
        docmax = Mydiabdocuments.objects.all().order_by('-id')[:3]
        docmax1 = docmax[0]
        docmax1_date = docmax1.DocumentDate
        docmax1_desc = docmax1.Description
        docmax1_url = docmax1.Fileurl
        docmax2 = docmax[1]
        docmax2_date = docmax2.DocumentDate
        docmax2_desc = docmax2.Description
        docmax2_url = docmax2.Fileurl
        docmax3 = docmax[2]
        docmax3_date = docmax3.DocumentDate
        docmax3_desc = docmax3.Description
        docmax3_url = docmax3.Fileurl

        eventmax = Mydiabevents2.objects.all().order_by('-id')[:3]
        eventmax1 = eventmax[0]
        eventmax2 = eventmax[1]
        eventmax3 = eventmax[2]
        if qq:
            uname1=Mydiabusers.objects.get(UserName=request.POST.get('username'))
            uname2=uname1.FirstName
            request.session['password'] = request.POST.get('password')
            request.session['member_id'] = uname1.id
            request.session['firstname'] = uname1.FirstName
            request.session['username'] = str(uname1.UserName)
            request.session['welcoming'] = str(qt3)
            request.session['document1_date'] = docmax1_date
            request.session['document1_url']= docmax1_url
            request.session['document1_desc'] =docmax1_desc
            request.session['document2_url'] = docmax2_url
            request.session['document2_date'] = docmax2_date
            request.session['document2_desc'] = docmax2_desc
            request.session['document3_url'] = docmax3_date
            request.session['document3_desc'] = docmax3_desc
            request.session['document3_date'] = docmax3_date
            request.session['eventmax1_name'] = eventmax1.EventName
            request.session['eventmax1_date'] = str(eventmax1.EventDate)[:16]
            request.session['eventmax1_desc'] = eventmax1.EventDescription
            request.session['eventmax2_name'] = eventmax2.EventName
            request.session['eventmax2_date'] = str(eventmax2.EventDate)[:16]
            request.session['eventmax2_desc'] = eventmax2.EventDescription
            request.session['eventmax3_name'] = eventmax3.EventName
            request.session['eventmax3_date'] = str(eventmax3.EventDate)[:16]
            request.session['eventmax3_desc'] = eventmax3.EventDescription
            request.session.set_expiry(0)
            latest_question_list = Mydiabresults.objects.filter(UserName_id=request.session['member_id']).order_by('-DateTime')[:30]
            request.session['results'] = str(latest_question_list)
            template = loader.get_template('mydiabprod/index.html')

            averagex = Mydiabresults.objects.all().filter(TypeOf='R').aggregate(Avg('HGB'))
            post_av1=int(averagex['HGB__avg'])
            request.session['averagex']=post_av1
            averagey = Mydiabresults.objects.all().filter(TypeOf='N').aggregate(Avg('HGB'))
            post_av2 = int(averagey['HGB__avg'])
            request.session['averagey'] = post_av2
        #pass welcoming to the user's window
            sessioncheck = request.session.get('welcoming')
        #pass firstname to the user's window
            sessioncheck2 = request.session.get('firstname')
            sessioncheck35 = request.session.get('username')
            sessioncheck3 = str(sessioncheck35)
            contex = {
                'latest_question_list': latest_question_list,
                'docmax1': docmax1_date,
                'docmax1_desc': docmax1_desc,
                'docmax1_url': docmax1_url,
                'docmax2': docmax2_date,
                'docmax2_desc': docmax2_desc,
                'docmax2_url': docmax2_url,
                'docmax3': docmax3_date,
                'docmax3_desc': docmax3_desc,
                'docmax3_url': docmax3_url,
                'sessioncheck': sessioncheck,
                'text2': sessioncheck,
                'averagex': post_av1,
                'averagey': post_av2,
                'firstname': sessioncheck2,
                'eventmax1_name': eventmax1.EventName,
                'eventmax1_date': str(eventmax1.EventDate)[:16],
                'eventmax1_desc': eventmax1.EventDescription,
                'eventmax2_name': eventmax2.EventName,
                'eventmax2_date': str(eventmax2.EventDate)[:16],
                'eventmax2_desc': eventmax2.EventDescription,
                'eventmax3_name': eventmax3.EventName,
                'eventmax3_date': str(eventmax3.EventDate)[:16],
                'eventmax3_desc': eventmax3.EventDescription,
            }
            return HttpResponse(template.render(contex, request))
    elif request.session.get('member_id'):
        template = loader.get_template('mydiabprod/index.html')
        latest_question_list = Mydiabresults.objects.filter(UserName_id=request.session.get('member_id')).order_by('-DateTime')[:100]
        sessioncheck = request.session.get('welcoming')
        sessioncheck2 = request.session.get('firstname')
        sessioncheck3 = request.session.get('username')
        post_av1 = request.session.get('averagex')
        post_av2 = request.session.get('averagey')
        contex = {
            'latest_question_list': latest_question_list,
            'sessioncheck': sessioncheck,
            'text2': sessioncheck,
            'averagex': post_av1,
            'averagey': post_av2,
            'firstname': sessioncheck2,
            'docmax1': request.session.get('document1_date'),
            'docmax1_desc': request.session.get('document1_desc'),
            'docmax1_url': request.session.get('document1_url'),
            'docmax2': request.session.get('document2_date'),
            'docmax2_desc': request.session.get('document2_desc'),
            'docmax2_url': request.session.get('document2_url'),
            'docmax3': request.session.get('document3_date'),
            'docmax3_desc': request.session.get('document3_desc'),
            'docmax3_url': request.session.get('document3_url'),
            'eventmax1_name': request.session.get('eventmax1_name'),
            'eventmax1_date': request.session.get('eventmax1_date'),
            'eventmax1_desc': request.session.get('eventmax1_desc'),
            'eventmax2_name': request.session.get('eventmax2_name'),
            'eventmax2_date': request.session.get('eventmax2_date'),
            'eventmax2_desc': request.session.get('eventmax2_desc'),
            'eventmax3_name': request.session.get('eventmax3_name'),
            'eventmax3_date': request.session.get('eventmax3_date'),
            'eventmax3_desc': request.session.get('eventmax3_desc'),
        }
        return HttpResponse(template.render(contex, request))
    else:
        #raise Http404("Wrong username or password")
        text1 = "wrong username or password"
        template = loader.get_template('mydiabprod/login.html')
        contex = {
            'text1': text1
        }
        return HttpResponse(template.render(contex, request))

def specific(request):
    if request.method=='GET':
        request.GET['lex']
        xps = request.GET['lex']
        sessioncheckxx = request.session.get('username')
        if xps == 'ALLX':
            latest_question_list = Mydiabresults.objects.filter(UserName_id=request.session['member_id']).order_by('-DateTime')
            qp = []
            DateTime = 'DateTime'
            UserName = 'UserName'
            HGB = 'HGB'
            TypeOf = 'TypeOf'
            for i in latest_question_list:
                # qx={ DateTime:i.DateTime, UserName:"wojtek", HGB:i.HGB, TypeOf:i.TypeOf }
                qp.append({DateTime: i.DateTime, UserName: sessioncheckxx, HGB: i.HGB, TypeOf: i.TypeOf})
                # qpx='{HGB:"152", UserName:"Wojtek", TypeOf:"R", DateTime: "2016-10-23 10:17:00"}'
            return HttpResponse(json.dumps(qp), content_type="application/json")
        else:
            latest_question_list = Mydiabresults.objects.filter(TypeOf=xps).filter(UserName_id=request.session['member_id']).order_by('-DateTime')[:100]
            qp = []
            DateTime='DateTime'
            UserName='UserName'
            HGB='HGB'
            TypeOf='TypeOf'
            for i in latest_question_list:
                qp.append({DateTime:i.DateTime, UserName:sessioncheckxx, HGB:i.HGB, TypeOf:i.TypeOf})
            return HttpResponse(json.dumps(qp), content_type="application/json")


def login(request):
    if not request.session.get('member_id'):
        template = loader.get_template('mydiabprod/login.html')
        contex = {
            'text1': "no active session please login"
            }
        return HttpResponse(template.render(contex, request))
    else:
        template = loader.get_template('mydiabprod/index.html')
        latest_question_list = Mydiabresults.objects.filter(UserName_id=request.session.get('member_id')).order_by('-DateTime')[:100]
        sessioncheck = request.session.get('welcoming')
        sessioncheck3 = request.session.get('username')

        #latest_question_list = request.session.get('results')
        sessioncheck2 = request.session.get('firstname')
        post_av1 = request.session.get('averagex')
        post_av2 = request.session.get('averagey')
        contex = {
            'latest_question_list': latest_question_list,
            'sessioncheck': sessioncheck,
            'text2': sessioncheck,
            'firstname': sessioncheck2,
            'averagex': post_av1,
            'averagey': post_av2,
            'docmax1': request.session.get('document1_date'),
            'docmax1_desc': request.session.get('document1_desc'),
            'docmax1_url': request.session.get('document1_url'),
            'docmax2': request.session.get('document2_date'),
            'docmax2_desc': request.session.get('document2_desc'),
            'docmax2_url': request.session.get('document2_url'),
            'docmax3': request.session.get('document3_date'),
            'docmax3_desc': request.session.get('document3_desc'),
            'docmax3_url': request.session.get('document3_url'),
            'eventmax1_name': request.session.get('eventmax1_name'),
            'eventmax1_date': request.session.get('eventmax1_date'),
            'eventmax1_desc': request.session.get('eventmax1_desc'),
            'eventmax2_name': request.session.get('eventmax2_name'),
            'eventmax2_date': request.session.get('eventmax2_date'),
            'eventmax2_desc': request.session.get('eventmax2_desc'),
            'eventmax3_name': request.session.get('eventmax3_name'),
            'eventmax3_date': request.session.get('eventmax3_date'),
            'eventmax3_desc': request.session.get('eventmax3_desc'),
            }
        return HttpResponse(template.render(contex, request))


def ajax(request):
    if request.method == u'GET':
        responsetext = "chjiaids"
        return HttpResponse(responsetext)


def logout(request):
    if request.method == 'POST':
        xexlog = request.POST['setting']
        if (xexlog == '3'):
            try:
                del request.session['member_id']
            except KeyError:
                pass
            text1 = "you are now logged out"
            template = loader.get_template('mydiabprod/login.html')
            contex = {
                'text1': text1
            }
            return HttpResponse(template.render(contex, request))
        elif (xexlog == '2'):
            return redirect('https://www.flickr.com/photos/desireedesire')
        elif (xexlog == '1'):
            return redirect('/admin/')


def upload_file(request):
    if request.method == 'POST' and request.FILES['myfiles']:
        myfiles=[]
        #filename = "tupa"
        myfiles=request.FILES.getlist('myfiles')
        fs = FileSystemStorage()
        upx = request.session.get('username')
        textarea = request.POST['textarea']
        datepix = request.POST['datepix']
        for myfile in myfiles:
            filename = fs.save(myfile.name, myfile)
            suploaded_file_url =fs.url(filename)
            q = Mydiabdocuments(Filename=filename, Fileurl=suploaded_file_url, Description=textarea, DocumentDate=datepix, Dokuowner=upx, EntryDate=timezone.now())
            q.save()
        text1="olokolo"
        return HttpResponse(text1)


def charts(request):
    if request.method == 'GET':
        DateTime = 'DateTime'
        HGB = 'HGB'
        #and request.get['foka']:
        latest_question_list = Mydiabresults.objects.filter(TypeOf='R').filter(UserName_id=request.session.get('member_id')).order_by('-DateTime')[:30]
        qpx=[]
        for i in latest_question_list:
            qpx.append({DateTime: i.DateTime[0:10], HGB: i.HGB})
        return HttpResponse(json.dumps(qpx), content_type="application/json")

#monthly calendar
def calendarium(request):
    if not request.session.get('member_id'):
##############################################################
#WJS 01.04.2019
# Currently only login screen will be provided with link to mydiabprod/results
# site is currently accessible only when sesssion exists 
# after connecting to domain a part for public access allowed is required here 
###
###############################################################
        template = loader.get_template('mydiabprod/login.html')
        contex = {
            'text1': "no active session please login"
            }
        return HttpResponse(template.render(contex, request))
    else:
        template = loader.get_template('mydiabprod/calendarx.html')
        contex = {
            'qx': "poka",
        }
        return HttpResponse(template.render(contex, request))

#weekly calendar
def eventum(request):
    if not request.session.get('member_id'):
##############################################################
#WJS 01.04.2019
# Currently only login screen will be provided with link to mydiabprod/results
# site is currently accessible only when sesssion exists 
# after connecting to domain a part for public access allowed is required here 
###
###############################################################
        template = loader.get_template('mydiabprod/login.html')
        contex = {
            'text1': "no active session please login"
            }
        return HttpResponse(template.render(contex, request))
    else:
        template = loader.get_template('mydiabprod/eventum.html')
        contex = {
            'qx': "pokas",
        }
        return HttpResponse(template.render(contex, request))
        #return HttpResponse(json.dumps(qz), content_type="application/json")

def eventlogx(request):
    if request.method == 'POST':
        eventowner = request.session.get('username')
        eventtime = request.POST['timepicker']
        eventdate = request.POST['datepicker']
        eventname = request.POST['eventname']
        eventdescription = request.POST['eventdesc']
        #eventdatetime = eventdate + " " + eventtime
        eventdatetime2 = parse_date(eventdate)
        #eventdatetime3 = timezone.make_aware(eventdatetime2, timezone.get_current_timezone())
        qpx = Mydiabevents2(EventName=eventname, Eventowner=eventowner, EventDate=eventdatetime2, EventTime=eventtime, EventDescription = eventdescription, EntryDate = timezone.now())
        qpx.save()
        return HttpResponse("OK")


def calendarx(request):
    #template = loader.get_template('mydiabprod/calendarx.html')
    if request.method == 'GET':
        #filex=open('/home/wojtek/git/pytho/pytho/django/web/mydiabprod/static/mydiabprod/datejson.json', 'w+', encoding='UTF-8')
        fullyear = request.GET['year']
        fullmonth = request.GET['month']
        px = calendar.TextCalendar(calendar.MONDAY)
        qx=[]
        hlistx = ['DE', 'PT']
        holidaylist = holidays.PL(years=int(fullyear))
        for entryx in hlistx:
            if entryx=='DE':
                holidaylist += holidays.DE(years=int(fullyear), prov='BY')
            else:
                holidaylist +=holidays.CountryHoliday(entryx)
        #holidaylist += holidays.PT(years=int(fullyear))
        for i in px.itermonthdates(int(fullyear), int(fullmonth)):
            holidayx=[]
            countrycodeappend=[]
            for countryx in holidaylist.country:
                ccappender = holidays.CountryHoliday(countryx)
                ccappender.year = int(fullyear)
                if countryx == 'DE':
                    ccappender += holidays.DE(years=int(fullyear), prov='BY')
                if str(i) in ccappender:
                    countrycodeappend.append(countryx)
            qq=Mydiabevents2.objects.filter(EventDate=i)
            ps = int(len(list(qq)))

            if (ps==0):
                eventx=[]
                eventx.append({"eventhour":" ", "eventdescp":" ", "eventname":" "})
                countingcodes = 0
                for datex, name in sorted(holidaylist.items()):
                    xyx = str(i)
                    xyz = str(datex)
                    if (xyz == xyx):
                        fussion = name.split(",")
                        for k in fussion:
                            holidayx.append({"pubname": k, "pubtype":countrycodeappend[countingcodes]})
                            countingcodes = countingcodes + 1
                qx.append({"date": str(i), "eventx": eventx, "pubholidayx": holidayx})
            else:
                eventx=[]
                for item in qq:
                    eventx.append({"eventhour":str(item.EventTime), "eventdescp":item.EventDescription, "eventname":item.EventName})
                countingcodes = 0
                for datex, name in sorted(holidaylist.items()):
                    xyx = str(i)
                    xyz = str(datex)
                    if (xyz == xyx):
                        fussion = name.split(",")
                        for k in fussion:
                            #countingcodes = 0
                            holidayx.append({"pubname": k, "pubtype": countrycodeappend[countingcodes]})
                            countingcodes = countingcodes + 1
                qx.append({"date": str(i), "eventx": eventx, "pubholidayx": holidayx})
    #filex.write("datejson="+json.dumps(qx))
        filex = open('/var/www/python-cgi/web/static/mydiabprod/datejson12.json', 'w+', encoding='UTF-8')
        filex.write("datejson=" + json.dumps(qx))
        return HttpResponse(json.dumps(qx), content_type="application/json")
    #return HttpResponse(qx)

def delevent(request):
    if request.method == 'POST':
        fulldate = request.POST['eventdate']
        fulltime = request.POST['eventtime']
        #fullname = request.POST['eventname']
        qpx = Mydiabevents2.objects.filter(EventDate=fulldate).filter(EventTime=fulltime)
        qpx.delete()
        return HttpResponse("ok")

def calendarmainlist(request):
    if request.method == 'GET':
        fulldatex = request.GET['datex']
        fullyear = fulldatex[:4]
        qx=[]
        eventx = []
        hlistx = ['DE', 'PT']
        holidaylist = holidays.PL(years=int(fullyear))
        for entryx in hlistx:
            if entryx == 'DE':
                holidaylist += holidays.DE(years=int(fullyear), prov='BY')
            else:
                holidaylist += holidays.CountryHoliday(entryx)
        holidayx = []
        countrycodeappend = []
        for countryx in holidaylist.country:
            ccappender = holidays.CountryHoliday(countryx)
            ccappender.year = int(fullyear)
            if countryx == 'DE':
                ccappender += holidays.DE(years=int(fullyear), prov='BY')
            if str(fulldatex) in ccappender:
                countrycodeappend.append(countryx)
        qq=Mydiabevents2.objects.filter(EventDate=fulldatex)
        #ps = int(len(list(qq)))
        for i in qq:
            eventx.append({"eventhour":str(i.EventTime), "eventdescp":i.EventDescription, "eventname":i.EventName})
        countingcodes = 0
        for datex, name in sorted(holidaylist.items()):
            xyx = str(fulldatex)
            xyz = str(datex)
            if (xyz == xyx):
                fussion = name.split(",")
                for k in fussion:
                    holidayx.append({"pubname": k, "pubtype": countrycodeappend[countingcodes]})
                    countingcodes = countingcodes + 1
        qx.append({"date": str(fulldatex), "eventx": eventx, "pubholidayx": holidayx})
    return HttpResponse(json.dumps(qx), content_type="application/json")

def checkevent(request):
    if request.method == 'GET':
        fulldate = request.GET['fulldate']
        fullhours = request.GET['fullhours']
        #fullhours = fulldatex[:4]
        qx=[]
        eventx = []
        qq=Mydiabevents2.objects.filter(EventDate=fulldate).filter(EventTime=fullhours)
        #ps = int(len(list(qq)))
        #for i in qq:
        #eventx.append({"eventhour":str(qq.EventTime), "eventdescp":qq.EventDescription, "eventname":qq.EventName})
        eventx.append({"eventname": qq.EventName})
        #qx.append({"date": str(fulldatex), "eventx": eventx})
        return HttpResponse(json.dumps(eventx), content_type="application/json")

def checkeventsecond(request):
    if request.method == 'GET':
        fulldate = request.GET['fulldate']
        fullhours = request.GET['fullhours']
        #fullhours = fulldatex[:4]
        qx=[]
        eventx = []
        qq=Mydiabevents2.objects.filter(EventDate=fulldate).filter(EventTime=fullhours)
        #ps = int(len(list(qq)))
        #for i in qq:
        #eventx.append({"eventhour":str(qq.EventTime), "eventdescp":qq.EventDescription, "eventname":qq.EventName})
        eventx.append({"eventname": qq.EventName})
        #qx.append({"date": str(fulldatex), "eventx": eventx})
        return HttpResponse(json.dumps(eventx), content_type="application/json")

def currentweek(request):
    if request.method == 'GET':
        fullyear = request.GET['year']
        fullmonth = request.GET['month']
        fullday = request.GET['day']
        weekminus = []
        daybase = datetime.date(int(fullyear), int(fullmonth), int(fullday))
        caldelta = daybase.weekday()
        dayminuscalculate = datetime.timedelta(caldelta)
        dayfirstminus = daybase - dayminuscalculate
        deltaweekdays = datetime.timedelta(1)
        daysecondminus = dayfirstminus + deltaweekdays
        daythirdminus = daysecondminus + deltaweekdays
        dayfourthminus = daythirdminus + deltaweekdays
        dayfifthminus = dayfourthminus + deltaweekdays
        daysixthminus = dayfifthminus + deltaweekdays
        dayseventhminus = daysixthminus + deltaweekdays
        weekminus.append(dayfirstminus)
        weekminus.append(daysecondminus)
        weekminus.append(daythirdminus)
        weekminus.append(dayfourthminus)
        weekminus.append(dayfifthminus)
        weekminus.append(daysixthminus)
        weekminus.append(dayseventhminus)
        #px = calendar.TextCalendar(calendar.MONDAY)
        qx=[]
        hlistx = ['DE', 'PT']
        holidaylist = holidays.PL(years=int(fullyear))
        for entryx in hlistx:
            if entryx=='DE':
                holidaylist += holidays.DE(years=int(fullyear), prov='BY')
            else:
                holidaylist +=holidays.CountryHoliday(entryx)
        #holidaylist += holidays.PT(years=int(fullyear))
        for i in weekminus:
            holidayx=[]
            countrycodeappend=[]
            for countryx in holidaylist.country:
                ccappender = holidays.CountryHoliday(countryx)
                ccappender.year = int(fullyear)
                if countryx == 'DE':
                    ccappender += holidays.DE(years=int(fullyear), prov='BY')
                if str(i) in ccappender:
                    countrycodeappend.append(countryx)
            qq=Mydiabevents2.objects.filter(EventDate=i)
            ps = int(len(list(qq)))

            if (ps==0):
                eventx=[]
                eventx.append({"eventhour":" ", "eventdescp":" ", "eventname":" "})
                countingcodes = 0
                for datex, name in sorted(holidaylist.items()):
                    xyx = str(i)
                    xyz = str(datex)
                    if (xyz == xyx):
                        fussion = name.split(",")
                        for k in fussion:
                            holidayx.append({"pubname": k, "pubtype":countrycodeappend[countingcodes]})
                            countingcodes = countingcodes + 1
                qx.append({"date": str(i), "eventx": eventx, "pubholidayx": holidayx})
            else:
                eventx=[]
                for item in qq:
                    eventx.append({"eventhour":str(item.EventTime), "eventdescp":item.EventDescription, "eventname":item.EventName})
                countingcodes = 0
                for datex, name in sorted(holidaylist.items()):
                    xyx = str(i)
                    xyz = str(datex)
                    if (xyz == xyx):
                        fussion = name.split(",")
                        for k in fussion:
                            #countingcodes = 0
                            holidayx.append({"pubname": k, "pubtype": countrycodeappend[countingcodes]})
                            countingcodes = countingcodes + 1
                qx.append({"date": str(i), "eventx": eventx, "pubholidayx": holidayx})
    #filex.write("datejson="+json.dumps(qx))
        filex = open('/srv/samba/share/pytho/django/web/mydiabprod/static/mydiabprod/datejson1231.json', 'w+', encoding='UTF-8')
        filex.write("datejson=" + json.dumps(qx))
        return HttpResponse(json.dumps(qx), content_type="application/json")
#daily calendar	
def quotidie(request):
    if not request.session.get('member_id'):
##############################################################
#WJS 01.04.2019
# Currently only login screen will be provided with link to mydiabprod/results
# site is currently accessible only when sesssion exists 
# after connecting to domain a part for public access allowed is required here 
###
###############################################################
        template = loader.get_template('mydiabprod/login.html')
        contex = {
            'text1': "no active session please login"
            }
        return HttpResponse(template.render(contex, request))
    else:
        template = loader.get_template('mydiabprod/quotidie.html')
        contex = {
            'qx': "pokas",
        }
        return HttpResponse(template.render(contex, request))

def loginx(request):
    if not request.session.get('member_id'):
        template = loader.get_template('mydiabprod/loginx.html')
        contex = {
            'text1': "nono active session please login"
        }
        return HttpResponse(template.render(contex, request))
    elif request.session.get('member_id'):
        template = loader.get_template('mydiabprod/pers.html')
        qx1 = Mydiabautorization.objects.get(id=1)
        if ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == True))\
        or ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == False))\
        or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == True))\
        or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == False)):
            variable1 = 'admin_view'
        elif ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == False))\
        or ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == True)):
            variable1 = 'doctor_view'
        elif ((qx1.is_visitor == True) and (qx1.is_admin == False) and (qx1.is_doctor == False)):
            variable1 = 'user_view'
        else: variable1 = 'no_access'
        contextauth = {
            'variable1': variable1
        }
        return HttpResponse(template.render(contextauth, request))
def persefona(request):
    if request.method == 'POST':
        qqx=Mydiabusers.objects.filter(UserName=request.POST.get('username')).filter(Password=request.POST.get('password'))
        if qqx:
            template = loader.get_template('mydiabprod/pers.html')
            qx1 = Mydiabautorization.objects.get(id=1)
            if ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == True))\
            or ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == False))\
            or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == True))\
            or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == False)):
                variable1 = 'admin_view'
            elif ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == False))\
            or ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == True)):
                variable1 = 'doctor_view'
            elif ((qx1.is_visitor == True) and (qx1.is_admin == False) and (qx1.is_doctor == False)):
                variable1 = 'user_view'
            else: variable1 = 'no_access'
            qt29 = Mydiabrichblog.objects.all().aggregate(Max('id'))
            qt43 = (qt29['id__max'])
            fileqxbase = Mydiabrichblog.objects.get(id=qt43)
            fileqx = fileqxbase.BlogRich
            fileqq = open(fileqx, "r")
            filehtml = fileqq.read()
            fileqq.close()
            contextauth = {
                'bloghtml': filehtml,
                'variable1': variable1
            }
            return HttpResponse(template.render(contextauth, request))
        else:
        #raise Http404("Wrong username or password")
            text1 = "wrong username or password"
            template = loader.get_template('mydiabprod/loginx.html')
            contex = {
                'text1': text1
            }
            return HttpResponse(template.render(contex, request))
    elif request.session.get('member_id'):
        template = loader.get_template('mydiabprod/pers.html')
        qx1 = Mydiabautorization.objects.get(id=1)
        if ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == True))\
        or ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == False))\
        or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == True))\
        or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == False)):
            variable1 = 'admin_view'
        elif ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == False))\
        or ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == True)):
            variable1 = 'doctor_view'
        elif ((qx1.is_visitor == True) and (qx1.is_admin == False) and (qx1.is_doctor == False)):
            variable1 = 'user_view'
        else: variable1 = 'no_access'
        qt29 = Mydiabrichblog.objects.all().aggregate(Max('id'))
        qt43 = (qt29['id__max'])
        fileqxbase = Mydiabrichblog.objects.get(id=qt43)
        fileqx = fileqxbase.BlogRich
        fileqq = open(fileqx, "r")
        filehtml = fileqq.read()
        fileqq.close()
        contextauth = {
            'bloghtml': filehtml,
            'variable1': variable1
        }
        return HttpResponse(template.render(contextauth, request))
    else:
        #raise Http404("Wrong username or password")
        text1 = "no active session please login"
        template = loader.get_template('mydiabprod/loginx.html')
        contex = {
            'text1': text1
        }
        return HttpResponse(template.render(contex, request))

def richtextblog(request):
    if request.method == 'POST':
        post_owner = request.session.get('username')
        richblogtext = request.POST['richtextblogx']
        richname = request.POST['title']
        richprivacy = request.POST['privacy']
        if (richprivacy == 'private'):
            make_private = 1
        else:
            make_private = 0
        check_role = Mydiabautorization.objects.get(UserName=post_owner)
        if (check_role.is_admin == True):
            role_flag = 'A' #for Admin
        elif (check_role.is_doctor):
            role_flag = 'S' #for Super User 
        elif (check_role.is_visitor):
            role_flag = 'R' #for RegularVisitor
        else:
            role_flag = 'V' # for public visitor 
################################

#        make_private = False
        richblogdate = timezone.now()
        qz = random.randint(1, 100000)
        qzsb = str(richname)
        qzsy = qzsb.replace(" ", "")
        qzsx = ".html"
        qzs = qzsy+qzsx
        fdset = staticfiles_storage.path("mydiabprod/blogx/"+qzs)
###################
# WJS 01.04.2019 block for saving input into the file
###################
        with open(fdset, "w+") as filexz:
            filexx=File(filexz)
            filexx.write(richblogtext)
        added_file_url = fdset
        qblx = Mydiabrichblog(BlogName=richname, BlogEntry=richblogdate, BlogRich=added_file_url, BlogHtml=richblogtext, is_private=make_private, BlogOwner=post_owner, AdminRight=role_flag)
        qblx.save()
        dt = datetime.datetime.now()
        eventowner = Mydiabusers.objects.get(id=1)
        et1 = str(dt.hour)
        et2 = str(dt.minute)
        et3 = str(dt.second)
        ed1 = str(dt.year)
        ed2 = str(dt.month)
        ed3 = str(dt.day)
        eventtime = et1+":"+et2+":"+et3+".000000"
        eventdatetime2 = ed1+"-"+ed2+"-"+ed3
        eventname = richname
        eventdescription = "new entry in blog"
        qpx = Mydiabevents2(EventName=eventname, Eventowner=eventowner, EventDate=eventdatetime2, EventTime=eventtime, EventDescription = eventdescription, EntryDate = timezone.now())
        qpx.save()
        #os.remove(filexx)
        #os.remove(filexz)
        filexx.close()
        filexz.close()
        return HttpResponse("OK")

def instantimage(request):
    if request.method == 'POST':
        # and request.FILES:
        sequencefiles=[]
        #filename = "tupa"
        #sequencefiles=request.FILES.getlist('images')
        sequencefiles=request.FILES.getlist('file');
        fs = FileSystemStorage()
        upx = "unkas"
        textarea = "test"
        datepix = "2019-03-23"
        for sequencefile in sequencefiles:
            sequencefilename = fs.save(sequencefile.name, sequencefile)
            sequencefileurl =fs.url(sequencefilename)
            q = Mydiabdocuments(Filename=sequencefilename, Fileurl=sequencefileurl, Description=textarea, DocumentDate=datepix, Dokuowner=upx, EntryDate=timezone.now())
            q.save()
            url=sequencefileurl
            return HttpResponse(url)
			
def instantimageremove(request):
    if request.method == 'POST':
        sequence_from_ajax=request.POST['targetsrc']
        sequence_for_del_path = '/var/www/python-cgi/web/'
        sequence_for_replace = sequence_from_ajax.replace('http://192.168.2.50:8000/', sequence_for_del_path)
        os.remove(sequence_for_replace)
        sequence_for_database = sequence_from_ajax.replace('http://192.168.2.50:8000', "")
        delx = Mydiabdocuments.objects.get(Fileurl=sequence_for_database)
        delx.delete()
        infoback = 'file has been deleted from server'
        return HttpResponse(infoback)

#section for summernote editor publish		
def pers_blog(request):
    if not request.session.get('member_id'):
##############################################################
#WJS 01.04.2019
# Currently only login screen will be provided with link to mydiabprod/results
# site is currently accessible only when sesssion exists 
# after connecting to domain a part for public access allowed is required here 
###
###############################################################
        template = loader.get_template('mydiabprod/login.html')
        contex = {
            'text1': "no active session please login"
            }
        return HttpResponse(template.render(contex, request))
    else:
        #qqx=Mydiabusers.objects.filter(UserName=request.POST.get('username')).filter(Password=request.POST.get('password'))
        template = loader.get_template('mydiabprod/pers_blog.html')
        post_owner = request.session.get('username')
        qt0 = Mydiabusers.objects.get(UserName=post_owner)
        qx1 = Mydiabautorization.objects.get(UserName=qt0)
        if ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == True))\
        or ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == False))\
        or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == True))\
        or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == False)):
            variable1 = 'admin_view'
        elif ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == False))\
        or ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == True)):
            variable1 = 'doctor_view'
        elif ((qx1.is_visitor == True) and (qx1.is_admin == False) and (qx1.is_doctor == False)):
            variable1 = 'user_view'
        else: 
            variable1 = 'no_access'
        qt29 = Mydiabrichblog.objects.all().aggregate(Max('id')) ## aggregation for instant preview after publish is triggered 
        qt43 = (qt29['id__max'])
        fileqxbase = Mydiabrichblog.objects.get(id=qt43)
        filehtml = fileqxbase.BlogHtml
        qt=Mydiabwelcome.objects.all().aggregate(Max('id'))
        qt1=(qt['id__max'])
        qt2=random.randint(1, qt1)
        qt3=Mydiabwelcome.objects.get(id=qt2)
        qt4 = qx1.FirstName
        contextauth = {
            'firstname': qt4,
            'text2': qt3,
            'bloghtml': filehtml,
            'variable1': variable1
        }
        return HttpResponse(template.render(contextauth, request))

#blog display beta
################3
def blog_counter(request):
    if not request.session.get('member_id'):
##############################################################
#WJS 01.04.2019
# Currently only login screen will be provided with link to mydiabprod/results
# site is currently accessible only when sesssion exists 
# after connecting to domain a part for public access allowed is required here 
###
###############################################################
        template = loader.get_template('mydiabprod/login.html')
        contex = {
            'text1': "no active session please login"
            }
        return HttpResponse(template.render(contex, request))
    else:
        template = loader.get_template('mydiabprod/blog_counter.html')
        post_owner = request.session.get('username')
        qt0 = Mydiabusers.objects.get(UserName=post_owner)
        qx1 = Mydiabautorization.objects.get(UserName=qt0)
        if (qx1.is_admin == True):
            role_check = 'A'
 #################################################################################################
 #WJS 01.04.2019
 #      can do other actions - in this case only text is passed to variable1 - admin_view
 #
 #################################################################################################
        elif (qx1.is_doctor == True):
            role_check = 'SU'
        elif (qx1.is_visitor == True):
            role_check = 'R'
        else: role_check = 'V'
#########################################################################
#WJS 01.04.2019
#MAX ID | MIN ID aggregation                                            #
#qt29 = Mydiabrichblog.objects.all().aggregate(Max('id'))               #
#qt43 = (qt29['id__max'])                                               #
#########################################################################
#01.04.2019
# adding section to deploy comments 
# either by DJANGO TEMPLATE CONTEXT - if block for 3 types of authorization - is_admin, is_doctor (is_superuser), is_private (is_visitor - public)
# or JSON where json_comment = [] for initiate and json_comment.append({DATA FROM MydiabComments.objects.filter})
##########################################################################
        if (post_owner) and (qx1.is_admin == True):
            html_looping = Mydiabrichblog.objects.all().order_by('-id')
            comment_source = MydiabComments.objects.all()
            user_role = 'admin'
# visitors is_visitor will only publish public posts therefore all will be visible by is_doctor (SU) SU can restrict own posts (only A+SU will see it)
        elif (post_owner) and (qx1.is_doctor == True):
            html_looping = (Mydiabrichblog.objects.filter(BlogOwner=post_owner) | Mydiabrichblog.objects.filter(AdminRight='S') |  Mydiabrichblog.objects.filter(AdminRight='R') | Mydiabrichblog.objects.filter(is_private=False)).order_by('-id')
            comment_source = MydiabComments.objects.all()
            #comment_source = MydiabComments.objects.filter(Comment_Owner=post_owner) | MydiabComments.objects.filter(is_private=False)
            user_role = 'superuser'
        elif (post_owner) and (qx1.is_visitor == True):
            html_looping = (Mydiabrichblog.objects.filter(BlogOwner=post_owner) | Mydiabrichblog.objects.filter(is_private=False)).order_by('-id')
            comment_source = MydiabComments.objects.all()
            #comment_source = MydiabComments.objects.filter(Comment_Owner=post_owner) | MydiabComments.objects.filter(is_private=False)
            user_role = 'visitor'
        else:
            html_looping = Mydiabrichblog.objects.filter(is_private = False).order_by('-id')
            comment_source = MydiabComments.objects.all()
            #comment_source = MydiabComments.objects.filter(is_private = False)
            user_role = 'public'
        qt=Mydiabwelcome.objects.all().aggregate(Max('id'))
        qt1=(qt['id__max'])
        qt2=random.randint(1, qt1)
        qt3=Mydiabwelcome.objects.get(id=qt2)
        qt4 = qx1.FirstName
        roles_check = 'V'
        max_id = html_looping.aggregate(Max('id'))
        max_display = max_id['id__max']
        paginator = Paginator(html_looping, 5)
        page = request.GET.get('page')
        get_subpage = paginator.get_page(page)
        context = {
            'html_loop': get_subpage,
			'html_comments': comment_source,
			'user_role': user_role,
            'postowner': post_owner,
            'max_display': max_display
        }
        return HttpResponse(template.render(context, request))

def mydiab_comments(request):
    if request.method == 'POST':
        user_check = request.session.get('username')
        comment_target = request.POST['blog_title']
        comment_text = request.POST['comment_text']
        comment_ownerx = request.POST['comment_owner']
        coment_privacy = request.POST['privacy_status']
        if comment_privacy:
            comment_privacy = True
        else: comment_privacy = False
        if user_check:
            comment_owner = user_check
        elif comment_ownerx:
            comment_owner = comment_ownerx
        else: commetn_owner = public
        comment_add = MydiabComments(BlogName=comment_target, CommentDate=timezone.now(), CommentRich=comment_text, is_private=comment_privacy, CommentOwner=comment_owner)
        comment_add.save()
        text = "comment added"
        return HttpResponse(text)

def postremove(request):
    if request.method == 'POST':
        user_check = request.session.get('username')
        post_for_del_string=request.POST['target']
        post_for_del_int = int(post_for_del_string)
        post_delx =  Mydiabrichblog.objects.get(id=post_for_del_int)
        post_delx.delete()
        infoback = 'post has been deleted from server'
        return HttpResponse(infoback)

def postsetpublic(request):
    if request.method == 'POST':
        user_check = request.session.get('username')
        post_for_pub_string=request.POST['target']
        post_for_pub_int = int(post_for_pub_string)
        post_pubx = Mydiabrichblog.objects.get(id=post_for_pub_int)
        post_pubx.is_private = 0
        post_pubx.save()
        infoback = 'post privacy set public'
        return HttpResponse(infoback)

def postsetprivate(request):
    if request.method == 'POST':
        user_check = request.session.get('username')
        #implement here additional conditions for changing privacy eq. if (user_check == post_owner):xx
        post_for_priv_string=request.POST['target']
        post_for_priv_int = int(post_for_priv_string)
        post_privx = Mydiabrichblog.objects.get(id=post_for_priv_int)
        post_privx.is_private = 1
        post_privx.save()
        infoback = 'post privacy set private'
        return HttpResponse(infoback)

def getforwards(request):
    if request.method == 'POST':
        id_for_check = request.POST['forward']
        take_int = int(id_for_check)
        template = loader.get_template('mydiabprod/blog_counter.html')
        post_owner = request.session.get('username')
        qt0 = Mydiabusers.objects.get(UserName=post_owner)
        qx1 = Mydiabautorization.objects.get(UserName=qt0)
        if (qx1.is_admin == True):
            role_check = 'A'
 #################################################################################################
 #WJS 01.04.2019
 #      can do other actions - in this case only text is passed to variable1 - admin_view
 #
 #################################################################################################
        elif (qx1.is_doctor == True):
            role_check = 'SU'
        elif (qx1.is_visitor == True):
            role_check = 'R'
        else: role_check = 'V'
#########################################################################
#WJS 01.04.2019
#MAX ID | MIN ID aggregation                                            #
#qt29 = Mydiabrichblog.objects.all().aggregate(Max('id'))               #
#qt43 = (qt29['id__max'])                                               #
#########################################################################
#01.04.2019
# adding section to deploy comments 
# either by DJANGO TEMPLATE CONTEXT - if block for 3 types of authorization - is_admin, is_doctor (is_superuser), is_private (is_visitor - public)
# or JSON where json_comment = [] for initiate and json_comment.append({DATA FROM MydiabComments.objects.filter})
##########################################################################
        if (post_owner) and (qx1.is_admin == True):
            #html_looping = Mydiabrichblog.objects.filter(id__gt=take_int)
			
            comment_source = MydiabComments.objects.all()
            user_role = 'admin'
# visitors is_visitor will only publish public posts therefore all will be visible by is_doctor (SU) SU can restrict own posts (only A+SU will see it)
        elif (post_owner) and (qx1.is_doctor == True):
            html_looping = (Mydiabrichblog.objects.filter(BlogOwner=post_owner) | Mydiabrichblog.objects.filter(AdminRight='S') |  Mydiabrichblog.objects.filter(AdminRight='R') | Mydiabrichblog.objects.filter(is_private=False)).order_by('-id')
            comment_source = MydiabComments.objects.all()
            #comment_source = MydiabComments.objects.filter(Comment_Owner=post_owner) | MydiabComments.objects.filter(is_private=False)
            user_role = 'superuser'
        elif (post_owner) and (qx1.is_visitor == True):
            html_looping = (Mydiabrichblog.objects.filter(BlogOwner=post_owner) | Mydiabrichblog.objects.filter(is_private=False)).order_by('-id')
            comment_source = MydiabComments.objects.all()
            #comment_source = MydiabComments.objects.filter(Comment_Owner=post_owner) | MydiabComments.objects.filter(is_private=False)
            user_role = 'visitor'
        else:
            html_looping = Mydiabrichblog.objects.filter(is_private = False).order_by('-id')
            comment_source = MydiabComments.objects.all()
            #comment_source = MydiabComments.objects.filter(is_private = False)
            user_role = 'public'
        qt=Mydiabwelcome.objects.all().aggregate(Max('id'))
        qt1=(qt['id__max'])
        qt2=random.randint(1, qt1)
        qt3=Mydiabwelcome.objects.get(id=qt2)
        qt4 = qx1.FirstName
        roles_check = 'V'
        max_id = html_looping.aggregate(Max('id'))
        max_display = max_id['id__max']
        paginator = Paginator(html_looping, 2)
        page = request.GET.get('page')
        get_subpage = paginator.get_page(page)
        context = {
            'html_loop': get_subpage,
			'html_comments': comment_source,
			'user_role': user_role,
            'postowner': post_owner,
            'max_display': max_display
        }
        return HttpResponse(context)
    

def getpostx(request):
    if request.method == 'POST':
        user_check = request.session.get('username')
        #implement here additional conditions for changing privacy eq. if (user_check == post_owner):xx
        post_for=request.POST['target']
        if post_for == "get_post":
            csvfile=open("mydiabprod/templates/mydiabprod/form.html", "r+", encoding="UTF-8")
            poka = csvfile.read()
            context = {
                'poka': poka
            }
            return HttpResponse(poka)
def searchblogx(request):
    if request.method == 'POST':
        user_check = request.session.get('username')
        #implement here additional conditions for changing privacy eq. if (user_check == post_owner):xx
        post_forx=request.POST['searchinput']
            #csvfile=open("mydiabprod/templates/mydiabprod/form.html", "r+", encoding="UTF-8")
            #poka = csvfile.read()
        stext = 'tttt'
        return HttpResponse(post_forx)

def getsearch(request):
    if request.method == 'GET':
        testy =[]
        variabley = request.GET['parameter']
        variablex = 'getJSON test'
        testy.append({'testx': variablex})
        return HttpResponse(testy)

#####################################################################################################################################################
##############################################################################################################3
#block for older pers view - will be disconnected
# WJS 01.04.2019
# def pers(request):
    # if request.method == 'POST':
        # qqx=Mydiabusers.objects.filter(UserName=request.POST.get('username')).filter(Password=request.POST.get('password'))
        # if qqx:
            # template = loader.get_template('mydiabprod/pers.html')
            # qt0 = Mydiabusers.objects.get(id=1)
            # qx1 = Mydiabautorization.objects.get(UserName=qt0)
            # if ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == True))\
            # or ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == False))\
            # or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == True))\
            # or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == False)):
                # variable1 = 'admin_view'
            # elif ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == False))\
            # or ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == True)):
                # variable1 = 'doctor_view'
            # elif ((qx1.is_visitor == True) and (qx1.is_admin == False) and (qx1.is_doctor == False)):
                # variable1 = 'user_view'
            # else: variable1 = 'no_access'
            # qt29 = Mydiabrichblog.objects.all().aggregate(Max('id'))
            # qt43 = (qt29['id__max'])
            # fileqxbase = Mydiabrichblog.objects.get(id=qt43)
            # fileqx = fileqxbase.BlogRich
            # fileqq = open(fileqx, "r")
            # filehtml = fileqq.read()
            # fileqq.close()
            # qt=Mydiabwelcome.objects.all().aggregate(Max('id'))
            # qt1=(qt['id__max'])
            # qt2=random.randint(1, qt1)
            # qt3=Mydiabwelcome.objects.get(id=qt2)
            # qt4 = qx1.FirstName
            # contextauth = {
                # 'firstname': qt4,
                # 'text2': qt3,
                # 'bloghtml': filehtml,
                # 'variable1': variable1
            # }
            # return HttpResponse(template.render(contextauth, request))
        # else:
        # #raise Http404("Wrong username or password")
            # text1 = "wrong username or password"
            # template = loader.get_template('mydiabprod/loginx.html')
            # contex = {
                # 'text1': text1
            # }
            # return HttpResponse(template.render(contex, request))
    # elif request.session.get('member_id'):
        # template = loader.get_template('mydiabprod/pers.html')
        # qt0 = Mydiabusers.objects.get(id=1)
        # qx1 = Mydiabautorization.objects.get(UserName=qt0)
        # if ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == True))\
        # or ((qx1.is_admin == True) and (qx1.is_doctor == True) and (qx1.is_visitor == False))\
        # or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == True))\
        # or ((qx1.is_admin == True) and (qx1.is_doctor == False) and (qx1.is_visitor == False)):
            # variable1 = 'admin_view'
        # elif ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == False))\
        # or ((qx1.is_doctor == True) and (qx1.is_admin == False) and (qx1.is_visitor == True)):
            # variable1 = 'doctor_view'
        # elif ((qx1.is_visitor == True) and (qx1.is_admin == False) and (qx1.is_doctor == False)):
            # variable1 = 'user_view'
        # else: variable1 = 'no_access'
        # qt29 = Mydiabrichblog.objects.all().aggregate(Max('id'))
        # qt43 = (qt29['id__max'])
        # fileqxbase = Mydiabrichblog.objects.get(id=qt43)
        # fileqx = fileqxbase.BlogRich
        # fileqq = open(fileqx, "r")
        # filehtml = fileqq.read()
        # fileqq.close()
        # qt=Mydiabwelcome.objects.all().aggregate(Max('id'))
        # qt1=(qt['id__max'])
        # qt2=random.randint(1, qt1)
        # qt3=Mydiabwelcome.objects.get(id=qt2)
        # qt4 = qx1.FirstName
        # contextauth = {
            # 'firstname': qt4,
            # 'text2': qt3,
            # 'bloghtml': filehtml,
            # 'variable1': variable1
        # }
        # return HttpResponse(template.render(contextauth, request))
    # else:
        # #raise Http404("Wrong username or password")
        # text1 = "no active session please login"
        # template = loader.get_template('mydiabprod/loginx.html')
        # contex = {
            # 'text1': text1
        # }
        # return HttpResponse(template.render(contex, request))
        # xx = re.match("<[\w*\d*]+>[\w*\s*]+</[\w*\d*]+>", lox).group()
