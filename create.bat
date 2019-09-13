@echo off
REM calls pyhon file
python mkdir.py %*
REM redirects to djangoProjects folder
@cd Documents/DjangoProjects
REM redirects to new created folder
@cd /d %*