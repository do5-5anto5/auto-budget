from logic.budget_html_build import set_budget_html
from pdf.generate_pdf import generate_pdf


"""
simulating data entries from GUI
"""
name = "Nome"
phone = "(35) - 99999 9999"
logo = "Logo"

customer_name = "Cliente"
customer_address = "Endereço, Bairro, Cidade"

materials = {
    "Placa Standard": {"price": 42.0, "units": 15},
    "Tabica CR2": {"price": 16.0, "units": 6},
}

labor_price = 40.0
labor_qty = 26.8
billing_method = "m²"

bm = set_budget_html(
    name=name,
    phone=phone,
    logo=logo,
    customer_name=customer_name,
    customer_address=customer_address,
    materials=materials,
    labor_price=labor_price,
    labor_qty=labor_qty,
    billing_method=billing_method,
)

generate_pdf(bm, customer_name)
