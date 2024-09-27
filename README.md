# Battery Threshold GUI
Simple Python GUI to change start and stop charging threshold in SMAPI compatible batteries.  

![image](https://github.com/user-attachments/assets/6638d3ef-16f3-4ec0-aff3-c97221edfbb2)  

## Setup (LINUX)
- make sure to have python3 and python3-venv installed
- clone the repo to the desired installation folder
- create a virtual enviroment inside the installation folder using `python3 -m venv /desired/location/folder`
- activate the venv `source bin/activate`
- `pip3 install pynput`
- `pip3 install customtkinter`

You are now good to go. If you run the main.py while in the venv with sudo you can use the GUI correctly.

## Create a shortcut
The last step to have easy access to the utility is to modify the given `start` file to run the program with the correct privileges.
You can modify the file by:
- modfiy the first path to your venv activate file
- modify the second path to your `main.py` file

The last step is to create a .desktop file and placing it in `/.local/share/applications`. You can do so by using Menu Libre or by hand.
.desktop template:
```
[Desktop Entry]
Version=1.1
Type=Application
Name=Battery Threshold
Icon=battery-level-10-symbolic
Exec=/home/.../src/start %f
Path=/home/...
Actions=
Categories=HardwareSettings;X-GNOME-Other;
```

