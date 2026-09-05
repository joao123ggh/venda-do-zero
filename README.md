# 🚀 FAÇA SUA PRIMEIRA VENDA DO ZERO — Landing Page em Flask

Landing Page profissional de alta conversão para o produto digital **"FAÇA SUA PRIMEIRA VENDA DO ZERO"** (Guia prático para iniciantes venderem na Shopee e no Mercado Livre).

Desenvolvida com **Python + Flask**, HTML5 semântico, CSS3 moderno (tema escuro com detalhes em laranja vibrante) e JavaScript vanilla.

---

## 📁 Estrutura do Projeto

```text
EBOOK NOVO SHOPEE E MERCADO LIVRE/
├── static/
│   ├── favicon.svg         # Ícone personalizado da aba do navegador
│   ├── style.css           # Folha de estilo completa e responsiva
│   └── script.js           # Lógica do menu mobile, acordeão FAQ e navegação
├── templates/
│   └── index.html          # Template principal com todas as 8 seções
├── app.py                  # Aplicação Flask com rotas '/' e '/checkout'
├── config.py               # Configuração centralizada (Link da Kiwify, preços, redes)
├── server.py               # Script de execução com abertura automática do navegador
├── requirements.txt        # Dependências do projeto (Flask)
├── iniciar_site.bat        # Arquivo de 1-clique para rodar no Windows
└── README.md               # Instruções e documentação
```

---

## ⚡ Como Iniciar o Site no Windows

### Método 1: Pelo arquivo executável (Mais Fácil)
1. Dê um duplo clique no arquivo **`iniciar_site.bat`**.
2. O script detectará o Python automaticamente, instalará as dependências se necessário e iniciará o servidor Flask.
3. Seu navegador padrão abrirá automaticamente na página: **`http://127.0.0.1:5000`**.

### Método 2: Pelo Terminal / PowerShell
```powershell
# 1. Instalar as dependências (caso ainda não tenha feito)
pip install -r requirements.txt

# 2. Executar o servidor
python server.py
```
O terminal exibirá a mensagem de confirmação e abrirá a página no seu navegador.

---

## 🛒 Como Configurar o Link de Checkout da Kiwify

Todos os botões de compra da página estão conectados a uma única configuração central.

1. Abra o arquivo **`config.py`** em qualquer editor de texto.
2. Localize a linha:
   ```python
   CHECKOUT_URL = "COLE_SEU_LINK_DA_KIWIFY_AQUI"
   ```
3. Substitua `"COLE_SEU_LINK_DA_KIWIFY_AQUI"` pela URL real do seu checkout na Kiwify (ex: `"https://pay.kiwify.com.br/abcdef"`).
4. Salve o arquivo e recarregue a página! Todos os botões do site agora levarão diretamente para o seu checkout.

---

## 🎨 Seções da Landing Page

1. **HERO:** Título impactante com destaque visual em *"PRIMEIRA VENDA"* e *"DO ZERO"*, subtítulo, texto complementar e mockup 3D do livro digital e smartphone com gráficos de vendas.
2. **PROBLEMA:** 6 cards reais com as principais barreiras de quem começa do zero.
3. **O QUE VOU APRENDER:** 6 cards numerados (01 a 06) detalhando os módulos práticos.
4. **O QUE VOCÊ RECEBE:** 6 cards detalhando o Ebook principal e os 5 bônus complementares inclusos.
5. **COMO FUNCIONA:** 3 passos simples da compra ao aprendizado.
6. **APRESENTAÇÃO DO EBOOK:** Prévia visual das páginas internas e metodologia do guia.
7. **OFERTA:** Card de conversão com preço promocional (De R$ 49,90 por R$ 19,90 - pagamento único) e selos de segurança.
8. **FAQ:** 5 perguntas frequentes em formato de acordeão interativo com JavaScript.
9. **RODAPÉ:** Identidade da marca, links rápidos, contatos configuráveis e aviso legal.

---

## ⚙️ Customização Adicional (Opcional)

No arquivo `config.py`, você também pode alterar:
- Preço original e preço atual (`PRICE_ORIGINAL`, `PRICE_CURRENT`)
- Links do Instagram e TikTok (`INSTAGRAM_URL`, `TIKTOK_URL`)
- E-mail de suporte (`SUPPORT_EMAIL`)
