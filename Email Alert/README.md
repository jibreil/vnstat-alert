# vnStat Alert

## What is it?

This is a simple python script to control data usage by shutting down the machine when a set limit is reached and sends an email alert to the admin.

## Current Version

* Version 1.0
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
2. Change email addresses on Lines 15 and 18 to the email of the sender
3. Change email addresses on Lines 16 and 19 to the email of the recipient of the alert
4. Change `smtp.server.com` on Line 44 to the smtp server provided by your hosting company
5. Add script to `crontab` to run automatically
   * Add `5 * * * * /path/to/script.py` to root crontab (`sudo crontab -e`)
      * Replace the 5 with how often you want the script to check usage in minutes
      * Replace `/path/to/script.py` with the actual path to the script (obviously)

## Comments

* Update and addition of conversion code is because vnStat uses GiB (gibibyte) rather than GB (gigabyte) and 1 GiB is more than 1 GB

## Changelog
