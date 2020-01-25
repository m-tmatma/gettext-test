cd /d %~dp0

setlocal

set PATH=%PATH%;C:\Python38-32\Tools\i18n
compile-po.py

endlocal
