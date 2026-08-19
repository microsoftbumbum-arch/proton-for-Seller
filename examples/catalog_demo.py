from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from proton_seller_public.catalog import (  # noqa: E402
    get_lowest_price_text,
    normalize_sales_panel_image_url,
    parse_product_lines,
)

raw_products = """\
Nitro Mensal | R$ 12,90 | 5
VIP | R$ 7,50 | 10
"""

products = parse_product_lines(raw_products)
print("Produtos:")
for product in products:
    print(f"- {product['name']} | {product['price']} | estoque {product['stock']}")

print("Menor preço:", get_lowest_price_text(products))
print("Imagem:", normalize_sales_panel_image_url("[banner](https://example.com/banner.png)"))
