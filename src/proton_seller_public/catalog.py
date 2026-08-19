"""Funções públicas de catálogo e apresentação do Proton for Seller."""

from __future__ import annotations

import re
from typing import Optional


def extract_price_value(price_text: str) -> Optional[float]:
    """Converte preços como 'R$ 1.234,56' para float."""
    cleaned = str(price_text).strip().replace("R$", "").replace("r$", "")
    cleaned = cleaned.replace(" ", "")
    cleaned = cleaned.replace(".", "")
    cleaned = cleaned.replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None


def format_brl(value: float) -> str:
    """Formata um valor simples no padrão de exibição usado pelo projeto."""
    return f"R$ {value:.2f}".replace(".", ",")


def get_lowest_price_text(products: list[dict]) -> str:
    """Retorna o menor preço válido de uma lista de produtos."""
    numeric_prices: list[float] = []
    for product in products:
        parsed = extract_price_value(product.get("price", ""))
        if parsed is not None:
            numeric_prices.append(parsed)

    if numeric_prices:
        return format_brl(min(numeric_prices))
    if products:
        return str(products[0].get("price", "Consultar"))
    return "Consultar"


def parse_stock_value(stock_text: str) -> Optional[int]:
    """Extrai uma quantidade inteira de um texto de estoque."""
    digits = "".join(ch for ch in str(stock_text) if ch.isdigit())
    if not digits:
        return None
    try:
        return int(digits)
    except ValueError:
        return None


def normalize_sales_panel_image_url(value: Optional[str]) -> Optional[str]:
    """Normaliza uma URL HTTP(S) informada para a imagem de um painel."""
    raw = str(value or "").strip()
    if not raw:
        return None

    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1].strip()

    markdown_match = re.search(r"\[[^\]]*\]\((https?://[^)]+)\)", raw, flags=re.IGNORECASE)
    if markdown_match:
        raw = markdown_match.group(1).strip()

    if not raw.lower().startswith(("http://", "https://")):
        url_match = re.search(r"https?://\S+", raw, flags=re.IGNORECASE)
        if url_match:
            raw = url_match.group(0).rstrip(">)., ")

    if not raw.lower().startswith(("http://", "https://")):
        return None

    return raw


def parse_product_lines(value: str, *, max_products: int = 25) -> list[dict]:
    """Lê linhas no formato ``nome | preço | quantidade``.

    Levanta ``ValueError`` quando uma linha é inválida ou quando o limite de
    produtos é excedido.
    """
    raw_lines = [line.strip() for line in str(value or "").splitlines() if line.strip()]
    products: list[dict] = []

    for line_number, line in enumerate(raw_lines, start=1):
        parts = [part.strip() for part in line.split("|")]
        if len(parts) != 3 or not all(parts):
            raise ValueError(
                f"Linha {line_number} inválida. Use: nome | preço | quantidade"
            )

        quantity = parse_stock_value(parts[2])
        if quantity is None:
            raise ValueError(f"Quantidade inválida na linha {line_number}: {parts[2]!r}")

        products.append(
            {
                "name": parts[0],
                "price": parts[1],
                "stock": str(quantity),
                "emoji_id": None,
            }
        )

    if not products:
        raise ValueError("Informe pelo menos um produto.")
    if len(products) > max_products:
        raise ValueError(f"O painel aceita no máximo {max_products} produtos.")

    return products
