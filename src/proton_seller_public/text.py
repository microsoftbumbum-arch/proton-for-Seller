"""Pequenos utilitários de texto usados na experiência do Seller."""

from __future__ import annotations

from typing import Optional


def sanitize_channel_name(text_value: str) -> str:
    """Converte um texto em um nome simples de canal do Discord."""
    lowered = "".join(ch.lower() if ch.isalnum() else "-" for ch in str(text_value))
    while "--" in lowered:
        lowered = lowered.replace("--", "-")
    return lowered.strip("-") or "ticket"


def build_ticket_topic(owner_id: int, claimed_by: int = 0) -> str:
    """Cria o pequeno marcador de contexto usado por tickets."""
    return f"ticket_owner:{int(owner_id)};claimed_by:{int(claimed_by)}"


def parse_ticket_topic(topic: Optional[str]) -> tuple[Optional[int], Optional[int]]:
    """Lê os IDs de dono e atendente de um marcador de ticket."""
    if not topic:
        return None, None

    owner_id: Optional[int] = None
    claimed_by: Optional[int] = None
    for part in topic.split(";"):
        if part.startswith("ticket_owner:"):
            try:
                owner_id = int(part.split(":", 1)[1])
            except ValueError:
                owner_id = None
        elif part.startswith("claimed_by:"):
            try:
                claimed_by = int(part.split(":", 1)[1])
            except ValueError:
                claimed_by = None
    return owner_id, claimed_by
