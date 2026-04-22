import customtkinter as ctk


def build(parent: ctk.CTkScrollableFrame, row: int) -> None:
    font = ctk.CTkFont(parent, size=24, weight='bold')

    ctk.CTkLabel(parent, text='Orçamento', font=font).grid(
        row=row, column=1, columnspan=2, pady=30, padx=10, sticky='ew'
    )
