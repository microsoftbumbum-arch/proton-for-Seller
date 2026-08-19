from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from proton_seller_public.catalog import (  # noqa: E402
    extract_price_value,
    format_brl,
    normalize_sales_panel_image_url,
    parse_product_lines,
    parse_stock_value,
)
from proton_seller_public.giveaways import (  # noqa: E402
    format_giveaway_duration,
    parse_giveaway_duration,
)
from proton_seller_public.text import (  # noqa: E402
    build_ticket_topic,
    parse_ticket_topic,
    sanitize_channel_name,
)


class CatalogTests(unittest.TestCase):
    def test_price(self):
        self.assertEqual(extract_price_value("R$ 12,90"), 12.90)
        self.assertEqual(format_brl(7.5), "R$ 7,50")

    def test_stock(self):
        self.assertEqual(parse_stock_value("10 unidades"), 10)
        self.assertIsNone(parse_stock_value("sem estoque"))

    def test_products(self):
        products = parse_product_lines("A | R$ 5,00 | 2\nB | 3,99 | 8")
        self.assertEqual(len(products), 2)
        self.assertEqual(products[1]["stock"], "8")

    def test_image_url(self):
        self.assertEqual(
            normalize_sales_panel_image_url("[banner](https://example.com/a.png)"),
            "https://example.com/a.png",
        )
        self.assertIsNone(normalize_sales_panel_image_url("arquivo local"))


class GiveawayTests(unittest.TestCase):
    def test_duration(self):
        self.assertEqual(parse_giveaway_duration("2h"), 7200)
        self.assertEqual(format_giveaway_duration(7200), "2 hora(s)")
        self.assertIsNone(parse_giveaway_duration("31d"))


class TextTests(unittest.TestCase):
    def test_channel(self):
        self.assertEqual(sanitize_channel_name("Pedido do João!"), "pedido-do-joão")

    def test_topic(self):
        raw = build_ticket_topic(123, 456)
        self.assertEqual(parse_ticket_topic(raw), (123, 456))


if __name__ == "__main__":
    unittest.main()
