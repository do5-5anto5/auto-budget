import state
from pdf.generate_pdf import generate_pdf as generate_pdf_file
from logic.budget_html_build import set_budget_html
from database.business import get_business


def collect_all_data(parent_frame):
    """
   Collects all data from the UI and stores it in the state.
    """
    try:
        # Business data
        business_data = {
            'name': getattr(parent_frame, 'business_name_entry', None).get() if hasattr(parent_frame, 'business_name_entry') else "",
            'phone': getattr(parent_frame, 'business_phone_entry', None).get() if hasattr(parent_frame, 'business_phone_entry') else "",
            'logo': getattr(parent_frame, 'business_logo_entry', None).get() if hasattr(parent_frame, 'business_logo_entry') else "",
        }
        
        # Get logo image from database
        business_db_data = get_business()
        business_data['logo_image'] = business_db_data.get('logo_image', '')
        
        # Customer data
        customer_data = {
            'customer_name': getattr(parent_frame, 'customer_name_entry', None).get() if hasattr(parent_frame, 'customer_name_entry') else "",
            'customer_phone': getattr(parent_frame, 'customer_phone_entry', None).get() if hasattr(parent_frame, 'customer_phone_entry') else "",
            'customer_address': getattr(parent_frame, 'customer_address_entry', None).get() if hasattr(parent_frame, 'customer_address_entry') else "",
        }
        
        # Labor data
        labor_price_str = getattr(parent_frame, 'labor_price_entry', None).get() if hasattr(parent_frame, 'labor_price_entry') else "0"
        labor_qty_str = getattr(parent_frame, 'labor_qty_entry', None).get() if hasattr(parent_frame, 'labor_qty_entry') else "0"
        billing_method = getattr(parent_frame, 'labor_billing_combo', None).get() if hasattr(parent_frame, 'labor_billing_combo') else "hora(s)"
        
        labor_data = {
            'labor_price': float(labor_price_str.replace(',', '.')) if labor_price_str else 0.0,
            'labor_qty': float(labor_qty_str.replace(',', '.')) if labor_qty_str else 0.0,
            'billing_method': billing_method,
        }
        
        # Combine all data
        all_data = {**business_data, **customer_data, **labor_data}
        
        # Store in state
        state.collect_data_to_pdf(all_data)
        
        return True
    except Exception as e:
        print(f"Erro ao coletar dados: {e}")
        return False


def generate_budget_pdf(parent_frame):
    """
    Generates the budget PDF using the collected data.
    """
    if not collect_all_data(parent_frame):
        return False
    
    try:
        # Get data from state
        data = state.data_to_pdf
        
        # Generate HTML and PDF
        html_string = set_budget_html(
            name=data.get('name', ''),
            phone=data.get('phone', ''),
            logo=data.get('logo', ''),
            customer_name=data.get('customer_name', ''),
            customer_address=data.get('customer_address', ''),
            labor_price=data.get('labor_price', 0.0),
            labor_qty=data.get('labor_qty', 0.0),
            billing_method=data.get('billing_method', 'm²'),
            materials=state.materials_data,
            logo_image=data.get('logo_image', ''),
        )

        generate_pdf_file(
            html=html_string,
            name=data.get('customer_name', ''),
        )
        
        return True
    except Exception as e:
        print(f"Erro ao gerar PDF: {e}")
        return False
