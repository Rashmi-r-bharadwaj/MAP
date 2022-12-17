import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def _init_(self):
        super()._init_()

       
        self.title("Event Manager")
        self.geometry(f"{500}x{250}")
        
        self.main_mail = customtkinter.CTkButton(master=self,text='Mail' , border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_mail.place(x=90,y=80)
        self.main_whatsapp = customtkinter.CTkButton(master=self,text='Whatsapp',bg_color='red',hover_color='green', border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_whatsapp.place(x=265,y=80)
        
        
    def sidebar_button_event(self):
        print("sidebar_button click")

if _name_ == "_main_":
    app = App()
    app.mainloop()