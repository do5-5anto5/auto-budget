from os import makedirs
from datetime import date
from playwright.sync_api import sync_playwright

def generate_pdf(html: str, name: str):    
    """
    Receives html string and parse and saves it to pdf file
    """
    makedirs('budgets', exist_ok=True)
    today = date.today().strftime('%d-%m-%y')
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html)
        page.pdf(path=f'budgets/{name}  {today}.pdf', print_background=True)
        browser.close()
