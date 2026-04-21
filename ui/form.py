import customtkinter as ctk

ctk.set_appearance_mode("dark")

# TODO logo entry
# TODO Fill existent relevant data to fields

app = ctk.CTk()
app.title('Auto Budget')
app.geometry('600x600')

scroll_frame = ctk.CTkScrollableFrame(app)
scroll_frame.pack(fill='both', expand=True)
scroll_frame.grid_columnconfigure(0, weight=1)
scroll_frame.grid_columnconfigure(1, weight=4)
scroll_frame.grid_columnconfigure(2, weight=4)
scroll_frame.grid_columnconfigure(3, weight=1)

str_materials_list = ctk.StringVar()


def write_this_materials():
    str_material_name = str(material_entry.get())
    f_material_price = float(price_entry.get())
    i_material_qty = int(qty_entry.get())
    subtotal = f'{(f_material_price * i_material_qty):.2f}'    
    current = str_materials_list.get()
    new_line = f'{i_material_qty}    x    {str_material_name}:                  R$ {subtotal}'
    str_materials_list.set(current + '\n' + new_line if current else new_line)
    

font_label = ctk.CTkFont(scroll_frame, size=24, weight='bold')
description_label_font = ctk.CTkFont(scroll_frame, size=20, weight='bold')

# Top label 'above' the grid
label = ctk.CTkLabel(scroll_frame, text='Orçamento', font=font_label)
label.grid(row=0, column=1, columnspan=2, pady=30, padx=10, sticky='ew')


# Business data entries

business_label = ctk.CTkLabel(
    scroll_frame, text='Dados da empresa:', font=description_label_font
)
business_label.grid(row=1, column=1, columnspan=2, pady=10, padx=10, sticky='ew')

name_entry = ctk.CTkEntry(scroll_frame, placeholder_text='Nome da empresa')
name_entry.grid(row=2, column=1, pady=10, padx=10, sticky='ew')

phone_entry = ctk.CTkEntry(scroll_frame, placeholder_text='Whatsscroll_frame da empresa')
phone_entry.grid(row=2, column=2, pady=10, padx=10, sticky='ew')

spacer_2 = ctk.CTkLabel(scroll_frame, text='')
spacer_2.grid(row=3)


# Customer data entries

customer_label = ctk.CTkLabel(
    scroll_frame, text='Dados do cliente:', font=description_label_font
)
customer_label.grid(row=4, column=1, columnspan=2, pady=10, padx=10, sticky='ew')

customer_name_entry = ctk.CTkEntry(scroll_frame, placeholder_text='Nome do cliente')
customer_name_entry.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

customer_address_entry = ctk.CTkEntry(scroll_frame, placeholder_text='Endereço do cliente')
customer_address_entry.grid(row=5, column=2, padx=10, pady=10, sticky='ew')

spacer_2 = ctk.CTkLabel(scroll_frame, text='')
spacer_2.grid(row=6)


# Materials sub grid

materials_label = ctk.CTkLabel(scroll_frame, text='Materiais:', font=description_label_font)
materials_label.grid(
    row=7,
    column=1,
    columnspan=2,
    pady=10,
    padx=10,
)

materials_frame = ctk.CTkFrame(scroll_frame, fg_color='transparent')
materials_frame.grid(row=8, column=1, columnspan=2, padx=10, pady=10, sticky='ew')
materials_frame.grid_columnconfigure(0, weight=1)
materials_frame.grid_columnconfigure(1, weight=1)
materials_frame.grid_columnconfigure(2, weight=1)

add_material_label = ctk.CTkLabel(materials_frame, text='Adicionar material:')
add_material_label.grid(row=0, column=0, sticky='ew')

add_price_label = ctk.CTkLabel(materials_frame, text='Preço ex. 99.99 :')
add_price_label.grid(row=0, column=1, sticky='ew')

add_qty_label = ctk.CTkLabel(materials_frame, text='Quantidade:')
add_qty_label.grid(row=0, column=2, sticky='ew')


material_entry = ctk.CTkEntry(materials_frame)
material_entry.grid(row=1, column=0, padx=(0, 5), sticky='ew')

# Set price format
vcmd = (
    scroll_frame.register(
        lambda P: P.replace('.', '', 1).replace(',', '', 1).isdigit() or P == ''
    ),
    '%P',
)
price_var = ctk.StringVar()
price_var.trace_add(
    'write', lambda *args: price_var.set(price_var.get().replace(',', '.'))
)

price_entry = ctk.CTkEntry(
    materials_frame, textvariable=price_var, validate='key', validatecommand=vcmd
)
price_entry.grid(row=1, column=1, padx=(0, 5), sticky='ew')

qty_entry = ctk.CTkEntry(materials_frame, validate='key', validatecommand=vcmd)
qty_entry.grid(row=1, column=2, sticky='ew')

add_material_button = ctk.CTkButton(
    scroll_frame, text='Adicionar', width=200, command=write_this_materials
)
add_material_button.grid(row=9, column=1, columnspan=2)

materials_list_label = ctk.CTkLabel(scroll_frame, textvariable=str_materials_list)
materials_list_label.grid(row=10, column=1, pady=10, padx=10)

app.mainloop()
