import gui
import subprocess


def check_sudo():
    try:
        subprocess.run(["pkexec", "-v"], check=True)
    except subprocess.CalledProcessError:
        return False
    return True


if __name__ == "__main__":

    if not check_sudo():
        print("This script needs sudo privileges to run")

    app = gui.MyWindow()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
