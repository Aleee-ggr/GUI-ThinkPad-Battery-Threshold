import gui

if __name__ == "__main__":
    app = gui.MyWindow()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
