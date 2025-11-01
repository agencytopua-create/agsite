/**
 * Contact Widget - TOP AGENCY
 * Красивый динамичный виджет для связи
 * 
 * Использование:
 * 1. Подключите CSS: <link rel="stylesheet" href="contact-widget.css">
 * 2. Подключите JS: <script src="contact-widget.js"></script>
 * 3. Добавьте HTML: <div id="contactWidget"></div>
 */

(function() {
    'use strict';

    // Конфигурация виджета
    const config = {
        telegram: '@Blastermannn',
        viber: '+380934797577',
        position: 'bottom-right', // bottom-right, bottom-left
        showOnScroll: true, // Скрывать при прокрутке вниз
        animationSpeed: 400
    };

    // HTML шаблон виджета
    const widgetHTML = `
        <!-- Dark Overlay -->
        <div class="contact-overlay" id="contactOverlay"></div>

        <!-- Contact Widget -->
        <div class="contact-widget ${config.position}">
            <!-- Contact Panel -->
            <div class="contact-panel" id="contactPanel">
                <div class="panel-header">
                    <div class="panel-title">Зв'яжіться з нами</div>
                    <div class="panel-subtitle">Оберіть зручний спосіб зв'язку</div>
                </div>
                
                <div class="contact-items">
                    <!-- Telegram -->
                    <a href="https://t.me/${config.telegram.replace('@', '')}" target="_blank" class="contact-item" rel="noopener noreferrer">
                        <div class="contact-icon telegram">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.568 8.16l-1.584 7.464c-.119.606-.427.755-.867.471l-2.395-1.765-1.154 1.109c-.131.131-.24.24-.491.24l.174-2.462 4.444-4.008c.194-.17-.042-.264-.3-.096l-5.488 3.458-2.365-.736c-.514-.16-.528-.514.107-.781l9.257-3.568c.431-.162.809.101.668.682z"/>
                            </svg>
                        </div>
                        <div class="contact-info">
                            <div class="contact-label">Telegram</div>
                            <div class="contact-value">${config.telegram}</div>
                        </div>
                        <div class="contact-arrow">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <line x1="7" y1="17" x2="17" y2="7"></line>
                                <polyline points="7 7 17 7 17 17"></polyline>
                            </svg>
                        </div>
                    </a>

                    <!-- Viber -->
                    <a href="viber://chat?number=${config.viber.replace(/\s/g, '')}" class="contact-item">
                        <div class="contact-icon viber">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M13.772 0c-3.706 0-6.74 1.933-6.74 4.323 0 .641.196 1.234.515 1.764l-2.01 6.31 6.788-2.085c.48.25 1.016.388 1.58.388.396 0 .78-.06 1.14-.17C12.87 12.844 12 11.726 12 10.353c0-2.69 2.954-4.84 6.62-4.84.408 0 .806.036 1.193.103-1.177-2.154-4.822-5.616-9.041-5.616zm-2.154 11.944c-.146.097-.489-.036-.915-.247-2.793-1.356-4.728-4.039-4.728-4.039s-.27-.295.143-.53c.412-.236 1.016-.412 1.016-.412s.39-.136.694.097c.228.171.519.445.969.9.889.889 1.093.59 1.127.512.034-.078.385-1.548.768-2.498.173-.435.246-.523.451-.523.205 0 .689-.068.689-.068s-.756 0-1.37.078c-.615.078-.837.153-1.201.477-.362.323-1.42 1.479-1.42 3.622 0 2.143.835 2.643 1.046 2.841.211.198.334.074.539-.049l1.259-.747zm8.204.499l-.197.221c-.206.228-.59.584-.984.972-2.164 2.037-5.179 2.22-6.926 1.992-.568-.074-1.219-.172-1.811-.235-.314-.034-.688-.074-1.025-.074-.062 0-.103 0-.103.059 0 .059-.034.068-.034.127-.062.244-.429.46-.668.667-.327.284-.837.695-1.015 1.045-.178.35-.196.612-.196.612s.597-.051.985-.145c.388-.094.82-.246 1.252-.416.432-.17.846-.377 1.252-.589.095-.049.197-.107.304-.171.8-.472 1.433-.994 1.926-1.421l-.59-.726c-.595-.724-1.046-1.467-1.046-2.275 0-.832.456-1.675 1.065-2.448l.194-.072c1.318.723 2.682 1.256 4.073 1.768.486.179.694.652.514 1.138zm.798 0c-.197.323-.549.587-.984.972-1.63 1.782-4.023 2.12-5.721 1.842-.568-.089-1.164-.195-1.77-.265-.314-.034-.678-.078-1.02-.078 0 0-.062 0-.062.059s-.034.068-.068.127c-.034.244-.411.478-.678.667-.327.244-.825.712-.985 1.045-.179.35-.205.612-.205.612s.594-.051.985-.145c.388-.094.82-.246 1.251-.416.432-.17.846-.377 1.252-.589.105-.049.207-.107.314-.171.806-.472 1.439-.994 1.932-1.421l-.624-.726c-.605-.724-1.067-1.467-1.067-2.275 0-.832.45-1.675 1.059-2.448l.23-.072c1.323.723 2.692 1.256 4.087 1.768.494.179.702.652.514 1.138l-.197.323"/>
                            </svg>
                        </div>
                        <div class="contact-info">
                            <div class="contact-label">Viber</div>
                            <div class="contact-value">${config.viber}</div>
                        </div>
                        <div class="contact-arrow">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <line x1="7" y1="17" x2="17" y2="7"></line>
                                <polyline points="7 7 17 7 17 17"></polyline>
                            </svg>
                        </div>
                    </a>
                </div>
            </div>

            <!-- Widget Button -->
            <button class="widget-button" id="contactWidgetButton">
                <div class="widget-icon">
                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" id="contactIconSvg">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                    </svg>
                </div>
            </button>
        </div>
    `;

    // Создание виджета
    function createWidget() {
        const widgetContainer = document.getElementById('contactWidget') || document.body;
        widgetContainer.insertAdjacentHTML('beforeend', widgetHTML);

        initWidget();
    }

    // Инициализация виджета
    function initWidget() {
        const widgetButton = document.getElementById('contactWidgetButton');
        const contactPanel = document.getElementById('contactPanel');
        const overlay = document.getElementById('contactOverlay');
        const iconSvg = document.getElementById('contactIconSvg');

        // Toggle function
        function toggleWidget() {
            const isActive = widgetButton.classList.contains('active');
            
            if (isActive) {
                closeWidget();
            } else {
                openWidget();
            }
        }

        function openWidget() {
            widgetButton.classList.add('active');
            contactPanel.classList.add('show');
            overlay.classList.add('show');
            changeIcon('close');
        }

        function closeWidget() {
            widgetButton.classList.remove('active');
            contactPanel.classList.remove('show');
            overlay.classList.remove('show');
            changeIcon('message');
        }

        // Change icon
        function changeIcon(type) {
            if (type === 'message') {
                iconSvg.innerHTML = `<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>`;
            } else if (type === 'close') {
                iconSvg.innerHTML = `<path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>`;
            }
        }

        // Event listeners
        widgetButton.addEventListener('click', toggleWidget);
        overlay.addEventListener('click', closeWidget);

        // Close on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && contactPanel.classList.contains('show')) {
                closeWidget();
            }
        });

        // Prevent panel click from closing
        contactPanel.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        // Animation on scroll (if enabled)
        if (config.showOnScroll) {
            let lastScroll = 0;
            const widget = document.querySelector('.contact-widget');
            
            window.addEventListener('scroll', () => {
                const currentScroll = window.pageYOffset;
                
                if (currentScroll > lastScroll && currentScroll > 100) {
                    // Scrolling down
                    widget.style.transform = 'translateY(calc(100% + 30px))';
                    widget.style.opacity = '0';
                } else {
                    // Scrolling up
                    widget.style.transform = 'translateY(0)';
                    widget.style.opacity = '1';
                }
                lastScroll = currentScroll;
            });
        }
    }

    // Инициализация при загрузке DOM
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', createWidget);
    } else {
        createWidget();
    }

    // Экспорт для кастомизации
    window.ContactWidget = {
        config: config,
        updateConfig: function(newConfig) {
            Object.assign(config, newConfig);
        }
    };

})();

