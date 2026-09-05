/**
 * VENDA DO ZERO — SCRIPTS INTERATIVOS
 * Gerencia: Menu móvel hambúrguer, acordeão do FAQ, scroll suave,
 * filtros de prévias do ebook e modal lightbox para visualização ampliada.
 */

document.addEventListener('DOMContentLoaded', () => {
    // ==============================================================================
    // 1. MENU MOBILE (HAMBÚRGUER)
    // ==============================================================================
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const navLinks = document.getElementById('navLinks');
    const allNavLinks = document.querySelectorAll('.nav-link');

    if (mobileMenuToggle && navLinks) {
        mobileMenuToggle.addEventListener('click', () => {
            const isOpen = navLinks.classList.toggle('active');
            mobileMenuToggle.classList.toggle('active');
            mobileMenuToggle.setAttribute('aria-expanded', isOpen);
        });

        // Fecha ao clicar em qualquer item do menu
        allNavLinks.forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                mobileMenuToggle.setAttribute('aria-expanded', 'false');
            });
        });

        // Fecha ao clicar fora do menu
        document.addEventListener('click', (e) => {
            if (!navLinks.contains(e.target) && !mobileMenuToggle.contains(e.target) && navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                mobileMenuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // ==============================================================================
    // 2. NAVBAR SCROLL EFFECT & BOTÃO VOLTAR AO TOPO
    // ==============================================================================
    const navbar = document.getElementById('navbar');
    const backToTopBtn = document.getElementById('backToTopBtn');

    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;

        if (navbar) {
            if (scrollY > 25) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }

        if (backToTopBtn) {
            if (scrollY > 400) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        }
    });

    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // ==============================================================================
    // 3. ABAS DE FILTRO DAS PRÉVIAS DO EBOOK
    // ==============================================================================
    const tabButtons = document.querySelectorAll('.tab-btn');
    const previewCards = document.querySelectorAll('.preview-item-card');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            tabButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const category = btn.getAttribute('data-category');

            previewCards.forEach(card => {
                const cardCat = card.getAttribute('data-category');
                if (category === 'todos' || cardCat === category) {
                    card.style.display = 'flex';
                    card.style.animation = 'fadeInCard 0.4s ease';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    // ==============================================================================
    // 4. ACORDEÃO DO FAQ (PERGUNTAS FREQUENTES)
    // ==============================================================================
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const questionBtn = item.querySelector('.faq-question');

        if (questionBtn) {
            questionBtn.addEventListener('click', () => {
                const isActive = item.classList.contains('active');

                // Fecha outros itens para foco limpo
                faqItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove('active');
                        const otherBtn = otherItem.querySelector('.faq-question');
                        if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
                    }
                });

                // Alterna o item atual
                if (isActive) {
                    item.classList.remove('active');
                    questionBtn.setAttribute('aria-expanded', 'false');
                } else {
                    item.classList.add('active');
                    questionBtn.setAttribute('aria-expanded', 'true');
                }
            });
        }
    });

    // ==============================================================================
    // 5. FEEDBACK DE MODO DEMONSTRAÇÃO DO CHECKOUT
    // ==============================================================================
    const checkoutButtons = document.querySelectorAll('.checkout-btn');
    const checkoutNotice = document.getElementById('checkoutNotice');

    checkoutButtons.forEach(btn => {
        const href = btn.getAttribute('href') || '';
        if (href.includes('COLE_SEU_LINK_DA_KIWIFY_AQUI')) {
            if (checkoutNotice) {
                checkoutNotice.style.display = 'flex';
            }
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                alert('⚙️ CONFIGURAÇÃO DE CHECKOUT:\n\nAbra o arquivo "config.py" no diretório do projeto e substitua a variável CHECKOUT_URL pelo link real da sua página de pagamento na Kiwify/Hotmart.\n\nDepois disso, todos os botões do site redirecionarão seus clientes automaticamente!');
            });
        }
    });

    // Fecha modal Lightbox com tecla ESC
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeLightbox();
        }
    });
});

// ==============================================================================
// 6. FUNÇÕES GLOBAIS DO LIGHTBOX MODAL
// ==============================================================================
function openLightbox(imgSrc, title, desc) {
    const modal = document.getElementById('pageLightbox');
    const modalImg = document.getElementById('lightboxImg');
    const modalTitle = document.getElementById('lightboxTitle');
    const modalDesc = document.getElementById('lightboxDesc');

    if (modal && modalImg && modalTitle && modalDesc) {
        modalImg.src = imgSrc;
        modalTitle.textContent = title;
        modalDesc.textContent = desc;
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }
}

function closeLightbox() {
    const modal = document.getElementById('pageLightbox');
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
}
