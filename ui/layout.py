import customtkinter as ctk
from ui.sections import materials
from ui.sections import business
from ui.sections import customer
from ui.sections import header


def build_app() -> ctk.CTk:
    """
    Join sections and build the application layout.
    """
    app = ctk.CTk()
    app.title('Auto Budget')
    app.geometry('600x700')

    scroll_frame = ctk.CTkScrollableFrame(app)
    scroll_frame.pack(fill='both', expand=True)
    scroll_frame.grid_columnconfigure(0, weight=1)
    scroll_frame.grid_columnconfigure(1, weight=4)
    scroll_frame.grid_columnconfigure(2, weight=4)
    scroll_frame.grid_columnconfigure(3, weight=1)

    header.build(scroll_frame, row=0)
    business.build(scroll_frame, start_row=1)
    customer.build(scroll_frame, start_row=4)
    materials.build(scroll_frame, start_row=7)

    return app
