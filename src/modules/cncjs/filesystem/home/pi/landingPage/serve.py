#!/usr/bin/env python3

import subprocess

from flask import Flask, render_template, request
app = Flask("V1Pi Landing Page")

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
        if 'cncjs' in request.form:
            service = 'cncjs'

        if 'Start' == request.form[service]:
            callService(service, 'start')
        elif 'Stop' == request.form[service]:
            callService(service, 'stop')
        elif 'Restart' == request.form[service]:
            callService(service, 'Restart')

    return render_template('landingPage.html',
            octoprint_running=getServiceRunning("octoprint"),
            cncjs_running=getServiceRunning("cncjs"))

