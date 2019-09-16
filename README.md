# "PythonAutomation" 
### Script to help using only one line to create new project directory and necessary files to quick and easy start new project. Additionally to that it will automatically login to GitHub account and will initial new repository, submit changes and automatically push files to new created repo.

#### In my case to start new Django project i will use windows terminal and default location so all my created files will go to this directory. 
``` 
C:\Users\Ignas>
```
## To do list:
- [x] Create CMD file to call Python script
- [x] Create variable folder name
- [x] Make new folder in set location
- [x] Redirect to new created folder
- [x] Call Web browser
- [x] Navigate to GitHub account and login
- [x] Create new Repository
- [ ] Push Files to Git

## Execution 
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
7. To fill the login/password information you need to use ***chrome developer tools*** to find login/password field. Click on the login field right mouse button and select ***inspect*** *[reference image](https://github.com/ignasgri/PythonAutomation/blob/master/images/loginInspect.jpg)*. Copy  id=" ***loginfield*** " *[reference image](https://github.com/ignasgri/PythonAutomation/blob/master/images/loginField.jpg)* to your code. To target id element use command ***find_element_by_id()***

> mkdir.py
```
login = driver.find_element_by_id('login_field')
```
8. To send your login information to the browser use command ***send.keys()***
>mkdir.py
```
login.send_keys("your github login")
```
9. Repeat process for password as shown in *point no. 7 and 8* 
> mkdir.py
```
login = driver.find_element_by_id('password')
login.send_keys("your github password")
```
10. To locate ***sign in*** button you need use ***find_elements_by_xpath()***
>mkdir.py
```
submit_button = driver.find_elements_by_xpath()
```

11. To get xPath you need to click right mouse button on ***sign in*** button and using ***chrome developer tools*** copy and paste xPath to your code
*[reference image](https://github.com/ignasgri/PythonAutomation/blob/master/images/xPath.jpg)*

>mkdir.py
```
submit_button = driver.find_elements_by_xpath('//*[@id="login"]/form/div[3]/input[7]')[0]
```
12. To submit all your credentials use command ***click()***
> mkdir.py
```
submit_button.click()
```
13. After you login to GitHub you need to create new repository. Repeat *point no. 11 and 12* just this time you need to get xPath for ***New*** button
```
new_repo_button = driver.find_elements_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div/div/h2/a")[0]

new_repo_button.click()
```
14. Automatically input repo name you need to use ***folderName***. So your project name will update your repository name. To get input field information use  ***find_element_by_id*** as shown in *point no.7* and to send information to fill the filed use ***send_keys()*** command *[reference image](https://github.com/ignasgri/PythonAutomation/blob/master/images/repoName.jpg)*
```
repo_name = driver.find_element_by_id('repository_name')

repo_name.send_keys(folderName)
```
15. Repository name to validate by GitHub takes less then a second so we need to delay process between the repository name was automatically filled in and clicking the button ***Create repository*** [reference image](https://github.com/ignasgri/PythonAutomation/blob/master/images/createRepository.jpg). To delay process we need to import *sleep* library. This need to be placed in top of your code.
```
from time import sleep
```
16. Firstly you need to  add sleep function ***sleep(1)*** and specify for how long we need to sleep (*in this case is one second*) this need to be placed above ***create_repo_button*** as shown in code sample below. 
Secondly to create repository repeat process as shown in *point no. 11*

```
sleep (1)

create_repo_button = driver.find_elements_by_xpath('//*[@id="new_repository"]/div[3]/button')[0]
create_repo_button.click()
```