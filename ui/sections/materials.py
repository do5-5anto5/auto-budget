import customtkinter as ctk
import state
from database.materials import insert_material, get_materials, remove_material

TABLE_ROW_OFFSET = 2  # 0 = header, 1 = divider, 2+ = data


def build(parent: ctk.CTkScrollableFrame, start_row: int) -> int:
    """
    Creates the Materials section UI in the scrollable frame, including inputs and a dynamic table.
    """
    section_font = ctk.CTkFont(parent, size=20, weight="bold")
    header_font = ctk.CTkFont(parent, size=13, weight="bold")

    # ── Title ─────────────────────────────────────────────────────────────────
    ctk.CTkLabel(parent, text="Materiais:", font=section_font).grid(
        row=start_row, column=1, columnspan=2, pady=10, padx=10
    )

    # ── Helper functions for dropdown ────────────────────────────────────────
    def refresh_dropdown():
        """Refresh the dropdown with materials from database."""
        materials = get_materials()
        materials_combo.configure(values=materials)
    
    def _on_material_selected(selected):
        """Handle material selection from dropdown."""
        if selected:
            material_entry.delete(0, "end")
            material_entry.insert(0, selected)
    
    def _delete_selected_material(materials_var, materials_combo):
        """Delete the selected material from database."""
        selected = materials_var.get()
        if selected:
            result = remove_material(selected)
            print(result)
            refresh_dropdown()
            materials_var.set("")  # Clear selection

    # ── Dropdown for saved materials ────────────────────────────────────────
    dropdown_frame = ctk.CTkFrame(parent, fg_color="transparent")
    dropdown_frame.grid(
        row=start_row + 1, column=1, columnspan=2, padx=10, pady=(5, 10), sticky="ew"
    )
    dropdown_frame.grid_columnconfigure(0, weight=1)
    dropdown_frame.grid_columnconfigure(1, weight=0)

    # Create dropdown combobox
    materials_var = ctk.StringVar()
    materials_combo = ctk.CTkComboBox(
        dropdown_frame, 
        variable=materials_var,
        values=[],
        command=lambda selected: _on_material_selected(selected)
    )
    materials_combo.set("Selecione um material salvo...")  # Placeholder
    materials_combo.grid(row=0, column=0, sticky="ew", padx=(0, 5))
    
    # Delete button for selected material
    delete_btn = ctk.CTkButton(
        dropdown_frame,
        text="🗑️ Excluir",
        width=80,
        fg_color="#8B0000",
        hover_color="#B22222",
        command=lambda: _delete_selected_material(materials_var, materials_combo)
    )
    delete_btn.grid(row=0, column=1)

    # ── Sub-frame inputs ───────────────────────────────────────────────────
    inputs_frame = ctk.CTkFrame(parent, fg_color="transparent")
    inputs_frame.grid(
        row=start_row + 2, column=1, columnspan=2, padx=10, pady=10, sticky="ew"
    )
    inputs_frame.grid_columnconfigure(0, weight=1)
    inputs_frame.grid_columnconfigure(1, weight=1)
    inputs_frame.grid_columnconfigure(2, weight=1)

    ctk.CTkLabel(inputs_frame, text="Material").grid(row=0, column=0, sticky="ew")
    ctk.CTkLabel(inputs_frame, text="Preço (ex: 99.99)").grid(
        row=0, column=1, sticky="ew"
    )
    ctk.CTkLabel(inputs_frame, text="Quantidade").grid(row=0, column=2, sticky="ew")

    material_entry = ctk.CTkEntry(inputs_frame)
    material_entry.grid(row=1, column=0, padx=(0, 5), sticky="ew")

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
        inputs_frame, textvariable=price_var, validate="key", validatecommand=vcmd
    )
    price_entry.grid(row=1, column=1, padx=(0, 5), sticky="ew")

    qty_entry = ctk.CTkEntry(inputs_frame, validate="key", validatecommand=vcmd)
    qty_entry.grid(row=1, column=2, sticky="ew")

    
    def _on_add():
        """
        Adds a new material to the materials list and database.

        Retrieves values from input fields, validates them, and adds a new material
        to the state. Saves to database if name is provided. Clears input fields 
        and refreshes the table after successful addition.

        Validates name, price, and quantity are provided.
        Calls state.add_material(name, float(price_raw), int(qty_raw)).
        Saves material name to database.
        Clears inputs and refreshes the table display.
        """
        name = material_entry.get().strip()
        price_raw = price_entry.get().strip()
        qty_raw = qty_entry.get().strip()
        if not name or not price_raw or not qty_raw:
            return
        
        # Save to database
        insert_material(name)
        
        # Add to state
        state.add_material(name, float(price_raw), int(qty_raw))
        material_entry.delete(0, "end")
        price_var.set("")
        qty_entry.delete(0, "end")
        refresh_table()
        refresh_dropdown()


    # ── Add Button ─────────────────────────────────────────────────────────────
    ctk.CTkButton(parent, text="Adicionar material", width=200, command=_on_add).grid(
        row=start_row + 3, column=1, columnspan=2, pady=(8, 0)
    )

    # ── Scrollable Table ─────────────────────────────────────────────────────
    scrollable_table_frame = ctk.CTkScrollableFrame(parent, height=120)
    scrollable_table_frame.grid(
        row=start_row + 4, column=1, columnspan=2, padx=10, pady=(10, 0), sticky="ew"
    )
    scrollable_table_frame.grid_columnconfigure(0, weight=3)
    scrollable_table_frame.grid_columnconfigure(1, weight=1)
    scrollable_table_frame.grid_columnconfigure(2, weight=2)
    scrollable_table_frame.grid_columnconfigure(3, weight=2)
    scrollable_table_frame.grid_columnconfigure(4, weight=1)

    # Table headers inside scrollable frame
    for col, text in enumerate(["Material", "Qtd", "Unit. (R$)", "Subtotal (R$)", ""]):
        ctk.CTkLabel(scrollable_table_frame, text=text, font=header_font).grid(
            row=0, column=col, padx=6, pady=(6, 2), sticky="ew"
        )
    ctk.CTkFrame(scrollable_table_frame, height=1, fg_color="gray50").grid(
        row=1, column=0, columnspan=5, sticky="ew", padx=4
    )

    def refresh_table():
        """
        Rebuilds the materials table UI from state data in the Materials section.
        Clears existing rows beyond header offset.
        Repopulates rows from state.materials_data with name, qty, price, subtotal, and remove button.
        Updates the total row with state.get_total() after refresh.
        """
        for widget in scrollable_table_frame.winfo_children():
            info = widget.grid_info()
            if info and int(info["row"]) >= TABLE_ROW_OFFSET:
                widget.destroy()

        for i, item in enumerate(state.materials_data):
            row = TABLE_ROW_OFFSET + i
            ctk.CTkLabel(scrollable_table_frame, text=item["name"], anchor="w").grid(
                row=row, column=0, padx=6, pady=2, sticky="ew"
            )
            ctk.CTkLabel(scrollable_table_frame, text=str(item["qty"])).grid(
                row=row, column=1, padx=6, pady=2
            )
            ctk.CTkLabel(scrollable_table_frame, text=f"{item['price']:.2f}").grid(
                row=row, column=2, padx=6, pady=2
            )
            ctk.CTkLabel(scrollable_table_frame, text=f"{item['subtotal']:.2f}").grid(
                row=row, column=3, padx=6, pady=2
            )
            ctk.CTkButton(
                scrollable_table_frame,
                text="✕",
                width=28,
                height=24,
                fg_color="#8B0000",
                hover_color="#B22222",
                command=lambda idx=i: _remove(idx, refresh_table),
            ).grid(row=row, column=4, padx=4, pady=2)

        total_row = TABLE_ROW_OFFSET + len(state.materials_data)
        ctk.CTkFrame(scrollable_table_frame, height=1, fg_color="gray50").grid(
            row=total_row, column=0, columnspan=5, sticky="ew", padx=4, pady=(4, 0)
        )
        ctk.CTkLabel(scrollable_table_frame, text="Total:", font=header_font, anchor="e").grid(
            row=total_row + 1, column=0, columnspan=3, padx=6, pady=(2, 8), sticky="e"
        )
        ctk.CTkLabel(
            scrollable_table_frame, text=f"R$ {state.get_total():.2f}", font=header_font
        ).grid(row=total_row + 1, column=3, padx=6, pady=(2, 8), sticky="ew")

    refresh_table()
    refresh_dropdown()
    return start_row + 6


def _remove(idx: int, refresh_callback) -> None:
    """
    Removes a material from the state and refreshes the table.
    """
    state.remove_material(idx)
    refresh_callback()
