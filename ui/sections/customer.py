import customtkinter as ctk

def build(parent: ctk.CTkScrollableFrame, start_row:int) -> None:
    font = ctk.CTkFont(parent, size=20, weight='bold')

    ctk.CTkLabel(parent, text='Dados do cliente:', font=font).grid(
        row=start_row, column=1, columnspan=2, pady=10, padx=10, sticky='ew'
    )
    ctk.CTkEntry(parent, placeholder_text='Nome do cliente').grid(
        row=start_row + 1, column=1, pady=10, padx=10, sticky='ew'
    )
    ctk.CTkEntry(parent, placeholder_text='Endereço do cliente').grid(
        row=start_row + 1, column=2, pady=10, padx=10, sticky='ew'
    )
    ctk.CTkLabel(parent, text='').grid(row=start_row + 2)