import customtkinter as ctk
from ui.sections import materials
from ui.sections import business
from ui.sections import customer
from ui.sections import header
from ui.sections import labor
from logic.data_collector import generate_budget_pdf


def build_app() -> ctk.CTk:
    """
    Join sections and build the application layout with scrollable content and fixed bottom button.
    """
    app = ctk.CTk()
    app.title('Auto Budget')
    app.geometry('600x700')
    
    # Main container
    main_frame = ctk.CTkFrame(app, fg_color="transparent")
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Scrollable content area
    scroll_frame = ctk.CTkScrollableFrame(main_frame)
    scroll_frame.pack(fill='both', expand=True)
    scroll_frame.grid_columnconfigure(0, weight=1)
    scroll_frame.grid_columnconfigure(1, weight=4)
    scroll_frame.grid_columnconfigure(2, weight=4)
    scroll_frame.grid_columnconfigure(3, weight=1)

    # Build all sections
    current_row = 0
    current_row = header.build(scroll_frame, row=current_row)
    current_row = business.build(scroll_frame, start_row=current_row)
    current_row = customer.build(scroll_frame, start_row=current_row)
    current_row = labor.build(scroll_frame, start_row=current_row)
    current_row = materials.build(scroll_frame, start_row=current_row)

    # Fixed bottom button frame
    button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    button_frame.pack(fill='x', pady=(10, 0))
    
    # Generate PDF button
    generate_button = ctk.CTkButton(
        button_frame,
        text="Gerar PDF de Orçamento",
        font=ctk.CTkFont(size=16, weight="bold"),
        height=40,
        command=lambda: generate_budget_pdf(scroll_frame)
    )
    generate_button.pack(fill='x', padx=20, pady=5)

    return app
