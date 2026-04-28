# Auto Budget

A desktop application that **automates the generation of professional service quotes and budgets as PDF documents**. Stop wasting time manually creating quotes - this app streamlines the entire process from data entry to professional PDF output.

## Problem It Solves

Creating professional quotes manually is time-consuming and error-prone. Auto Budget eliminates:
- Manual calculations for labor and materials
- Inconsistent quote formatting
- Time spent on document layout and design
- Missing information in quotes
- Paper-based quote management

The app automates the entire workflow: enter your business info, customer details, labor costs, and materials - then generate a professional PDF quote instantly.

## Features

- **Automated Quote Generation**: Transform data into professional PDFs instantly
- **Modern GUI**: Clean, intuitive interface built with CustomTkinter
- **Business Information Management**: Store company details, logos, and contact info
- **Customer Management**: Quick customer data entry and reuse
- **Smart Labor Cost Calculation**: Flexible billing methods (hourly, per square meter, etc.)
- **Materials Management**: Reusable materials database with pricing
- **Professional PDF Output**: Consistent, branded quote documents
- **Data Persistence**: SQLite database for all business information

## Usage

1. **Run the app**: `python main.py`
2. **Setup your business**: Fill in company details and logo
3. **Add customer**: Enter customer information
4. **Enter costs**: Add labor costs and materials
5. **Generate PDF**: Click "Gerar PDF de Orçamento"

Your professional quote PDF is automatically saved in the `budgets/` folder.

## Project Structure

```
auto-budget/
├── main.py                 # Application entry point
├── ui/                     # User interface components
│   ├── layout.py          # Main application layout
│   ├── sections/          # UI sections (business, customer, labor, materials)
│   └── components/        # Reusable UI components
├── logic/                  # Business logic
│   ├── data_collector.py  # Data collection from UI
│   ├── budget_html_build.py # HTML template generation
│   └── image_processing.py # Image processing utilities
├── database/              # Database operations
│   ├── business.py        # Business information CRUD
│   └── materials.py       # Materials CRUD
├── pdf/                   # PDF generation
│   └── generate_pdf.py    # PDF generation using Playwright
├── state.py               # Global state management
└── budgets/               # Generated PDFs (created automatically)
```

## Libraries Used

### Core Dependencies

- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** - Modern, customizable Tkinter UI library
  - Used for building the modern, dark-themed GUI
  - Provides enhanced widgets and styling options

- **[Playwright](https://playwright.dev/python/)** - Browser automation library
  - Used for converting HTML to PDF with high quality
  - Ensures consistent PDF rendering across different systems

- **[Pillow](https://pillow.readthedocs.io/)** - Python Imaging Library
  - Used for image processing and logo handling
  - Supports various image formats for company logos

### Standard Library Modules

- **sqlite3** - Database operations for persistent storage
- **os** - File system operations and path handling
- **datetime** - Date handling for PDF naming
- **sys** - System-specific parameters and functions

## Database

The application uses SQLite for data persistence with two main tables:

- **business** - Stores company information (name, phone, logo, logo_image)
- **materials** - Stores material names for reuse in quotes

The database file (`budget.db`) is automatically created when the application first runs.

## PDF Generation

PDFs are generated using Playwright's headless browser to ensure consistent formatting and high-quality output. The application:

1. Collects data from the UI
2. Generates an HTML template with the collected data
3. Converts the HTML to PDF using Playwright
4. Saves the PDF in the `budgets/` directory

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please:

1. Check the existing issues on GitHub
2. Create a new issue with detailed information about the problem
3. Include error messages and steps to reproduce the issues

## Quick Installation

1. **Clone and setup:**
```bash
git clone <repository-url>
cd auto-budget
python -m venv .venv
```

2. **Activate virtual environment:**
```bash
# Windows
.venv\Scripts\activate
# macOS/Linux  
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
playwright install
```

4. **Run the app:**
```bash
python main.py
```
