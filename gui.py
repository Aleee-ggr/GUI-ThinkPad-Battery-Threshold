import customtkinter
from modify import Modify

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

        self.setupFeedbackText()

    
    def on_button_click(self):
        start = self.entryStart.get()
        stop = self.entryStop.get()
        if(start == "" or stop == "" or 
           not start.isdigit() or not stop.isdigit() or 
           int(start) >= int(stop) or int(start) < 0 or int(stop) > 100):
            self.textbox.delete("0.0", "end")
            self.textbox.insert("0.0","Please enter valid values")
            return
        
        self.textbox.delete("0.0", "end")
        Modify(start, stop)
        self.textbox.insert("0.0","DONE! - start:" + start + " stop:" + stop)

    
    def setupFeedbackText(self):
        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.place(relx=0, rely=1, anchor=customtkinter.SW)
        self.textbox.configure(height = 10, width = 400)
        self.textbox.insert("0.0", "insert values and click set")




app = MyWindow()
app.mainloop()
