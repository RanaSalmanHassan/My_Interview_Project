import pandas as pd
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from .forms import Create_Interview_Form
from django.contrib import messages
from django.views.generic import ListView
from .models import Interview
from django.contrib.auth.decorators import login_required
from calendar import month_name
import pandas as pd
# Create your views here.

@login_required(login_url='loginapp:login')
def createinterview(request):
    form = Create_Interview_Form
    if request.method == 'POST':
        form = Create_Interview_Form(request.POST)
        if form.is_valid():
            intboi = form.save(commit=False)
            intboi.user = request.user
            intboi.save()
            messages.success(request,'Added Your Interview!')
            return HttpResponseRedirect(reverse('intapp:choose_month'))
    
    dict = {'form':form}
    return render(request,'intapp/createint.html',dict)


@login_required(login_url='loginapp:login')
def IntDesciption(request,month):
    # now = datetime.now()
    # month = now.month
    this_month = month_name[month]
    interviews = Interview.objects.filter(user=request.user,date__month=month)
    count = Interview.objects.filter(user=request.user,date__month=month).count()
    return render(request, 'intapp/intdescription.html', {'interviews': interviews, 'month': month,'count':count,'this_month':this_month})


@login_required(login_url='loginapp:login')
def Choose_Month(request):
    return render(request,'intapp/choose_month.html')



def export_to_excel(request):
    interviews = Interview.objects.all()
    data = {
        'Serial Number': [i.id for i in interviews],
        'Date': [i.date for i in interviews],
        'Activities': [i.activities for i in interviews],
        'Numbers/Hours': [i.no_of_Hours for i in interviews],
        'Position of Interviewed Person': [i.positon_of_interviewd_person for i in interviews],
        'Marks (out of 10)': [i.marks for i in interviews],
        'Comments': [i.comments for i in interviews],
        'Attachments': [i.attachments.url if i.attachments else 'No CV' for i in interviews],
        'Refer': ['Yes' if i.refer else 'No' for i in interviews]
    }
    df = pd.DataFrame(data)
    df.to_csv('interviews.csv', index=False)
    messages.success(request,'Successfully Exported To Excel!')
    return render(request, 'intapp/intdescription.html', {'interviews': interviews})
