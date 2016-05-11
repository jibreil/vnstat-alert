#!/usr/bin/python

import os
import commands
import smtplib

#limit in GB and conversion to GiB
limitGB = "100"

limitGB = int(limitGB)
limit = limitGB * 0.93
limit = str(limit)

#email settings
sender = 'sender@senderdomain.com'
receivers = ['to@todomain.com']

message = """From: Sender <sender@senderdomain.com>
To: Receiver <to@todomain.com>
Subject: Bandwidth Usage Limit Reached

Bandwidth usage limit has been reached and the machine will commence shutdown
"""

#updating vnStat database
os.system("sudo vnstat -u")

#getting usage data for current monthly period and converting it to a string
used = commands.getstatusoutput("sudo vnstat --oneline | cut -d ';' -f 11")
used =str(used)

#getting usage units
usageunits = used[10:13]

#set units to GiB
units = "GiB"

#getting actual usage value
usage = used[5:9]

#checking usage
if usageunits == units:
    if usage > limit:
        smtpObj = smtplib.SMTP('smtp.server.com')
        smtpObj.sendmail(sender, receivers, message)
        os.system("sudo shutdown")