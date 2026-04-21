from os import makedirs
from weasyprint import HTML
from datetime import date

def generate_pdf(html: str, name: str):    
    """
    Receives html string and parse and saves it to pdf file
    """
    today = date.today().strftime('%d-%m-%y')
    makedirs('budgets', exist_ok=True)

    try: 
        HTML(string=html).write_pdf(f'budgets/{name}-{today}.pdf')
    except Exception as e:
        print(f'Fail to generate pdf: \n{e}')
