# "PythonAutomation" 
#### Script to help using only one line to create new project directory and necessary files to quick and easy start new project. Additionally to that it will automatically login to GitHub account and will initial new repository, submit changes and automatically push files to new created repo.

> To do list:
- [x] Create CMD file to call Python script
- [x] Create variable folder name
- [x] Create path so projects location
- [x] Create function to redirect to set location
- [x] Make new folder in set location
- [ ] Redirect to new created folder
- [ ] Call Web browser
- [ ] Navigate to GitHub account and login
- [ ] Create new Repository
- [ ] Push Files to Git

>Execution 
1. Call Python script from (CMD) Command Prompt
```
@echo off
python mkdir.py %*
```
2. Create variable file name using (CMD) Command Prompt
```
folderName = str(sys.argv[1])
```
3. Set project location
```
path = (r'C:\\Users\Ignas\Documents\\')
```
4. Function to point to your set location (point no.3)
```
def makedirectory():
        os.chdir(path) 
if __name__ == '__main__':
    makedirectory()
```
5. Create project folder in set location
```
os.mkdir(path + folderName)
```
<!-- 5. Create project folder in set location
```

``` -->
<!-- 5. Create project folder in set location
```

``` -->