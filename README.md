# Anfisa for Friends

## Environment Setup
### Clone the Anfisa for Friends project into the *Dev/* directory.

The resulting structure should look like this:

```
Dev/
 └── anfisa1sprint/
     ├── anfisa_for_friends/
     ├── html_templates/
     ├── .gitignore
     ├── LICENSE
     ├── requirements.txt
     └── README.md
```

### Create a Virtual Environment

1. Open Visual Studio Code and use *File / Open Folder* to open the *Dev/anfisa1sprint/* directory.
2. Open the terminal in VS Code, make sure you are working from the *anfisa1sprint/* directory, and run the command below. If you are using Windows, make sure the terminal is running Git Bash rather than PowerShell or another shell.
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
This will create a virtual environment in the *anfisa1sprint/* directory and add a `venv` folder containing all project dependencies. The structure will look like this:

```

Dev/
└── anfisa1sprint/
    ├── anfisa_for_friends/
    ├── html_templates/
    ├── venv/   
    ├── .gitignore
    ├── LICENSE
    ├── requirements.txt
    └── README.md
```

### Activate the Virtual Environment
In the terminal, go to the project root directory *Dev/anfisa1sprint/* and run:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

After activation, all terminal commands will be prefixed with `(venv)`.

All subsequent terminal commands should be run with the virtual environment activated.

Upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

### Install Dependencies from *requirements.txt*
From the *Dev/anfisa1sprint/* directory, run:

```bash
pip install -r requirements.txt
```

### Apply Migrations

From the directory containing `manage.py`, run:

```bash
python manage.py migrate
```

### Run the Project in Development Mode

From the directory containing `manage.py`, run:

```bash
python manage.py runserver
```

Django will report that the server is running and the project is available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
