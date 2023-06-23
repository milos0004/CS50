from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import json
from .models import *
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "index.html")