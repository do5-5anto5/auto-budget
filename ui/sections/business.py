import customtkinter as ctk
from database.business import get_business, save_business


def build(parent: ctk.CTkScrollableFrame, start_row: int) -> int:
    """
    Creates the Business section UI in the scrollable frame.
    Loads existing business data from database.
    """
    font = ctk.CTkFont(parent, size=20, weight="bold")

    ctk.CTkLabel(parent, text="Dados da empresa:", font=font).grid(
        row=start_row, column=1, columnspan=2, pady=10, padx=10, sticky="ew"
    )

    # Load existing business data
    business_data = get_business()

    name_entry = ctk.CTkEntry(parent, placeholder_text="Nome da empresa")
    name_entry.grid(row=start_row + 1, column=1, pady=10, padx=10, sticky="ew")
    if business_data["name"]:  # Only insert if there's data
        name_entry.insert(0, business_data["name"])

    phone_entry = ctk.CTkEntry(parent, placeholder_text="WhatsApp da empresa")
    phone_entry.grid(row=start_row + 1, column=2, pady=10, padx=10, sticky="ew")
    if business_data["phone"]:  # Only insert if there's data
        phone_entry.insert(0, business_data["phone"])

    logo_entry = ctk.CTkEntry(parent, placeholder_text="Logo/Sigla da empresa")
    logo_entry.grid(
        row=start_row + 2, column=1, columnspan=2, pady=10, padx=10, sticky="ew"
    )
    if business_data["logo"]:  # Only insert if there's data
        logo_entry.insert(0, business_data["logo"])

    # Store references for data collection
    parent.business_name_entry = name_entry
    parent.business_phone_entry = phone_entry
    parent.business_logo_entry = logo_entry

    # Auto-save functionality
    def _on_field_change(event=None):
        """Auto-save business data when fields change."""
        save_business(
            name=name_entry.get().strip() or None,
            phone=phone_entry.get().strip() or None,
            logo=logo_entry.get().strip() or None
        )
    
    # Bind auto-save to field changes
    name_entry.bind("<FocusOut>", lambda e: _on_field_change())
    phone_entry.bind("<FocusOut>", lambda e: _on_field_change())
    logo_entry.bind("<FocusOut>", lambda e: _on_field_change())
    
    # Also save on Return key
    name_entry.bind("<Return>", lambda e: _on_field_change())
    phone_entry.bind("<Return>", lambda e: _on_field_change())
    logo_entry.bind("<Return>", lambda e: _on_field_change())

    ctk.CTkLabel(parent, text="").grid(row=start_row + 3)
    return start_row + 4
