"""
Configurações da Landing Page - Venda do Zero
Substitua o link da Kiwify abaixo pelo seu link de checkout real quando estiver pronto.
"""

import os

# ==============================================================================
# LINK DE CHECKOUT PRINCIPAL (Substitua pela sua URL da Kiwify / Hotmart / etc.)
# ==============================================================================
CHECKOUT_URL = "COLE_SEU_LINK_DA_KIWIFY_AQUI"

# ==============================================================================
# CONFIGURAÇÕES DO PRODUTO & OFERTA
# ==============================================================================
PRODUCT_NAME = "FAÇA SUA PRIMEIRA VENDA DO ZERO"
PRODUCT_SUBTITLE = "Aprenda o passo a passo para começar a vender na Shopee e no Mercado Livre, mesmo que você nunca tenha vendido nada pela internet."
PRODUCT_TAGLINE = "Aprenda como escolher produtos, calcular preços, criar anúncios, tirar melhores fotos e começar a divulgar sua loja."

PRICE_ORIGINAL = "49,90"
PRICE_CURRENT = "19,90"
PRICE_CURRENCY = "R$"
PAYMENT_TYPE = "Pagamento único"

BRAND_NAME = "VENDA DO ZERO"
BRAND_DESCRIPTION = "Conteúdo educacional para quem deseja aprender os primeiros passos das vendas online."

# ==============================================================================
# CANAIS DE CONTATO E REDES SOCIAIS (Configuráveis)
# ==============================================================================
INSTAGRAM_URL = "https://instagram.com/vendadozero"  # Substitua pelo seu Instagram se desejar
TIKTOK_URL = "https://tiktok.com/@vendadozero"       # Substitua pelo seu TikTok se desejar
SUPPORT_EMAIL = "suporte@vendadozero.com.br"         # Substitua pelo seu e-mail de suporte

# ==============================================================================
# CONFIGURAÇÃO DO SERVIDOR FLASK
# ==============================================================================
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000
DEBUG_MODE = False
SECRET_KEY = os.environ.get("SECRET_KEY", "venda_do_zero_chave_secreta_local_2026")
