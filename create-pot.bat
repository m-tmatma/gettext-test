cd /d %~dp0

setlocal

set PATH=%PATH%;C:\Python38-32\Tools\i18n
pygettext.py -d messages -p locale script\app.py

endlocal
