# TOP AGENCY Website

Профессиональное SEO агенство с более чем 15 летним опытом работы.

## 🚀 Особенности

- ✅ Статический HTML сайт (экспорт из WordPress)
- 🌍 Мультиязычность: Русский (по умолчанию), Украинский, Английский
- 📧 Интеграция с Web3Forms для обработки форм
- 📱 Адаптивный дизайн
- ⚡ Быстрая загрузка
- 🎨 Современный UI/UX

## 📁 Структура проекта

```
site-deploy/
├── index.html              # Главная (украинский)
├── ru/                     # Русская версия
│   ├── index.html
│   ├── kontakty/
│   ├── services/
│   ├── blog/
│   └── thank-you/
├── en/                     # Английская версия
│   ├── index.html
│   ├── contacts/
│   ├── services/
│   ├── blog/
│   └── thank-you/
├── wp-content/uploads/     # Изображения
├── web3forms-integration.js # Обработчик форм
└── vercel.json             # Конфигурация Vercel
```

## 🔧 Технологии

- **HTML5** - разметка
- **CSS3** - стили (встроены в HTML)
- **JavaScript** - интерактивность и обработка форм
- **Web3Forms** - обработка форм без бэкенда
- **Vercel** - хостинг и деплой

## 📧 Обработка форм

Формы на сайте отправляются через [Web3Forms](https://web3forms.com):
- Access Key: `cc8100b9-c892-4d69-b444-04bd73ef8884`
- Email получателя: `agencytopua@gmail.com`
- После отправки формы пользователь перенаправляется на страницу благодарности

## 🌍 Языковые версии

### Русская (по умолчанию)
- URL: `/ru/`
- Автоматический редирект с `/` на `/ru/`

### Украинская
- URL: `/`
- Базовая версия сайта

### Английская
- URL: `/en/`
- Для международной аудитории

## 🚀 Деплой на Vercel

### Быстрый старт

1. **Залейте на GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: TOP AGENCY website"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Подключите к Vercel:**
   - Зайдите на [vercel.com](https://vercel.com)
   - Нажмите "New Project"
   - Импортируйте ваш GitHub репозиторий
   - Vercel автоматически определит настройки
   - Нажмите "Deploy"

3. **Готово!** 🎉
   Ваш сайт будет доступен на Vercel домене

### Настройка собственного домена

В настройках проекта Vercel:
1. Settings → Domains
2. Добавьте ваш домен
3. Настройте DNS записи согласно инструкциям Vercel

## 📝 Важные файлы

### `web3forms-integration.js`
Обрабатывает отправку форм:
- Перехватывает submit форм
- Фильтрует служебные поля WordPress
- Переименовывает поля для Web3Forms
- Отправляет данные на API
- Перенаправляет на страницу благодарности

### `vercel.json`
Конфигурация для Vercel:
- Редирект `/` → `/ru/`
- Заголовки безопасности
- Правила маршрутизации

## 🔒 Безопасность

- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- X-XSS-Protection: 1; mode=block

## 📱 Контакты

- Email: agencytopua@gmail.com
- Все формы на сайте отправляются на этот email

## 📄 Лицензия

Все права защищены © TOP AGENCY

---

**Сделано с ❤️ для TOP AGENCY**

