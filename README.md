# py_data_structures

Complete project of Data Structures with the Python Programming Language - Front-End Back-End.

### How to Run

#### Termux (Android):
1. Open the Termux app.
2. Run the following commands to clone the repository, create and activate a virtual environment, install SQLite, and enter the directory:
   ```bash
   pkg install git
   pkg install python
   pkg install python2
   pkg install python3
   pkg install sqlite3
   git clone https://github.com/your_username/py_data_structures.git
   cd py_data_structures
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Navigate to the directory where the file is located.
4. Execute the Python file using the command:
   ```bash
   python filename.py
   ```

#### Windows:
1. Open the Command Prompt (cmd).
2. Navigate to the directory where the file is located.
3. Run the following commands to clone the repository, create and activate a virtual environment, and install SQLite:
   ```bash
   git clone https://github.com/your_username/py_data_structures.git
   cd py_data_structures
   python -m venv venv
   venv\Scripts\activate
   ```

4. Execute the Python file using the command:
   ```bash
   python filename.py
   ```

#### Debian/Linux:
1. Open the terminal.
2. Run the following commands to clone the repository, create and activate a virtual environment, install SQLite, and enter the directory:
   ```bash
   sudo apt update && sudo apt upgrade
   sudo apt install git
   sudo apt install python3-venv
   sudo apt install sqlite3
   git clone https://github.com/your_username/py_data_structures.git
   cd py_data_structures
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Navigate to the directory where the file is located.
4. Execute the Python file using the command:
   ```bash
   python filename.py
   ```

### How to Convert to Executable:

You can use PyInstaller to convert your Python scripts into executable files. Install PyInstaller with the following command:

```bash
pip install pyinstaller
```

Then, navigate to your project directory and run the following command to create the executable:

```bash
pyinstaller --onefile filename.py
```

This will create an executable in the `dist` folder of your project.
