# 📝 Git команды для деплоя

## 🚀 Быстрая загрузка на GitHub

Скопируйте и выполните эти команды по порядку:

```bash
# 1. Перейдите в папку site-deploy
cd site-deploy

# 2. Инициализируйте Git репозиторий
git init

# 3. Добавьте все файлы
git add .

# 4. Проверьте что добавлено
git status

# 5. Создайте первый коммит
git commit -m "Initial commit: TOP AGENCY website - ready for Vercel"

# 6. Переименуйте ветку в main
git branch -M main
```

---

## 🔗 Подключение к GitHub

### Вариант 1: Создать новый репозиторий

1. **Откройте [github.com/new](https://github.com/new)**
2. **Название:** `top-agency` (или любое другое)
3. **Описание:** `TOP AGENCY - Professional SEO Agency Website`
4. **Публичный или приватный:** Выберите по желанию
5. **НЕ добавляйте:** README, .gitignore, license (они уже есть)
6. **Нажмите "Create repository"**

После создания, GitHub покажет вам URL репозитория. Скопируйте его.

### Вариант 2: Команды для подключения

```bash
# Добавьте удаленный репозиторий (замените YOUR_USERNAME и YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Проверьте подключение
git remote -v

# Загрузите на GitHub
git push -u origin main
```

**Пример:**
```bash
git remote add origin https://github.com/topagency/website.git
git push -u origin main
```

---

## ⚠️ Если возникла ошибка

### Ошибка: "Authentication failed"

**Решение:** Используйте Personal Access Token вместо пароля:

1. **Создайте токен:** [github.com/settings/tokens](https://github.com/settings/tokens)
2. **Нажмите:** "Generate new token (classic)"
3. **Название:** "TOP AGENCY Deploy"
4. **Права:** Выберите `repo` (полный доступ к репозиториям)
5. **Нажмите:** "Generate token"
6. **ВАЖНО:** Скопируйте токен (он больше не появится!)

При push используйте токен вместо пароля:
```bash
Username: ваш-username
Password: вставьте-токен
```

### Ошибка: "Large files detected"

GitHub не принимает файлы больше 100 МБ.

**Решение:**
```bash
# Найдите большие файлы
find . -type f -size +50M

# Добавьте их в .gitignore
echo "large-file.jpg" >> .gitignore

# Удалите из индекса
git rm --cached large-file.jpg

# Закоммитьте снова
git add .
git commit -m "Remove large files"
git push
```

---

## 🔄 Обновление сайта

Когда вы внесли изменения:

```bash
# 1. Проверьте что изменилось
git status

# 2. Добавьте измененные файлы
git add .

# 3. Создайте коммит с описанием
git commit -m "Update: описание изменений"

# 4. Загрузите на GitHub
git push
```

**Примеры хороших коммитов:**
```bash
git commit -m "Fix: исправлена форма контактов"
git commit -m "Update: обновлены цены на услуги"
git commit -m "Add: добавлена новая страница кейса"
git commit -m "Style: улучшен дизайн кнопок"
```

---

## 📋 Полезные команды

```bash
# Посмотреть историю коммитов
git log --oneline --graph --all

# Посмотреть изменения в файле
git diff имя-файла.html

# Отменить изменения в файле (до commit)
git checkout -- имя-файла.html

# Отменить последний коммит (сохранив изменения)
git reset --soft HEAD~1

# Посмотреть все ветки
git branch -a

# Создать новую ветку
git checkout -b feature/новая-функция

# Переключиться на другую ветку
git checkout main

# Слить ветку в main
git checkout main
git merge feature/новая-функция
```

---

## 🏷️ Версионирование (Tags)

Рекомендую создавать теги для важных версий:

```bash
# Создать тег для первой версии
git tag -a v1.0.0 -m "Version 1.0.0: Initial release"

# Загрузить теги на GitHub
git push --tags

# Посмотреть все теги
git tag -l

# Перейти к определенной версии
git checkout v1.0.0
```

---

## 🔍 Проверка перед push

```bash
# 1. Проверьте что все файлы добавлены
git status

# 2. Проверьте что .gitignore работает
git ls-files

# 3. Проверьте размер репозитория
du -sh .git

# 4. Проверьте что нет чувствительных данных
grep -r "password\|secret\|api_key" .

# 5. Только после проверки - push
git push
```

---

## 📚 Структура коммитов

Используйте префиксы для лучшей организации:

- `feat:` - новая функция
- `fix:` - исправление бага
- `docs:` - изменения в документации
- `style:` - изменения стилей
- `refactor:` - рефакторинг кода
- `test:` - добавление тестов
- `chore:` - обновление зависимостей

**Примеры:**
```bash
git commit -m "feat: добавлена форма подписки на рассылку"
git commit -m "fix: исправлена отправка формы в Safari"
git commit -m "docs: обновлена инструкция по деплою"
git commit -m "style: улучшен адаптив на мобильных"
```

---

## 🎯 После загрузки на GitHub

1. **Проверьте:** Репозиторий доступен на `github.com/YOUR_USERNAME/YOUR_REPO`
2. **Переходите к:** [DEPLOY-INSTRUCTIONS.md](DEPLOY-INSTRUCTIONS.md)
3. **Следующий шаг:** Подключение к Vercel

---

**Удачного деплоя! 🚀**

