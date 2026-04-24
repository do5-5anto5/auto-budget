import customtkinter as ctk


def build(parent: ctk.CTkScrollableFrame, start_row: int) -> int:
    """
    Creates the Business section UI in the scrollable frame.
    """
    font = ctk.CTkFont(parent, size=20, weight="bold")

    ctk.CTkLabel(parent, text="Dados da empresa:", font=font).grid(
        row=start_row, column=1, columnspan=2, pady=10, padx=10, sticky="ew"
    )

    name_entry = ctk.CTkEntry(parent, placeholder_text="Nome da empresa")
    name_entry.grid(row=start_row + 1, column=1, pady=10, padx=10, sticky="ew")

    phone_entry = ctk.CTkEntry(parent, placeholder_text="WhatsApp da empresa")
    phone_entry.grid(row=start_row + 1, column=2, pady=10, padx=10, sticky="ew")

    logo_entry = ctk.CTkEntry(parent, placeholder_text="Logo/Sigla da empresa")
    logo_entry.grid(
        row=start_row + 2, column=1, columnspan=2, pady=10, padx=10, sticky="ew"
    )

    # Store references for data collection
    parent.business_name_entry = name_entry
    parent.business_phone_entry = phone_entry
    parent.business_logo_entry = logo_entry

    ctk.CTkLabel(parent, text="").grid(row=start_row + 3)
    return start_row + 4
