# Setup prototype in Pycharm
This guide specifies how to setup this project in Pycharm development environment.

### Prerequisite: install python3
  - we recommend installing homebrew to manage software, go to "https://brew.sh/", download the lastest version of homebrew;
  - if you donot have python3, install by executing "brew install python3"

### Get project and pycharm settings
  - cd to your workspace in CMD, clone down this repository;
  - open a new project in Pycharm, select the folder "mp-prototype" you just cloned down and go forward then the project will be imported;
  - Open Pycharm Preference, set the "Project Interpreter" to your installed python3; click "Django" under "Language & Frameworks", enable "Enable Django Support", set "settings" to "prototype/settings.py"; click "Apply" and "OK";
  - You will get reminder from Pycharm to install django packages (if not, open the project folder in Pycharm navigator and open one file such as manage.py), install all packages(you may be required to provide your system user password during installation).
  - If error occurs regarding to installing some packages, then install it from your CMD by executing "sudo -u your_username pip install XXX==X.X.X";

### Run configuration
- Click "Run" in Pycharm menu, select "Edit configuration"
- Click "+", select "Django Server", input "0.0.0.0" in Host, click Apply and OK
- Run the project by clicking the Green Triangle, then you can open your browser and go to "http://0.0.0.0:8000/" to see our web page

### Note:
The launching process of the application will be very slow since machine-learning models will be loaded, which are very large because of the large vocabulary learnt.
