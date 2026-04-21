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
    materials: dict,
    labor_price: float,
    labor_qty: float,
    billing_method: str,
):

    labor_subtotal = labor_qty * labor_price

    return f"""
<meta charset="UTF-8">

<div
    style="max-width: 600px; margin: 0 auto; background: white; border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); overflow: hidden; font-family: var(--font-sans); color: #222;">

    <div
    style="background: #0d2240; padding: 24px 28px; display: flex; align-items: center; justify-content: space-between;">
    <div>
        <div style="color: white; font-size: 22px; font-weight: 500; letter-spacing: 1px;">{name}</div>
        <div style="color: #a8bfd4; font-size: 14px; margin-top: 4px;">{phone}</div>
        <div style="color: #c8d8e8; font-size: 13px; font-weight: 500; margin-top: 8px; letter-spacing: 0.5px;">Orçamento
        </div>
    </div>
    <div
        style="width: 64px; height: 64px; border-radius: 8px; background: #1e3a5f; display: flex; align-items: center; justify-content: center; border: 1.5px solid #2e5a8f;">
        <span style="color: #a8bfd4; font-size: 11px; text-align: center; line-height: 1.3;">{logo}</span>
    </div>
    </div>

    <div style="padding: 24px 28px 0;">
    <div style="font-size: 15px; font-weight: 500;">{customer_name}</div>
    <div style="font-size: 13px; color: #555; margin-top: 2px;">{customer_address}</div>
    <div style="border-top: 1px solid #ddd; margin-top: 20px;"></div>
    </div>

    <div style="padding: 20px 28px 0;">
    <div style="font-size: 14px; font-weight: 500; margin-bottom: 10px;">Tabela de materiais</div>
    <table style="width: 100%; font-size: 13px; border-collapse: collapse;">
        <thead>
        <tr style="color: #666; border-bottom: 0.5px solid #ddd;">
            <th style="text-align: left; padding: 6px 0; font-weight: 500;">Item</th>
            <th style="text-align: center; padding: 6px 0; font-weight: 500;">Qtd</th>
            <th style="text-align: right; padding: 6px 0; font-weight: 500;">Preço unit.</th>
            <th style="text-align: right; padding: 6px 0; font-weight: 500;">Total</th>
        </tr>
        </thead>
        <tbody>
            {str(set_items_table_rows(materials))}
        </tbody>
    </table>
    <div
        style="text-align: right; font-size: 13px; color: #444; margin-top: 10px; padding-top: 8px; border-top: 0.5px solid #ddd;">
        Subtotal (materiais): <strong>R$ 537,00</strong>
    </div>
    <div style="border-top: 1px solid #ddd; margin-top: 16px;"></div>
    </div>

    <div style="padding: 20px 28px 0;">
    <div style="font-size: 14px; font-weight: 500; margin-bottom: 10px;">Mão de obra</div>
    <div style="font-size: 13px; color: #444;">{labor_qty} {billing_method} x {labor_price}</div>
    <div
        style="text-align: right; font-size: 13px; color: #444; margin-top: 10px; padding-top: 8px; border-top: 0.5px solid #ddd;">
        Subtotal (mão de obra): <strong>R$ {labor_subtotal:.2f}</strong>
    </div>
    <div style="border-top: 1px solid #ddd; margin-top: 16px;"></div>
    </div>    

    <div style="padding: 16px 28px 28px; display: flex; justify-content: flex-end;">
    <div
        style="background: #f5f7fa; border: 0.5px solid #ddd; border-radius: 8px; padding: 12px 20px; text-align: right;">
        <div style="font-size: 13px; color: #666;">Total geral</div>
        <div style="font-size: 20px; font-weight: 500; color: #0d2240;">R$ {(labor_subtotal + set_materials_subtotal(materials)):.2f}</div>
    </div>
    </div>

</div>
    """


def set_items_table_rows(materials: dict):
    table_rows = ""

    for item in materials:
        price = f" {(materials[item]['price']):.2f}"
        total = f"{(materials[item]['units'] * materials[item]['price']):.2f}"

        table_rows += f"""
        <tr style="border-bottom: 0.5px solid #f0f0f0;">
            <tr style="border-bottom: 0.5px solid #f0f0f0;">
            <td style="padding: 7px 0;">{str(item)}</td>
            <td style="text-align: center; padding: 7px 0;">{materials[item]['units']}</td>
            <td style="text-align: right; padding: 7px 0;">R$ {price}</td>
            <td style="text-align: right; padding: 7px 0;">R$ {total}</td>
        </tr>
    """
    return table_rows


def set_materials_subtotal(materials: dict):
    materials_total = 0
    for item in materials:
        subtotal = float(materials[item]["units"] + materials[item]["price"])
        materials_total += subtotal
    return float(materials_total)
