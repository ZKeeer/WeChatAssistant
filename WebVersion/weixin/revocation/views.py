from django.shortcuts import render
import itchat
import os
import time
# Create your views here.
from revo import main
from threading import Thread

def index(request):
    return render(request, "revocation/index.html")


def get_img(request):
    path = os.path.dirname(__file__) + '/static'
    if not os.path.exists(path):
        os.mkdir(path)
    run_thread = Thread(target=main.run, args=(path + '/QR.png', ))
    run_thread.start()
    # run_thread.join()
    while True:
        time.sleep(3)
        if os.path.exists(path + '/QR.png'):
            context = {"IF_QR": True, }
            return render(request, "revocation/login.html", context)

    




def start_waiting(request):
    pass