"""
Receives budget data and generates an HTML structure.
Returns this structure as a string.
"""


def set_budget_html(
    name: str,
    phone: str,
    logo: str,
    customer_name: str,
    customer_address: str,
    materials: list[dict],
    labor_price: float,
    labor_qty: float,
    billing_method: str,
    logo_image: str = None,
):

    labor_subtotal = labor_qty * labor_price
    
    # Generate dynamic valor label based on billing method
    if billing_method == "m²":
        valor_label = f"Valor do m²: R$ {labor_price:.2f}"
    elif billing_method == "metro linear":
        valor_label = f"Valor do metro linear: R$ {labor_price:.2f}"
    else:
        valor_label = f"Valor da unidade: R$ {labor_price:.2f}"
    
    # Generate logo HTML - use image if available, fallback to text
    if logo_image:
        logo_html = f'<img src="data:image/jpeg;base64,{logo_image}" style="width: 100%; height: 100%; object-fit: cover; display: block;" alt="Logo">'
    else:
        logo_html = f'<span style="color: #a8bfd4; font-size: 10px; text-align: center; line-height: 1.3; display: block;">{logo}</span>'

    return f"""
<meta charset="UTF-8">

<div
    style="max-width: 600px; margin: 20px auto; background: white; border: 2px solid #000000; border-radius: 12px; overflow: hidden; font-family: sans-serif; color: #222;">

    <div style="background: #0d2240; padding: 30px; display: flex; align-items: center; justify-content: center; gap: 30px;">
        <div style="text-align: center;">
            <div style="color: white; font-size: 22px; font-weight: 500; letter-spacing: 1px;">{name}</div>
            <div style="color: #a8bfd4; font-size: 14px; margin-top: 4px;">{phone}</div>
            <div style="color: #c8d8e8; font-size: 13px; font-weight: 500; margin-top: 8px; letter-spacing: 0.5px;">Orçamento</div>
        </div>
        <div
            style="width: 80px; height: 80px; border-radius: 12px; background: #1a1a1a; display: flex; align-items: center; justify-content: center; border: 2px solid #2e5a8f; overflow: hidden; flex-shrink: 0;">
            {logo_html}
        </div>
    </div>

    <div style="padding: 30px 40px 0;">
    <div style="font-size: 15px; font-weight: 500; text-align: center;">{customer_name}</div>
    <div style="font-size: 13px; color: #555; margin-top: 2px; text-align: center;">{customer_address}</div>
    <div style="border-top: 1px solid #ddd; margin-top: 20px;"></div>
    </div>

    <div style="padding: 30px 40px 0;">
    <div style="font-size: 14px; font-weight: 500; margin-bottom: 10px;">{valor_label}</div>
    <div style="border-top: 1px solid #ddd; margin-top: 20px;"></div>
    </div>

    <div style="padding: 30px 40px 0;">
    <div style="font-size: 14px; font-weight: 500; margin-bottom: 10px;">Tabela de materiais</div>
    <table style="width: 100%; font-size: 15px; border-collapse: collapse;">
        <thead>
        <tr style="color: #666; border-bottom: 0.5px solid #ddd;">
            <th style="text-align: left; padding: 8px 0; font-weight: 500;">Item</th>
            <th style="text-align: center; padding: 8px 0; font-weight: 500;">Qtd</th>
        </tr>
        </thead>
        <tbody>
            {str(set_items_table_rows(materials))}
        </tbody>
    </table>
    <div style="border-top: 1px solid #ddd; margin-top: 20px;"></div>
    </div>

    

    <div style="padding: 30px 40px 40px; text-align: center;">
    <div
        style="background: #f5f7fa; border: 0.5px solid #ddd; border-radius: 8px; padding: 20px; display: inline-block; text-align: center;">
        <div style="font-size: 16px; color: #666; margin-bottom: 8px;">Total do serviço</div>
        <div style="font-size: 16px; color: #666; margin-bottom: 8px;">Material e mão de obra:</div>
        <div style="font-size: 24px; font-weight: 500; color: #0d2240;">R$ {labor_subtotal:.2f}</div>
    </div>
    </div>

</div>
    """


def set_items_table_rows(materials: list):
    table_rows = ""

    for item in materials:
        table_rows += f"""
        <tr style="border-bottom: 0.5px solid #f0f0f0;">
            <td style="padding: 10px 0 10px 15px; font-size: 15px;">{item['name']}</td>
            <td style="text-align: center; padding: 10px 0; font-size: 15px;">{item['qty']}</td>
        </tr>
    """
    return table_rows


