cd /d %~dp0

setlocal

set PATH=%PATH%;C:\Program Files\Git\usr\bin
msgmerge.exe  locale\ja_JP\LC_MESSAGES\messages.po locale\messages.pot -o locale\ja_JP\LC_MESSAGES\messages-updated.po

endlocal
