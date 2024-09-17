import customtkinter

class MyWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.entryStart = customtkinter.CTkEntry(self, placeholder_text="Start Percentage")
        self.entryStart.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.entryStop = customtkinter.CTkEntry(self, placeholder_text="Stop Percentage")
        self.entryStop.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.button = customtkinter.CTkButton(self, text="Click me", command=self.on_button_click)
        self.button.place(relx=0.5, rely=0.85, anchor=customtkinter.CENTER)

    
    def on_button_click(self):
        start = self.entryStart.get()
        stop = self.entryStop.get()
        
        print(start + stop)


app = MyWindow()
app.mainloop()
