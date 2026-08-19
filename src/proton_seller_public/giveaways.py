"""Utilitários públicos de duração de sorteios."""

from __future__ import annotations

import re
from typing import Optional


def parse_giveaway_duration(value: str) -> Optional[int]:
    """Converte 30m, 2h, 1d ou minutos puros para segundos."""
    raw = str(value or "").strip().lower().replace(" ", "")
    if not raw:
        return None

    match = re.fullmatch(
        r"(\d+)(m|min|mins|minuto|minutos|h|hora|horas|d|dia|dias)?",
        raw,
    )
    if not match:
        return None

    amount = int(match.group(1))
    unit = match.group(2) or "m"
    if amount <= 0:
        return None

    if unit in {"m", "min", "mins", "minuto", "minutos"}:
        seconds = amount * 60
    elif unit in {"h", "hora", "horas"}:
        seconds = amount * 3600
    else:
        seconds = amount * 86400

    if seconds < 60 or seconds > 30 * 86400:
        return None
    return seconds


def format_giveaway_duration(seconds: Optional[int]) -> str:
    """Transforma segundos em uma descrição curta em português."""
    if not seconds:
        return "Não configurado"
    if seconds % 86400 == 0:
        return f"{seconds // 86400} dia(s)"
    if seconds % 3600 == 0:
        return f"{seconds // 3600} hora(s)"
    return f"{max(1, seconds // 60)} minuto(s)"
