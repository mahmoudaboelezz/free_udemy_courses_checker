from datetime import datetime, timedelta
from multiprocessing import context
from django.shortcuts import render
import sys
sys.path.append('../')
from prayer_time import prayer
from udemy_course import get_courses
from django.core.paginator import Paginator

from core.udemy.models import emails
# Create your views here.
def home(request):
    """this is home page"""
    # print(prayer.prayer_times())
    # get time now
    total_length = get_courses().__len__()
    # get time in egypt
    time_in_egypt = datetime.now() + timedelta(hours=3)
    time = time_in_egypt.strftime('%A - %B "%m/%d/%Y"') 
    today_date = datetime.now().strftime('%A - %B "%m/%d/%Y"') 
    print(today_date)
    context = {'prayer_time': prayer.prayer_times(),'get_courses': get_courses(), 'total_length': total_length, 'today_date': today_date}
    return render(request, 'home.html', context)

def freeudemycourses(request):
    """
    this is a daily free udemy courses page
    """
    return render(request, 'freeudemycourses.html')

def daily_routine(request):
    """
    this is a daily routine page
    """
    return render(request, 'daily_routine.html')