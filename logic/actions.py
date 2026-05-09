import os
import webbrowser
import state

def open_budgets_folder():
    """
    Opens the 'budgets' folder in the file explorer.
    """
    try:
        if not os.path.exists('budgets'):
            os.makedirs('budgets')
        os.startfile('budgets')
    except Exception as e:
        print(f"Erro ao abrir pasta: {e}")

def open_whatsapp():
    """
    Opens WhatsApp Web with the customer's phone number if available.
    """
    try:
        phone = state.data_to_pdf.get('customer_phone', '')
        # Remove any non-numeric characters
        clean_phone = ''.join(filter(str.isdigit, phone))
        
        if clean_phone:
            # If the number has 10 or 11 digits (DDD + Number), add Brazil prefix 55
            if len(clean_phone) in [10, 11] and not clean_phone.startswith('55'):
                clean_phone = f"55{clean_phone}"
            
            url = f"https://wa.me/{clean_phone}"
        else:
            url = "https://web.whatsapp.com"
            
        webbrowser.open(url)
    except Exception as e:
        print(f"Erro ao abrir WhatsApp: {e}")
