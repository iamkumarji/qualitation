/**
 * QUALITATION - Main JavaScript
 * Beautiful, Interactive & Professional
 */

document.addEventListener('DOMContentLoaded', function() {

    // ============================================
    // MOBILE MENU TOGGLE
    // ============================================
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const navbarMenu = document.getElementById('navbarMenu') || document.getElementById('navbarMiddleMenu');

    if (mobileMenuToggle && navbarMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            navbarMenu.classList.toggle('active');
            document.body.style.overflow = navbarMenu.classList.contains('active') ? 'hidden' : '';

            const icon = this.querySelector('i');
            if (navbarMenu.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideMenu = navbarMenu.contains(event.target);
            const isClickOnToggle = mobileMenuToggle.contains(event.target);

            if (!isClickInsideMenu && !isClickOnToggle && navbarMenu.classList.contains('active')) {
                navbarMenu.classList.remove('active');
                document.body.style.overflow = '';
                const icon = mobileMenuToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });

        // Close menu when window is resized
        window.addEventListener('resize', function() {
            if (window.innerWidth > 992 && navbarMenu.classList.contains('active')) {
                navbarMenu.classList.remove('active');
                document.body.style.overflow = '';
                const icon = mobileMenuToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // ============================================
    // DROPDOWN MENUS (Mobile)
    // ============================================
    const dropdownItems = document.querySelectorAll('.navbar-item.has-dropdown, .navbar-top-item.has-dropdown, .navbar-middle-item.has-dropdown, .navbar-bottom-item.has-dropdown');

    dropdownItems.forEach(item => {
        const link = item.querySelector('a');

        if (link) {
            link.addEventListener('click', function(e) {
                if (window.innerWidth <= 992) {
                    e.preventDefault();

                    dropdownItems.forEach(otherItem => {
                        if (otherItem !== item) {
                            otherItem.classList.remove('dropdown-open');
                        }
                    });

                    item.classList.toggle('dropdown-open');
                }
            });
        }

        window.addEventListener('resize', function() {
            if (window.innerWidth > 992) {
                item.classList.remove('dropdown-open');
            }
        });
    });

    // ============================================
    // SMOOTH SCROLLING
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const headerOffset = 100;
                    const elementPosition = target.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // ============================================
    // SCROLL REVEAL ANIMATIONS
    // ============================================
    const revealElements = document.querySelectorAll(
        '.service-card, .column, .quote-container, .accordion-item, ' +
        '.image-text-content, .heading-block, .paragraph-content, ' +
        '.contact-form, .contact-info'
    );

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Stagger the animation
                setTimeout(() => {
                    entry.target.classList.add('revealed');
                }, index * 100);
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        revealObserver.observe(el);
    });

    // Add revealed class styles
    const style = document.createElement('style');
    style.textContent = `
        .revealed {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);

    // ============================================
    // NAVBAR SCROLL EFFECT
    // ============================================
    const navbarMiddle = document.querySelector('.navbar-middle');
    let lastScrollTop = 0;

    if (navbarMiddle) {
        window.addEventListener('scroll', function() {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

            if (scrollTop > 100) {
                navbarMiddle.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.15)';
                navbarMiddle.style.padding = '0.6rem 0';
            } else {
                navbarMiddle.style.boxShadow = '';
                navbarMiddle.style.padding = '';
            }

            lastScrollTop = scrollTop;
        });
    }

    // ============================================
    // CAROUSEL FUNCTIONALITY
    // ============================================
    const carouselSections = document.querySelectorAll('.carousel-section');

    carouselSections.forEach(carouselSection => {
        const slides = carouselSection.querySelectorAll('.carousel-slide');
        const dots = carouselSection.querySelectorAll('.carousel-dot');
        const prevBtn = carouselSection.querySelector('.carousel-arrow-prev');
        const nextBtn = carouselSection.querySelector('.carousel-arrow-next');

        let currentSlide = 0;
        let autoplayInterval = null;
        let isAnimating = false;

        const autoplay = carouselSection.dataset.autoplay === 'True';
        const autoplaySpeed = parseInt(carouselSection.dataset.autoplaySpeed) || 5000;

        function showSlide(index) {
            if (isAnimating) return;
            isAnimating = true;

            slides.forEach((slide, i) => {
                slide.classList.remove('active', 'prev');
                if (i < index) {
                    slide.classList.add('prev');
                }
            });

            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === index);
            });

            if (slides[index]) {
                slides[index].classList.add('active');
            }

            currentSlide = index;

            setTimeout(() => {
                isAnimating = false;
            }, 800);
        }

        function nextSlide() {
            let next = currentSlide + 1;
            if (next >= slides.length) next = 0;
            showSlide(next);
        }

        function prevSlide() {
            let prev = currentSlide - 1;
            if (prev < 0) prev = slides.length - 1;
            showSlide(prev);
        }

        function startAutoplay() {
            if (autoplay && slides.length > 1) {
                autoplayInterval = setInterval(nextSlide, autoplaySpeed);
            }
        }

        function stopAutoplay() {
            if (autoplayInterval) {
                clearInterval(autoplayInterval);
                autoplayInterval = null;
            }
        }

        function restartAutoplay() {
            stopAutoplay();
            startAutoplay();
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                nextSlide();
                restartAutoplay();
            });
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                prevSlide();
                restartAutoplay();
            });
        }

        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                if (currentSlide !== index) {
                    showSlide(index);
                    restartAutoplay();
                }
            });
        });

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') {
                prevSlide();
                restartAutoplay();
            } else if (e.key === 'ArrowRight') {
                nextSlide();
                restartAutoplay();
            }
        });

        // Touch/swipe support
        let touchStartX = 0;
        let touchEndX = 0;

        carouselSection.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });

        carouselSection.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            const diff = touchStartX - touchEndX;
            const swipeThreshold = 50;

            if (Math.abs(diff) > swipeThreshold) {
                if (diff > 0) {
                    nextSlide();
                } else {
                    prevSlide();
                }
                restartAutoplay();
            }
        }, { passive: true });

        // Pause on hover
        carouselSection.addEventListener('mouseenter', stopAutoplay);
        carouselSection.addEventListener('mouseleave', startAutoplay);

        // Pause when page not visible
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                stopAutoplay();
            } else {
                startAutoplay();
            }
        });

        // Initialize
        if (slides.length > 0) {
            showSlide(0);
            startAutoplay();
        }
    });

    // ============================================
    // TESTIMONIAL SLIDER FUNCTIONALITY
    // ============================================
    const testimonialSliders = document.querySelectorAll('.testimonial-slider-section');

    testimonialSliders.forEach(sliderSection => {
        const slides = sliderSection.querySelectorAll('.testimonial-slide');
        const dots = sliderSection.querySelectorAll('.testimonial-dot');
        const prevBtn = sliderSection.querySelector('.testimonial-arrow-prev');
        const nextBtn = sliderSection.querySelector('.testimonial-arrow-next');

        let currentSlide = 0;
        let autoplayInterval = null;
        let isAnimating = false;

        const autoplay = sliderSection.dataset.autoplay === 'True';
        const autoplaySpeed = parseInt(sliderSection.dataset.speed) || 5000;

        function showSlide(index) {
            if (isAnimating || slides.length <= 1) return;
            isAnimating = true;

            slides.forEach((slide, i) => {
                slide.classList.remove('active', 'prev');
                if (i < index) {
                    slide.classList.add('prev');
                }
            });

            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === index);
            });

            if (slides[index]) {
                slides[index].classList.add('active');
            }

            currentSlide = index;

            setTimeout(() => {
                isAnimating = false;
            }, 500);
        }

        function nextSlide() {
            let next = currentSlide + 1;
            if (next >= slides.length) next = 0;
            showSlide(next);
        }

        function prevSlide() {
            let prev = currentSlide - 1;
            if (prev < 0) prev = slides.length - 1;
            showSlide(prev);
        }

        function startAutoplay() {
            if (autoplay && slides.length > 1) {
                autoplayInterval = setInterval(nextSlide, autoplaySpeed);
            }
        }

        function stopAutoplay() {
            if (autoplayInterval) {
                clearInterval(autoplayInterval);
                autoplayInterval = null;
            }
        }

        function restartAutoplay() {
            stopAutoplay();
            startAutoplay();
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                nextSlide();
                restartAutoplay();
            });
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                prevSlide();
                restartAutoplay();
            });
        }

        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                if (currentSlide !== index) {
                    showSlide(index);
                    restartAutoplay();
                }
            });
        });

        // Touch/swipe support
        let touchStartX = 0;
        let touchEndX = 0;

        sliderSection.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });

        sliderSection.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            const diff = touchStartX - touchEndX;
            const swipeThreshold = 50;

            if (Math.abs(diff) > swipeThreshold) {
                if (diff > 0) {
                    nextSlide();
                } else {
                    prevSlide();
                }
                restartAutoplay();
            }
        }, { passive: true });

        // Pause on hover
        sliderSection.addEventListener('mouseenter', stopAutoplay);
        sliderSection.addEventListener('mouseleave', startAutoplay);

        // Initialize
        if (slides.length > 0) {
            showSlide(0);
            startAutoplay();
        }
    });

    // ============================================
    // ACCORDION FUNCTIONALITY
    // ============================================
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const accordionItem = this.parentElement;
            const isActive = accordionItem.classList.contains('active');

            // Smooth close all items
            document.querySelectorAll('.accordion-item').forEach(item => {
                item.classList.remove('active');
            });

            // Toggle current
            if (!isActive) {
                accordionItem.classList.add('active');

                // Scroll into view if needed
                setTimeout(() => {
                    const rect = accordionItem.getBoundingClientRect();
                    if (rect.top < 100) {
                        window.scrollBy({
                            top: rect.top - 120,
                            behavior: 'smooth'
                        });
                    }
                }, 400);
            }
        });
    });

    // ============================================
    // COUNTER ANIMATION FOR STATS
    // ============================================
    const counters = document.querySelectorAll('.column h2');

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                const text = target.innerText;
                const hasPlus = text.includes('+');
                const hasPercent = text.includes('%');
                const numericValue = parseInt(text.replace(/[^0-9]/g, ''));

                if (!isNaN(numericValue) && numericValue > 0) {
                    animateCounter(target, numericValue, hasPlus, hasPercent);
                }

                counterObserver.unobserve(target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });

    function animateCounter(element, target, hasPlus, hasPercent) {
        let current = 0;
        const increment = target / 50;
        const duration = 2000;
        const stepTime = duration / 50;

        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }

            let display = Math.floor(current);
            if (hasPlus) display += '+';
            if (hasPercent) display += '%';
            if (target === 24 && current >= target) display = '24/7';

            element.innerText = display;
        }, stepTime);
    }

    // ============================================
    // BUTTON RIPPLE EFFECT
    // ============================================
    const buttons = document.querySelectorAll('.btn, .slide-button, .btn-request-quote, .btn-client-portal');

    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');

            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple-effect 0.6s ease-out;
                pointer-events: none;
            `;

            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);

            setTimeout(() => ripple.remove(), 600);
        });
    });

    // Add ripple animation
    const rippleStyle = document.createElement('style');
    rippleStyle.textContent = `
        @keyframes ripple-effect {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(rippleStyle);

    // ============================================
    // PARALLAX EFFECT FOR HERO/CAROUSEL
    // ============================================
    const parallaxElements = document.querySelectorAll('.carousel-section, .hero');

    if (parallaxElements.length > 0 && window.innerWidth > 768) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;

            parallaxElements.forEach(el => {
                const overlay = el.querySelector('.slide-overlay, .hero-overlay');
                if (overlay) {
                    overlay.style.transform = `translateY(${scrolled * 0.3}px)`;
                }
            });
        });
    }

    // ============================================
    // SERVICE CARDS TILT EFFECT
    // ============================================
    const serviceCards = document.querySelectorAll('.service-card');

    if (window.innerWidth > 768) {
        serviceCards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = (y - centerY) / 20;
                const rotateY = (centerX - x) / 20;

                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = '';
            });
        });
    }

    // ============================================
    // ISO STANDARDS NAVBAR ANIMATION
    // ============================================
    const isoItems = document.querySelectorAll('.navbar-bottom-item');

    isoItems.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(10px)';

        setTimeout(() => {
            item.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            item.style.opacity = '1';
            item.style.transform = 'translateY(0)';
        }, 100 + (index * 80));
    });

    // ============================================
    // FORM ENHANCEMENT
    // ============================================
    const formInputs = document.querySelectorAll('.form-input, .form-textarea');

    formInputs.forEach(input => {
        // Floating label effect (if labels exist)
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });

        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentElement.classList.remove('focused');
            }
        });
    });

    // ============================================
    // SCROLL TO TOP FUNCTIONALITY
    // ============================================
    // Create scroll to top button
    const scrollTopBtn = document.createElement('button');
    scrollTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollTopBtn.className = 'scroll-to-top';
    scrollTopBtn.setAttribute('aria-label', 'Scroll to top');
    document.body.appendChild(scrollTopBtn);

    // Add styles
    const scrollTopStyle = document.createElement('style');
    scrollTopStyle.textContent = `
        .scroll-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #2563eb 0%, #7c3aed 100%);
            color: white;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            opacity: 0;
            visibility: hidden;
            transform: translateY(20px);
            transition: all 0.3s ease;
            z-index: 9999;
            box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
        }
        .scroll-to-top.visible {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }
        .scroll-to-top:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(37, 99, 235, 0.5);
        }
    `;
    document.head.appendChild(scrollTopStyle);

    // Show/hide on scroll
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 500) {
            scrollTopBtn.classList.add('visible');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    });

    // Scroll to top on click
    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // ============================================
    // PRELOADER (Optional)
    // ============================================
    window.addEventListener('load', () => {
        document.body.classList.add('loaded');
    });

});
