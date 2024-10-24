# Welcome to the amaltools.com repository

The entire code behind amaltools.com has been made publically available so that you too can run your very own amaltools!
Here is the link to a YouTube video on how to run it [https://www.youtube.com/watch?v=Vn75FxOYF9A](https://www.youtube.com/watch?v=Vn75FxOYF9A)

## How to run it

### Before you can run this you'll need 
- to have python version > 3.10 installed on your computer
- a computer
- some knowledge on how to navigate your operating systems cli
- PowerShell if you are using a windows pc

All paths, folders and file names can be named as you wished however the instructions below already have paths to make this guide simpler
### Let's begin

Download the zip file of the project or clone the repository (if you know how to)
If you downloaded the zip file you then need to extract it and go to the resulting folder in a command line or preferably open it in a code editor such as VS Code.

Although these next few steps are optional I recommend you follow them so as not to pollute your global environment with specific versions of libraries and their dependencies.

Create a virtual environment
For windows:
```powershell
py -m venv .venv
```
For Linux & MacOS:
```bash
python -m venv .venv
```

Then you need to enter the virtual environment
For windows:
```powershell
.venv/Scripts/Activate.ps1
```
For Linux & MacOS:
```bash
source .venv/bin/activate
```

Next you need to install the python libraries the project requires to work, quite a lot of libraries are only required for certain tools (remove as you wish) others are required for multiple. The main ones are Django and its dependencies.

To install the libraries run
For windows and Linux & MacOS:
```powershell
pip install -r dev_requirements.txt
```

This command will take some time to complete depending on your network download speed.

The next steps are very crucial to getting amaltools.com in the state it was in before it was shut down, these steps work with databases and may be prone to error so follow closely.
For windows :
```powershell
py manage.py loaddata db_data.json
```

For Linux & MacOS:
```bash
python manage.py loaddata db_data.json
```

Now all you need to do is start up the server and you are done
