# RPI4-4x1-button-membrane-zrx-543

Simple script allowing Raspberry pi 4 to recognise which button is pressed, whilst preventing duplicate requests for actions if connected to 3v.

Status:
README: - Work in progress - 05/07/2022
Code: - Adequate - 05/07/2022

Setup:
TBC - 05/07/2022

*Known issue*

Default options on Raspberry PI 4 would increase the log and kernel file significantly when script runs.
This can result in Raspberry PI 4 being unable to login (press CTRL+ALT+F6)
  To validate enter df -h (and check if the /dev/root location uses 100%)
  If /dev/root is 100%, as root, remove the following files
    - syslog.1, kern.log.1

There are 3 options to explore:
- Manually remove the file and restart the service (not great) - to be explained further
- Configure logrotate to limit log file size (still can happen as this is done once a day) - to be explained further
- Configure regular cleansing - to be explained further
