import customtkinter as ctk


def build(parent: ctk.CTkScrollableFrame, start_row: int) -> int:
    """
    Creates the Labor section UI in the scrollable frame.
    """
    font = ctk.CTkFont(parent, size=20, weight='bold')

    ctk.CTkLabel(parent, text='Mão de obra:', font=font).grid(
        row=start_row, column=1, columnspan=2, pady=10, padx=10, sticky='ew'
    )
    
    # Labor inputs frame
    labor_frame = ctk.CTkFrame(parent, fg_color="transparent")
    labor_frame.grid(
        row=start_row + 1, column=1, columnspan=2, padx=10, pady=10, sticky="ew"
    )
    labor_frame.grid_columnconfigure(0, weight=1)
    labor_frame.grid_columnconfigure(1, weight=1)
    labor_frame.grid_columnconfigure(2, weight=1)

    ctk.CTkLabel(labor_frame, text="Preço (R$)").grid(row=0, column=0, sticky="ew")
    ctk.CTkLabel(labor_frame, text="Quantidade").grid(row=0, column=1, sticky="ew")
    ctk.CTkLabel(labor_frame, text="Tipo").grid(row=0, column=2, sticky="ew")

    # Price input with validation
    vcmd = (
        parent.register(
            lambda P: P.replace(".", "", 1).replace(",", "", 1).isdigit() or P == ""
        ),
        "%P",
    )
    price_var = ctk.StringVar()
    price_var.trace_add(
        "write", lambda *args: price_var.set(price_var.get().replace(",", "."))
    )

    price_entry = ctk.CTkEntry(
        labor_frame, textvariable=price_var, validate="key", validatecommand=vcmd
    )
    price_entry.grid(row=1, column=0, padx=(0, 5), sticky="ew")

    qty_entry = ctk.CTkEntry(labor_frame, validate="key", validatecommand=vcmd)
    qty_entry.grid(row=1, column=1, padx=(0, 5), sticky="ew")

    # Billing method dropdown
    billing_methods = ["m²", "dia", "unidade"]
    billing_combo = ctk.CTkComboBox(labor_frame, values=billing_methods)
    billing_combo.set("m²")
    billing_combo.grid(row=1, column=2, sticky="ew")

    # Store references for data collection
    parent.labor_price_entry = price_entry
    parent.labor_qty_entry = qty_entry
    parent.labor_billing_combo = billing_combo

    ctk.CTkLabel(parent, text='').grid(row=start_row + 2)
    return start_row + 3
