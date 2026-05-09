import customtkinter as ctk


def build(parent: ctk.CTkScrollableFrame, start_row: int) -> int:
    """
    Creates the Customer section UI in the scrollable frame.
    """
    font = ctk.CTkFont(parent, size=20, weight="bold")

    ctk.CTkLabel(parent, text="Dados do cliente:", font=font).grid(
        row=start_row, column=1, columnspan=2, pady=10, padx=10, sticky="ew"
    )

    name_entry = ctk.CTkEntry(parent, placeholder_text="Nome do cliente")
    name_entry.grid(row=start_row + 1, column=1, pady=10, padx=10, sticky="ew")

    phone_entry = ctk.CTkEntry(parent, placeholder_text="WhatsApp (Ex: 11999998888)")
    phone_entry.grid(row=start_row + 1, column=2, pady=10, padx=10, sticky="ew")

    address_entry = ctk.CTkEntry(parent, placeholder_text="Endereço do cliente")
    address_entry.grid(row=start_row + 2, column=1, columnspan=2, pady=10, padx=10, sticky="ew")

    # Store references for data collection
    parent.customer_name_entry = name_entry
    parent.customer_phone_entry = phone_entry
    parent.customer_address_entry = address_entry

    ctk.CTkLabel(parent, text="").grid(row=start_row + 3)
    return start_row + 4
