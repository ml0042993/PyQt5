echo off
rem 将子目录QtApp下的.ui文件复制到当前目录下,并编译
copy .\QtApp\Widget.ui Widget.ui
pyuic5 -o ui_Widget.py Widget.ui

rem 编译并复制资源文件

pyrcc5 .\QtApp\res.qrc -o res_rc.py