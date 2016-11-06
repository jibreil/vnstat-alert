#!/usr/bin/python

import os
import commands

# limit in GB and conversion to GiB
limitGB = "100"

limitGB = int(limitGB)
limit = limitGB * 0.93
limit = str(limit)

# updating vnStat database
os.system("sudo vnstat -u")

# getting usage data for current monthly period and converting it to a string
used = commands.getstatusoutput("sudo vnstat --oneline | cut -d ';' -f 11")
used = str(used)

# getting usage units
usageunits = used[10:13]

# set units to GiB
units = "GiB"

# getting actual usage value
usage = used[5:9]

# checking usage
if usageunits == units:
    if usage > limit:
        os.system("sudo shutdown")
