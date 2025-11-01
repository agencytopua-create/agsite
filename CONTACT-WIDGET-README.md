# Contact Widget - TOP AGENCY 📞

Красивый, современный и динамичный виджет для связи через Telegram и Viber.

## ✨ Особенности

- 🎨 **Современный дизайн** в стиле TOP AGENCY
- 📱 **Адаптивный** - отлично работает на всех устройствах
- 🎭 **Плавные анимации** - пульсация кнопки, появление панели
- ⚡ **Легковесный** - минимальное влияние на скорость загрузки
- 🔒 **Безопасный** - правильные ссылки, noopener, noreferrer
- ♿ **Доступность** - поддержка клавиатурной навигации
- 🌙 **Темная тема** - красиво выглядит на темном фоне
- 📊 **Аналитика готовна** - легко добавить отслеживание кликов

## 🚀 Быстрый старт

### Вариант 1: Standalone HTML (для тестирования)

Просто откройте `contact-widget.html` в браузере.

### Вариант 2: Интеграция в существующий сайт

1. Скопируйте файлы `contact-widget.css` и `contact-widget.js` в ваш проект
2. Добавьте подключение в `<head>` вашего HTML:

```html
<link rel="stylesheet" href="contact-widget.css">
```

3. Добавьте подключение JavaScript перед закрывающим `</body>`:

```html
<script src="contact-widget.js"></script>
<div id="contactWidget"></div>
```

Готово! Виджет автоматически создастся и появится в правом нижнем углу.

## ⚙️ Кастомизация

### Изменение контактов

Отредактируйте файл `contact-widget.js`, найдите секцию `config`:

```javascript
const config = {
    telegram: '@Blastermannn',     // Ваш Telegram username
    viber: '+380934797577',         // Ваш Viber номер
    position: 'bottom-right',       // Позиция: 'bottom-right' или 'bottom-left'
    showOnScroll: true,             // Скрывать при прокрутке вниз
    animationSpeed: 400             // Скорость анимаций (мс)
};
```

### Изменение цветов

Откройте `contact-widget.css` и найдите переменные цветов:

- Основной цвет (зеленый): `#52b936`
- Telegram: `#0088cc`
- Viber: `#665cac`

### Изменение размера кнопки

В файле `contact-widget.css` найдите `.widget-button`:

```css
.widget-button {
    width: 70px;   /* Измените размер */
    height: 70px;
}
```

## 📁 Структура файлов

```
├── contact-widget.html       # Standalone версия для тестирования
├── contact-widget.css        # Стили виджета
├── contact-widget.js         # Логика и функционал
└── CONTACT-WIDGET-README.md  # Документация (этот файл)
```

## 🎯 Интеграция в разные страницы

### Украинская версия (index.html)

```html
<link rel="stylesheet" href="contact-widget.css">
<script src="contact-widget.js"></script>
<div id="contactWidget"></div>
```

### Английская версия (en/)

То же самое. Виджет универсален.

### Русская версия (ru/)

То же самое.

## 📱 Адаптивность

Виджет автоматически адаптируется под размер экрана:

- **Desktop** (768px+): Полноразмерный виджет
- **Tablet** (481-767px): Компактный виджет
- **Mobile** (до 480px): Уменьшенный виджет

## 🔧 Дополнительные настройки

### Скрытие виджета при прокрутке

По умолчанию включено. Чтобы отключить:

```javascript
window.ContactWidget.config.showOnScroll = false;
```

### Изменение позиции после загрузки

```javascript
// Переместить в левый нижний угол
const widget = document.querySelector('.contact-widget');
widget.classList.remove('bottom-right');
widget.classList.add('bottom-left');
```

### Добавление аналитики

```javascript
// В файле contact-widget.js, в функции initWidget()
document.querySelectorAll('.contact-item').forEach(item => {
    item.addEventListener('click', function() {
        // Google Analytics
        gtag('event', 'click', {
            'event_category': 'Contact Widget',
            'event_label': this.querySelector('.contact-label').textContent
        });
        
        // или Яндекс.Метрика
        ym(XXXXXX, 'reachGoal', 'widget_click');
    });
});
```

## 🐛 Решение проблем

### Виджет не появляется

1. Проверьте, что файлы CSS и JS загружаются
2. Убедитесь, что есть `<div id="contactWidget"></div>`
3. Откройте консоль браузера (F12) и проверьте ошибки

### Кнопка не реагирует на клик

1. Проверьте z-index других элементов на странице
2. Убедитесь, что JavaScript включен в браузере

### Виджет перекрывается другими элементами

Виджет имеет `z-index: 9999`. Если этого мало, увеличьте в CSS:

```css
.contact-widget {
    z-index: 99999 !important;
}
```

## 🌐 Браузерная поддержка

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Opera 76+
- ✅ Mobile Safari (iOS 14+)
- ✅ Chrome Mobile (Android 10+)

## 📈 Производительность

- CSS: ~15KB (минифицированный ~8KB)
- JS: ~7KB (минифицированный ~4KB)
- Иконки: встроенные SVG (0KB дополнительно)
- **Итого**: ~12KB минифицированный

## 🔐 Безопасность

- Все внешние ссылки имеют `target="_blank"`
- Добавлены `rel="noopener noreferrer"`
- Нет внешних зависимостей
- Нет сбора данных о пользователях

## 📝 Лицензия

Этот виджет создан специально для TOP AGENCY и может быть использован в проектах агентства.

## 🤝 Поддержка

Если у вас есть вопросы или предложения по улучшению виджета, обращайтесь к команде разработки.

---

**Версия:** 1.0.0  
**Дата создания:** 2025  
**Автор:** TOP AGENCY Development Team

