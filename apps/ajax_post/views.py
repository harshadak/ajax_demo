from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from time import gmtime, strftime, localtime
from django.contrib import messages
from models import * # Need this in order to run queries
from django.core.urlresolvers import reverse
import bcrypt
from django.core import serializers

# Create your views here.

def index(request):
    print request.session.values()
    return render(request, 'ajax_post/my_post.html')


def add(request):
    posts = request.POST['post_name']
    return render(request, "ajax_post/posts.html", {"posts": posts})