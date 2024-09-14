import time, sys
import urllib
from urllib import request
import tkinter
import tkinter.messagebox

jobs = ['http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20Build%20Proxy/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20Logcheck%20Warnings/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20NbLogger/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20Static%20Analysis%20SM4/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20Target%20Test%20FSMr4%20(Stable)/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20Target%20Test%20Kep_fzm2cc%20(Stable)/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20Target%20Test%20Nyq%204Dsp_RL70%20(Stable)/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20Target%20Test%20Nyq%206Dsp_Basic%20(Stable)/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20Target%20Test%20Nyq%206Dsp_Mixed%20(Stable)/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20UT%20PS%20Sanitizer%20Gtest%20Lionfish/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20UT%20PS%20Sanitizer%20Gtest%20Nyq/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20UT%20PS%20Sanitizer%20Gtest%20SM4_Arm/',
        'http://wrlinb219.emea.nsn-net.net:8080/job/MACPS%20Trunk%20CI%20UT%20PS%20Sanitizer%20Gtest%20SM4_Dsp/']
status_red = False

def is_job_red(url):
    build_result_url = url + "/api/python?pretty=true"
    try:
        page_content = request.urlopen(build_result_url).read()
        page_dict = eval(page_content)
        if page_dict:
            return page_dict['lastCompletedBuild']['number'] != page_dict['lastSuccessfulBuild']['number']
        else:
            print("No build data.")
            sys.exit(0)
    except Exception:
        print("request data error !!!")
        sys.exit(0)

def has_red_job():
    for job in jobs:
        if is_job_red(job):
            return True
    return False

def report_red():
    window = tkinter.Tk()
    window.withdraw()
    tkinter.messagebox.showwarning(title='Warning', message='Trunk Turns Red!')

def report_green():
    window = tkinter.Tk()
    window.withdraw()
    tkinter.messagebox.showinfo(title='Info',message='Trunk Turns Green!')

def check_ci():
    global status_red
    if has_red_job():
        if (not status_red):
            report_red()
            status_red = True
        print('Trunk Turns Red!')
    else:
        if (status_red):
            report_green()
            status_red = False
        print('Trunk Turns Green!')

delay_minute = 1
while (True):
    time.sleep(delay_minute * 60)
    #print ("CI status")
    check_ci()
