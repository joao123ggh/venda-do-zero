#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplicação Flask da Landing Page 'FAÇA SUA PRIMEIRA VENDA DO ZERO'
Autor: Venda do Zero
"""

import sys

# Garante compatibilidade de encoding no console do Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from flask import Flask, render_template, redirect, request, url_for
import config

app = Flask(__name__)
app.config.from_object(config)

@app.context_processor
def inject_global_variables():
    """Disponibiliza variáveis de configuração para todos os templates Jinja2."""
    return {
        "checkout_url": config.CHECKOUT_URL,
        "CHECKOUT_URL": config.CHECKOUT_URL,
        "product_name": config.PRODUCT_NAME,
        "product_subtitle": config.PRODUCT_SUBTITLE,
        "product_tagline": config.PRODUCT_TAGLINE,
        "price_original": config.PRICE_ORIGINAL,
        "price_current": config.PRICE_CURRENT,
        "price_currency": config.PRICE_CURRENCY,
        "payment_type": config.PAYMENT_TYPE,
        "brand_name": config.BRAND_NAME,
        "brand_description": config.BRAND_DESCRIPTION,
        "instagram_url": config.INSTAGRAM_URL,
        "tiktok_url": config.TIKTOK_URL,
        "support_email": config.SUPPORT_EMAIL,
    }

@app.route("/")
def index():
    """Renderiza a landing page principal com todas as seções e oferta."""
    return render_template(
        "index.html",
        checkout_url=config.CHECKOUT_URL,
        CHECKOUT_URL=config.CHECKOUT_URL
    )

@app.route("/checkout")
def checkout_redirect():
    """
    Rota de redirecionamento dinâmico para o checkout.
    Permite apontar botões locais para /checkout e gerenciar o destino em config.py.
    """
    target_url = config.CHECKOUT_URL.strip() if config.CHECKOUT_URL else ""
    
    # Se ainda for o placeholder padrão, exibe um alerta amigável e redireciona de volta à oferta
    if not target_url or "COLE_SEU_LINK" in target_url:
        return redirect("/#oferta?config_alerta=configure_checkout_url")
    
    return redirect(target_url, code=302)

if __name__ == "__main__":
    print("=" * 60)
    print(f"[OK] Iniciando servidor em http://{config.SERVER_HOST}:{config.SERVER_PORT}")
    print(f"[OK] Checkout configurado: {config.CHECKOUT_URL}")
    print("=" * 60)
    app.run(
        host=config.SERVER_HOST,
        port=config.SERVER_PORT,
        debug=config.DEBUG_MODE
    )
