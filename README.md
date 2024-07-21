# py_data_structures

Complete project of Data Structures with the Python Programming Language - Front-End Back-End.

### How to Run

#### Termux (Android):
1. Open the Termux app.
2. Run the following commands to clone the repository, create and activate a virtual environment, install SQLite, install Tkinter, and enter the directory:
   ```bash
   pkg install git
   pkg install python
   pkg install python2
   pkg install python3
   pkg install sqlite3
   pkg install tcl
   pkg install tk
   git clone https://github.com/your_username/py_data_structures.git
   cd py_data_structures
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install VNC Server and Configure XFCE4**:
   - **Install Termux and Update Packages**:
     ```bash
     pkg update && pkg upgrade
     ```
   - **Install VNC Server and XFCE4**:
     ```bash
     pkg install x11-repo
     pkg install tigervnc xfce4 xfce4-terminal
     ```
   - **Configure XFCE4 Environment**:
     Create and edit the initialization script:
     ```bash
     mkdir -p ~/.vnc
     vi ~/.vnc/xstartup
     ```
     In the `vi` editor:
     1. Press `i` to enter insertion mode.
     2. Add the following content:
        ```bash
        #!/data/data/com.termux/files/usr/bin/sh
        xfce4-session &
        ```
     3. Press `Esc`, then type `:wq` and press `Enter` to save and exit.
     - **Make the Script Executable**:
       ```bash
       chmod +x ~/.vnc/xstartup
       ```
     - **Start VNC Server**:
       ```bash
       export ID=:1
       vncserver $ID -localhost
       ```
       Follow the prompts to set a secure password.
     - **Configure VNC Screen Resolution (Optional)**:
       Stop the VNC Server if running:
       ```bash
       vncserver -kill :1
       ```
       Restart with desired resolution:
       ```bash
       vncserver :1 -localhost -geometry 1280x720
       ```
     - **Connect to VNC Server**:
       Install a VNC Viewer app (e.g., VNC Viewer from the Google Play Store), and connect to `localhost:1` with the password you set.

4. Navigate to the directory where the file is located.
5. Execute the Python file using the command:
   ```bash
   python filename.py
   ```

#### Windows:
1. Open the Command Prompt (cmd).
2. Navigate to the directory where the file is located.
3. Run the following commands to clone the repository, create and activate a virtual environment, install SQLite, and install Tkinter:
   ```bash
   git clone https://github.com/Hatoridev/py_estrutura_dados.git
   cd py_estrutura_dados
   python -m venv venv
   venv\Scripts\activate
   pip install tk
   ```

4. Execute the Python file using the command:
   ```bash
   python filename.py
   ```

#### Debian/Linux:
1. Open the terminal.
2. Run the following commands to clone the repository, create and activate a virtual environment, install SQLite, install Tkinter, and enter the directory:
   ```bash
   sudo apt update && sudo apt upgrade
   sudo apt install git
   sudo apt install python3-venv
   sudo apt install sqlite3
   sudo apt install python3-tk
   git clone https://github.com/Hatoridev/py_estrutura_dados.git
   cd py_estrutura_dados
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

#### Additional Steps for Termux (Android):
To use PyInstaller in Termux, you need to install additional packages:

1. Open the Termux app.
2. Run the following commands:
   ```bash
   pkg install ldd
   pkg install binutils
   pip install pyinstaller
   ```

Then, navigate to your project directory and run the following command to create the executable:

```bash
pyinstaller --onefile filename.py
```

## Language

 <div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="60" alt="python logo"  />
</div>

## Library

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tkinter/tkinter-original.svg" height="60" alt="tkinter logo" />
</div>

---
