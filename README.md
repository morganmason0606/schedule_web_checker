# schedule_web_checker
Schedule checking a website for changes. Alert user when new change detected. Requires user set up. 

# Setup
Anny command run should be run within 
make sure you have python installed
- run `python --version` and make sure you have atleast python 3.10

make sure you have the requests library installed
- run  `pip install -r requirements.txt` or `pip install requests`

# Running the App 
main.py is the file responsible for managing your websites. Add and delete websites from this app. Make sure the url is the page that will be changing. Also make sure there are no miscellaneous items on the page that you do not want to capture. 
* to run main.py, run `python main.py`

check.py is the file responsible for checking changes to the website. To set up check.py, you need to set up a task.\
# On Windows
you can follow [this link to an example of how to set up a windows task](https://community.esri.com/t5/python-documents/schedule-a-python-script-using-windows-task/ta-p/915861)
* search for the task scheduler app
* on the right, select create a basic task. A window should pop up
* give it a good name and description
* then select how frequently you wish for the app to run
* under action, select start a program
* your program/script should be 'python'
    * alternatively, if you do not want a cmd window to popup, you can instead use the program `pythonw.exe`
* and the argument should be the path provided under the about page in main.py
    * alternatively, right click on check.py and copy the path
* then select finish\
notes:
* make sure to not move these files as that will mess up the task scheduled
* if you want to disable the task, you need to reopen task schedule and cancel your created task
* if you want to manually run check, you can run `python check.py`
