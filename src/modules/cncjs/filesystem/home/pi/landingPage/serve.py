#!/usr/bin/env python3

import subprocess

from flask import Flask, render_template, request
app = Flask("Luban Landing Page")

def getServiceRunning(service):
    try:
        output = subprocess.check_output(['service', service, 'status'])
    except subprocess.CalledProcessError as err:
        output = err.output
    if 'active (running)' in output:
        print("{} is running".format(service))
        return True
    if 'active (exited)' in output:
        print("{} has exited".format(service))
        return False
    if 'inactive (dead)' in output:
        print("{} is dead".format(service))
        return False
    print("{} is unknown".format(service))
    return False

def getServiceInstalled(service):
    try:
        output = subprocess.check_output(['service', service, 'status'])
    except subprocess.CalledProcessError as err:
        if err.returncode == 4:
            print("{} is not installed".format(service))
            return False
        else:
            print("{} is found".format(service))
            return True
    else:
        print("{} is found".format(service))
        return True

def callService(service, command):
    print("Running service {} {}".format(service, command))
    subprocess.call(['sudo', '/usr/sbin/service', service, command])

@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        # It's ugly to have all these logic parts in here, but I don't want unknown posts to be ran
        # as root.
        service = None
        if 'octoprint' in request.form:
            service = 'octoprint'
        elif 'luban' in request.form:
            service = 'luban'
        elif 'lighttpd' in request.form:
            service = 'lighttpd'
        else:
            return "Not Logical"

        if 'Start' == request.form[service]:
            callService(service, 'start')
        elif 'Stop' == request.form[service]:
            callService(service, 'stop')
        elif 'Restart' == request.form[service]:
            callService(service, 'restart')

    return render_template('landingPage.html',
            octoprint_running=getServiceRunning("octoprint"),
            raspap_installed=getServiceInstalled("lighttpd"),
            raspap_running=getServiceRunning("lighttpd"),
            cncjs_running=getServiceRunning("luban"))

