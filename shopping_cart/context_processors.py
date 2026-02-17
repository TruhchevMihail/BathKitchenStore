from decimal import Decimal
from typing import Dict, List

from django.http import HttpRequest

from catalog.models import Product

CART_SESSION_KEY = "cart"


def cart(request: HttpRequest) -> Dict[str, object]:
    session_cart = request.session.get(CART_SESSION_KEY, {}) or {}

    total_qty = 0
    for _, entry in session_cart.items():
        try:
            total_qty += max(0, int(entry.get("qty", 0)))
        except (TypeError, ValueError):
            continue
    preview_items: List[dict] = []
    preview_total = Decimal("0.00")

    if session_cart:
        ordered_ids = list(session_cart.keys())[:5]
        try:
            product_ids = [int(pid) for pid in ordered_ids]
        except ValueError:
            product_ids = []
        products = {p.id: p for p in Product.objects.filter(id__in=product_ids)}
        for pid_str in ordered_ids:
            try:
                pid = int(pid_str)
            except ValueError:
                continue
            p = products.get(pid)
            if not p:
                continue
            try:
                qty = max(1, int(session_cart.get(pid_str, {}).get("qty", 1)))
            except (TypeError, ValueError):
                qty = 1
            price = Decimal(p.price)
            subtotal = price * qty
            preview_total += subtotal
            preview_items.append({
                "product": p,
                "qty": qty,
                "price": price,
                "subtotal": subtotal,
            })

    return {
        "cart_count": total_qty,
        "cart_items": len(session_cart),
        "cart_preview_items": preview_items,
        "cart_preview_total": preview_total,
    }
