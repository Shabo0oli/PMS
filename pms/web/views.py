from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Student ,Todo, Done, Course
from django.db.models import Sum
import jdatetime


# Create your views here.


def index(request):
    context = {}
    if request.user.is_authenticated():
        return render(request, 'index.html', context)
    else :
        return login_view(request)


@csrf_exempt
def login_view(request):
    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            st = Student.objects.filter(Username=user)[0]
            if( not st.IsValid ) :
                context = {}
                context['message'] = 'اکانت شما هنوز تایید نشده است'
                return render(request, 'login.html', context)
            login(request, user)
            student = Student.objects.filter(Username=user)
            context = {}
            #context['avatar'] = usrInfo[0].Avatar.url[4:]
            request.session['studentAvatar'] = student[0].Avatar.url[4:]
            request.session['user'] = user.username
            return render(request, 'index.html', context)
        else:
            context = {}
            context['message'] ='نام کاربری یا پسورد وارد شده اشتباه میباشد'
            return render(request, 'login.html', context)
    else:
        context = {}
        return render(request, 'login.html', context)



def register(request):
    if 'username' in request.POST and 'password' in request.POST and 'email' in request.POST:
        if User.objects.filter(email=request.POST['email']).exists() or User.objects.filter(username=request.POST['username']).exists():
            context = {}
            context['message']='مشخصات وارد شده تکراری میباشد'
            return render(request, 'register.html', context)
        else:
            username = request.POST['username']
            password = request.POST['password']
            phone = request.POST['phone']
            email = request.POST['email']
            name = request.POST['name']
            family = request.POST['family']
            user = User.objects.create_user(username, email, password)
            user.save()
            student = Student(Username=user, PhoneNumber=phone, Name=name, Family=family)
            student.save()
            context={}
            context['message'] = 'ثبت نام شما با موفقیت انجام شد.پس از تایید میتوانید در سیستم وارد شوید'
            return render(request, 'login.html', context)
    else:
        context = {}
        context['message'] = 'لطفا فیلد های فرم را به درستی پر کنید'
        return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def report(request):

    for i in range(0, 10):
        tagName = 'readed' + str(i)
        if tagName in request.POST:
            readed = request.POST[tagName]
            tested = request.POST['test'+str(i)]
            st = Student.objects.filter(Username=request.user)[0]
            cr = Course.objects.filter(id=i)[0]
            record = Done(StudentName=st, DoneDate=jdatetime.date.today(), CourseName=cr, StudyHour=readed, TestNumber=tested)
            record.save()

    context = {}
    isOk = 0
    if Done.objects.filter(StudentName__Username=request.user, DoneDate=jdatetime.date.today()):
        context['readonly'] = 'YES'
        isOk = 1
    context['ReportDay'] = jdatetime.date.today().day
    context['ReportMonth'] = jdatetime.date.j_months_fa[ jdatetime.date.today().month-1 ]
    context['ReportYear'] = jdatetime.date.today().year
    list1 = Todo.objects.filter(StudentName__Username=request.user, DueDate=jdatetime.date.today())
    list2 = Done.objects.filter(StudentName__Username=request.user, DoneDate=jdatetime.date.today())
    if isOk == 0:
        list2 = list1

    list = zip(list1, list2)
    context['List'] = list
    return render(request, 'report.html', context)


def statistics(request):
    context = {}
    if 'StartDate' in request.POST and 'EndDate' in request.POST:
        startDate = request.POST['StartDate'].split('-')
        startJDate = jdatetime.date(int(startDate[0]), int(startDate[1]), int(startDate[2]))
        endDate = request.POST['EndDate'].split('-')
        endJDate = jdatetime.date(int(endDate[0]), int(endDate[1]), int(endDate[2]))
        currentDate = startJDate



        endJDate = endJDate.__add__(jdatetime.timedelta(days=1))
        #context['dates'] = []
        crList = []
        sumList = []
        tstList = []

        courses = Course.objects.all()
        for cr in courses:
            list2 = Done.objects.filter(StudentName__Username=request.user, DoneDate__gte=startJDate, DoneDate__lte=endJDate, CourseName=cr)
            sum = 0
            test = 0
            for rec in list2:
                sum += rec.StudyHour
                test += rec.TestNumber
            crList.append(cr.Name)
            sumList.append(sum)
            tstList.append(test)
        context['courses'] = zip(crList,sumList , tstList)
        dtList = []
        tst2List = []
        sumList2 = []
        totalRead = 0
        totalTest = 0
        while currentDate != endJDate:
            dtList.append(currentDate)
            list2 = Done.objects.filter(StudentName__Username=request.user, DoneDate=currentDate)
            sum = 0
            test = 0
            for rec in list2:
                sum += rec.StudyHour
                totalRead +=rec.StudyHour
                test += rec.TestNumber
                totalTest +=rec.TestNumber

            tst2List.append(test)
            sumList2.append(sum)
            currentDate = currentDate.__add__(jdatetime.timedelta(days=1))

        dtList.append('مجموع')
        sumList2.append(totalRead)
        tst2List.append(totalTest)
        context['dates'] = zip(dtList,sumList2,tst2List)

    return render(request, 'statistics.html', context)