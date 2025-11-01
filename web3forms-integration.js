// Web3Forms Integration Script
// Automatically handles all forms on the site

(function() {
    'use strict';
    
    // Определение языка страницы для редиректа
    function getThankYouUrl() {
        const lang = document.documentElement.lang;
        const path = window.location.pathname;
        
        if (path.includes('/ru/')) {
            return '/ru/thank-you/';
        } else if (path.includes('/en/')) {
            return '/en/thank-you/';
        } else {
            return '/thank-you/';
        }
    }
    
    // Обработка всех форм Contact Form 7
    function initializeForms() {
        const forms = document.querySelectorAll('.wpcf7-form, form.form');
        
        forms.forEach(function(form) {
            // Пропускаем формы, которые уже обработаны
            if (form.hasAttribute('data-web3forms-initialized')) {
                return;
            }
            
            // Изменяем action и method
            form.setAttribute('action', 'https://api.web3forms.com/submit');
            form.setAttribute('method', 'POST');
            form.setAttribute('data-web3forms-initialized', 'true');
            
            // Удаляем старые скрытые поля Contact Form 7
            const oldFields = form.querySelectorAll('input[name^="_wpcf7"], input[name="honeypot-"]');
            oldFields.forEach(function(field) {
                if (field.parentElement && field.parentElement.classList.contains('honeypot-437-wrap')) {
                    field.parentElement.remove();
                } else if (!field.name.includes('recaptcha')) {
                    field.remove();
                }
            });
            
            // Добавляем Web3Forms access key
            if (!form.querySelector('input[name="access_key"]')) {
                const accessKeyInput = document.createElement('input');
                accessKeyInput.type = 'hidden';
                accessKeyInput.name = 'access_key';
                accessKeyInput.value = 'cc8100b9-c892-4d69-b444-04bd73ef8884';
                form.insertBefore(accessKeyInput, form.firstChild);
            }
            
            // Добавляем subject
            if (!form.querySelector('input[name="subject"]')) {
                const subjectInput = document.createElement('input');
                subjectInput.type = 'hidden';
                subjectInput.name = 'subject';
                subjectInput.value = 'Новая заявка с сайта TOP AGENCY';
                form.insertBefore(subjectInput, form.firstChild);
            }
            
            // Добавляем from_name
            if (!form.querySelector('input[name="from_name"]')) {
                const fromNameInput = document.createElement('input');
                fromNameInput.type = 'hidden';
                fromNameInput.name = 'from_name';
                fromNameInput.value = 'TOP AGENCY Website';
                form.insertBefore(fromNameInput, form.firstChild);
            }
            
            // Добавляем redirect URL (отключаем, будем делать через JS)
            // Web3Forms не всегда корректно работает с redirect в форме
            // if (!form.querySelector('input[name="redirect"]')) {
            //     const redirectInput = document.createElement('input');
            //     redirectInput.type = 'hidden';
            //     redirectInput.name = 'redirect';
            //     redirectInput.value = window.location.origin + getThankYouUrl();
            //     form.insertBefore(redirectInput, form.firstChild);
            // }
            
            // Переименовываем поля для совместимости
            const fieldMappings = {
                'your-name': 'name',
                'your-tel': 'phone',
                'your-email': 'email',
                'your-site': 'website',
                'your-message': 'message',
                'select-services': 'service',
                'ua_phone': 'phone',
                'your-product': 'product',
                'your-sku': 'sku',
                'your-color': 'color',
                'your-size': 'size',
                'your-qty': 'quantity'
            };
            
            Object.keys(fieldMappings).forEach(function(oldName) {
                const field = form.querySelector('[name="' + oldName + '"]');
                if (field && oldName !== fieldMappings[oldName]) {
                    // Сохраняем старое имя в data-атрибуте
                    field.setAttribute('data-original-name', oldName);
                }
            });
            
            // Обработчик отправки формы
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const submitButton = form.querySelector('button[type="submit"], input[type="submit"]');
                const originalButtonText = submitButton ? submitButton.textContent || submitButton.value : '';
                
                // Показываем индикатор загрузки
                if (submitButton) {
                    submitButton.disabled = true;
                    if (submitButton.tagName === 'BUTTON') {
                        submitButton.textContent = 'Отправка...';
                    } else {
                        submitButton.value = 'Отправка...';
                    }
                }
                
                // Собираем данные формы
                const formData = new FormData(form);
                
                // Переименовываем поля Contact Form 7 для Web3Forms
                const oldToNew = {
                    'your-name': 'name',
                    'your-tel': 'phone',
                    'your-email': 'email',
                    'your-site': 'website',
                    'your-message': 'message',
                    'select-services': 'service',
                    'ua_phone': 'phone'
                };
                
                // Создаем новый FormData с правильными именами
                const newFormData = new FormData();
                
                // Копируем все поля, переименовывая где нужно
                for (let [key, value] of formData.entries()) {
                    // Пропускаем служебные поля Contact Form 7 и Akismet
                    if (key.startsWith('_wpcf7') || 
                        key.startsWith('_') || 
                        key === 'honeypot-437' ||
                        key === 'honeypot-439' ||
                        key.includes('_ak_') ||
                        key.includes('file-')) {
                        console.log('⏭️  Пропускаем служебное поле:', key);
                        continue;
                    }
                    
                    // Пропускаем пустые значения
                    if (value === '' || value === null || value === undefined) {
                        console.log('⏭️  Пропускаем пустое поле:', key);
                        continue;
                    }
                    
                    const newKey = oldToNew[key] || key;
                    newFormData.append(newKey, value);
                }
                
                // Проверяем наличие обязательных полей и добавляем если нет
                if (!newFormData.get('access_key')) {
                    newFormData.set('access_key', 'cc8100b9-c892-4d69-b444-04bd73ef8884');
                }
                if (!newFormData.get('subject')) {
                    newFormData.set('subject', 'Новая заявка с сайта TOP AGENCY');
                }
                if (!newFormData.get('from_name')) {
                    newFormData.set('from_name', 'TOP AGENCY Website');
                }
                
                // Логирование для отладки
                console.log('🚀 Отправка формы на Web3Forms...');
                console.log('📧 Email получателя: agencytopua@gmail.com');
                console.log('📦 Отправляемые данные:');
                for (let [key, value] of newFormData.entries()) {
                    console.log(`   ${key}: ${value}`);
                }
                
                // Проверяем наличие обязательных полей
                if (!newFormData.get('access_key')) {
                    console.error('❌ Отсутствует access_key!');
                    alert('Ошибка конфигурации формы. Свяжитесь с администратором.');
                    if (submitButton) {
                        submitButton.disabled = false;
                        if (submitButton.tagName === 'BUTTON') {
                            submitButton.textContent = originalButtonText;
                        } else {
                            submitButton.value = originalButtonText;
                        }
                    }
                    return;
                }
                
                // Отправляем через fetch
                fetch('https://api.web3forms.com/submit', {
                    method: 'POST',
                    body: newFormData
                })
                .then(function(response) {
                    console.log('📡 Ответ от сервера, статус:', response.status);
                    if (!response.ok) {
                        throw new Error('HTTP статус: ' + response.status);
                    }
                    return response.json();
                })
                .then(function(data) {
                    console.log('📦 Данные ответа:', data);
                    
                    if (data.success) {
                        console.log('✅ Форма успешно отправлена!');
                        // Редирект на Thank You страницу
                        window.location.href = window.location.origin + getThankYouUrl();
                    } else {
                        console.error('❌ Ошибка Web3Forms:', data.message);
                        throw new Error(data.message || 'Ошибка отправки формы');
                    }
                })
                .catch(function(error) {
                    console.error('❌ Ошибка при отправке:', error);
                    console.error('Детали ошибки:', error.message);
                    
                    var errorMessage = 'Произошла ошибка при отправке формы.\n\n';
                    errorMessage += 'Детали: ' + error.message + '\n\n';
                    errorMessage += 'Проверьте консоль (F12) для подробностей.';
                    
                    alert(errorMessage);
                    
                    // Восстанавливаем кнопку
                    if (submitButton) {
                        submitButton.disabled = false;
                        if (submitButton.tagName === 'BUTTON') {
                            submitButton.textContent = originalButtonText;
                        } else {
                            submitButton.value = originalButtonText;
                        }
                    }
                });
            });
        });
    }
    
    // Инициализация при загрузке страницы
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeForms);
    } else {
        initializeForms();
    }
    
    // Повторная инициализация для динамически загруженных форм
    if (typeof MutationObserver !== 'undefined') {
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.addedNodes.length) {
                    initializeForms();
                }
            });
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }
})();

