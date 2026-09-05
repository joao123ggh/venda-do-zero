#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de inicialização do servidor Flask com abertura automática do navegador.
Execute: python server.py
"""

import sys
import time
import threading
import webbrowser

# Garante compatibilidade de saída no terminal Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from app import app
import config

def abrir_navegador(url):
    """Aguarda 1.5 segundos para o servidor inicializar e abre a URL no navegador padrão."""
    time.sleep(1.5)
    print(f"\n[OK] Abrindo navegador em: {url} ...")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"[AVISO] Nao foi possivel abrir automaticamente: {e}")
        print(f"Por favor, abra manualmente no seu navegador: {url}")

def main():
    url = f"http://{config.SERVER_HOST}:{config.SERVER_PORT}"
    print("=" * 65)
    print(" >>> VENDA DO ZERO - SERVIDOR DA LANDING PAGE <<< ")
    print("=" * 65)
    print(f"  Endereco local: {url}")
    print(f"  Link Checkout : {config.CHECKOUT_URL}")
    print("  Para encerrar o servidor, aperte CTRL+C.")
    print("=" * 65)

    # Dispara thread para abrir o navegador
    threading.Thread(target=abrir_navegador, args=(url,), daemon=True).start()

    # Inicia o Flask
    app.run(
        host=config.SERVER_HOST,
        port=config.SERVER_PORT,
        debug=False
    )

if __name__ == "__main__":
    main()
