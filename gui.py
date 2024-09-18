import customtkinter

class MyWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.entryStart = customtkinter.CTkEntry(self, placeholder_text="Start Percentage")
        self.entryStart.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.entryStop = customtkinter.CTkEntry(self, placeholder_text="Stop Percentage")
        self.entryStop.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.button = customtkinter.CTkButton(self, text="Set", command=self.on_button_click)
        self.button.place(relx=0.5, rely=0.85, anchor=customtkinter.CENTER)

        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.place(relx=0, rely=1, anchor=customtkinter.SW)
        self.textbox.configure(height = 10, width = 400)

        self.textbox.insert("0.0", "new text to insert")

    
    def on_button_click(self):
        start = self.entryStart.get()
        stop = self.entryStop.get()
            
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0","DONE! - start:" + start + " stop:" + stop)


app = MyWindow()
app.mainloop()
