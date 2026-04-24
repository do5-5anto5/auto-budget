materials_data: list[dict] = []
data_to_pdf: dict = {}

def add_material(name: str, price: float, qty: int) -> None:
    materials_data.append(
        {'name': name, 'price': price, 'qty': qty, 'subtotal': price * qty}
    )


def remove_material(idx: int) -> None:
    materials_data.pop(idx)


def get_total() -> float:
    return sum(item['subtotal'] for item in materials_data)

def collect_data_to_pdf(data) -> None:
    data_to_pdf.update(data)