import customtkinter as ctk
from ui.layout import build_app

ctk.set_appearance_mode('dark')

if __name__ == '__main__':
    app = build_app()
    app.mainloop()