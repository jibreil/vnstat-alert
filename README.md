# vnStat Alert

## What is it?

This is a simple python script to control data usage using a set limit, the script executes the command `sudo shutdown` when the limit is reached and the email version sends an email alert before shutting down the machine.

## Current Version

* Version 3.0
* Released 07/05/2016

## Requirements

* vnStat

## vnStat Configuration

1. Edit `/etc/vnstat.conf`
   * Change `MonthRotate` on line 10 to start date of billing period (1-28)
2. Setup vnStat monitoring
   * `sudo vnstat -u -i eth0`
      * Replace eth0 with network interface to be monitored, the command `vnstat --iflist` will show all available network interfaces
3. Start the vnStat daemon and set to run on boot
   * `sudo vnstatd -d`
   * Add `vnstat -d` above `exit 0` line in `/etc/rc.local`

## Script Configuration

1. Change the number on Line 7 to the usage limit in GB (whole numbers only)
2. Add script to `crontab` to run automatically
   * Add `5 * * * * /path/to/script.py` to root crontab (`sudo crontab -e`)
      * Replace the 5 with how often you want the script to check usage in minutes
      * Replace `/path/to/script.py` with the actual path to the script (obviously)

## Comments

* Update and addition of conversion code is because vnStat uses GiB (gibibyte) rather than GB (gigabyte) and 1 GiB is more than 1 GB

## Changelog

#### Version 2.0 (05/05/2016)

* Completely changed how script retrieves usage data

#### Version 2.1 (06/05/2016)

* Added conversion from GB to GiB within the script for more accuracy
* Added units checking for MiB and GiB

#### Version 3.0 (07/05/2016)

* Cleanup and new README
* Email capable version of script added
