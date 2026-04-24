import customtkinter as ctk
from database.business import get_business, save_business
from ui.components.logo_upload import create_logo_upload_frame


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

    # Create logo upload frame instead of text entry
    def on_logo_update(base64_str):
        """Handle logo update callback"""
        parent.temp_logo_image = base64_str
        _on_field_change()
    
    logo_frame, logo_label = create_logo_upload_frame(
        parent, start_row + 2, 1, business_data.get("logo_image"), on_logo_update
    )
    logo_frame.grid(row=start_row + 2, column=1, columnspan=2, pady=10, padx=10, sticky="ew")

    # Store references for data collection
    parent.business_name_entry = name_entry
    parent.business_phone_entry = phone_entry
    parent.business_logo_label = logo_label

    # Auto-save functionality
    def _on_field_change(event=None):
        """Auto-save business data when fields change."""
        logo_image = getattr(parent, 'temp_logo_image', business_data.get('logo_image'))
        save_business(
            name=name_entry.get().strip() or None,
            phone=phone_entry.get().strip() or None,
            logo=None,  # Keep old logo text for compatibility
            logo_image=logo_image or None
        )
    
    # Bind auto-save to field changes
    name_entry.bind("<FocusOut>", lambda e: _on_field_change())
    phone_entry.bind("<FocusOut>", lambda e: _on_field_change())
    
    # Also save on Return key
    name_entry.bind("<Return>", lambda e: _on_field_change())
    phone_entry.bind("<Return>", lambda e: _on_field_change())

    ctk.CTkLabel(parent, text="").grid(row=start_row + 3)
    return start_row + 4
