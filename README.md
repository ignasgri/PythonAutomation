# "PythonAutomation" 
#### Script to help using only one line to create new project directory and necessary files to quick and easy start new project. Additionally to that it will automatically login to GitHub account and will initial new repository, submit changes and automatically push files to new created repo.

### In my case to start new Django project i will use windows terminal and default location so all my created files will go to this directory. 
``` 
C:\Users\Ignas>
```
> To do list:
- [x] Create CMD file to call Python script
- [x] Create variable folder name
- [x] Make new folder in set location
- [x] Redirect to new created folder
- [x] Call Web browser
- [ ] Navigate to GitHub account and login
- [ ] Create new Repository
- [ ] Push Files to Git

>Execution 
1. Call Python script from (CMD) Command Prompt
> create.bat
```
@echo off
python mkdir.py %*
```
<!-- 1.1 Import 
```
import os
import sys
``` -->

2. Create variable file name using (CMD) Command Prompt
> mkdir.py
```
folderName = str(sys.argv[1])
```
3. Create project folder in set location
> mkdir.py
```
os.mkdir(("C:/Users/Ignas/Documents/DjangoProjects/") + folderName)
```
4. Set path to your project folder 
> create.bat
```
@cd Documents/DjangoProjects
@cd /d %*
```
5. To call browser we need to pip install selenium and download webdriver for your browser (Chrome Version 76.0.3809.132 (Official Build) (64-bit))
- pip install selenium
- Web driver <https://chromedriver.chromium.org/downloads>
> mkdir.py
```
import selenium
from selenium import webdriver
```
6. Set webdriver to use chrome web browser
> mkdir.py
```
driver = webdriver.Chrome()
```