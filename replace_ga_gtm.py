#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для замены кода Google Analytics и Google Tag Manager во всех HTML файлах
"""

import os
import re
from pathlib import Path

# Новый код Google tag (gtag.js)
NEW_GTAG_CODE = '''<!-- Google tag (gtag.js) -->

<script async src="https://www.googletagmanager.com/gtag/js?id=AW-17579677343"></script>

<script>

  window.dataLayer = window.dataLayer || [];

  function gtag(){dataLayer.push(arguments);}

  gtag('js', new Date());



  gtag('config', 'AW-17579677343');

</script>

	

<!-- Google Tag Manager -->

<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':

new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],

j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=

'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);

})(window,document,'script','dataLayer','GTM-K4T4HRJ9');</script>

<!-- End Google Tag Manager -->'''

# Новый noscript код
NEW_NOSCRIPT_CODE = '''<!-- Google Tag Manager (noscript) -->

<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-K4T4HRJ9"

height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<!-- End Google Tag Manager (noscript) -->'''

def replace_gtm_in_head(content):
    """Заменяет GTM код в <head>"""
    # Сначала проверяем, есть ли уже новый код
    if 'GTM-K4T4HRJ9' in content and 'AW-17579677343' in content:
        return content
    
    # Ищем GTM код с любым ID и заменяем
    # Паттерн для полного блока GTM в head (более гибкий, учитывает любые пробелы и табы)
    gtm_pattern = r'<!--\s*Google\s+Tag\s+Manager\s*-->[\s\S]*?<!--\s*End\s+Google\s+Tag\s+Manager\s*-->'
    
    # Заменяем весь блок GTM на новый код (включая gtag)
    new_content = re.sub(gtm_pattern, NEW_GTAG_CODE, content, flags=re.DOTALL | re.IGNORECASE)
    
    # Если замена произошла, используем новый контент
    if new_content != content:
        content = new_content
    # Если GTM код не найден в формате с комментариями, ищем просто скрипт
    elif 'GTM-K4T4HRJ9' not in content:
        # Ищем GTM скрипт с любым ID (более гибкий паттерн)
        gtm_script_pattern = r"<script>[\s\S]*?\(function\(w,d,s,l,i\)\{[\s\S]*?GTM-[A-Z0-9]+[\s\S]*?</script>"
        content = re.sub(gtm_script_pattern, NEW_GTAG_CODE, content, flags=re.DOTALL | re.IGNORECASE)
    
    return content

def replace_gtm_noscript(content):
    """Заменяет GTM noscript код в <body>"""
    # Проверяем, есть ли уже новый noscript код
    if 'GTM-K4T4HRJ9' in content and 'ns.html?id=GTM-K4T4HRJ9' in content:
        return content
    
    # Паттерны для noscript версии (с разными вариантами форматирования, более гибкие)
    patterns = [
        # С комментариями (гибкий паттерн для любых пробелов)
        r'<!--\s*Google\s+Tag\s+Manager\s*\(noscript\)\s*-->[\s\S]*?<!--\s*End\s+Google\s+Tag\s+Manager\s*\(noscript\)\s*-->',
        # Iframe с GTM ID в noscript
        r'<noscript>[\s\S]*?<iframe[^>]*?GTM-[A-Z0-9]+[^>]*?>[\s\S]*?</iframe>[\s\S]*?</noscript>',
        # Iframe с data-src и GTM ID
        r'<noscript>[\s\S]*?<iframe[^>]*?data-src[^>]*?GTM-[A-Z0-9]+[^>]*?>[\s\S]*?</iframe>[\s\S]*?</noscript>',
    ]
    
    for pattern in patterns:
        new_content = re.sub(pattern, NEW_NOSCRIPT_CODE, content, flags=re.DOTALL | re.IGNORECASE)
        if new_content != content:
            content = new_content
            break
    
    return content

def replace_old_ga_code(content):
    """Удаляет старый код Google Analytics, если он есть"""
    # Паттерны для старого GA кода
    ga_patterns = [
        r'<!--\s*Google\s+Analytics[^>]*-->.*?<!--\s*End\s+Google\s+Analytics[^>]*-->',
        r'<script[^>]*google-analytics[^>]*>.*?</script>',
        r'<script[^>]*gtag\([^>]*>.*?</script>',
    ]
    
    for pattern in ga_patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    return content

def process_file(file_path):
    """Обрабатывает один файл"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Проверяем, есть ли уже новый код
        if 'AW-17579677343' in content and 'GTM-K4T4HRJ9' in content:
            # Код уже обновлен
            return False
        
        # Удаляем старый GA код
        content = replace_old_ga_code(content)
        
        # Заменяем GTM в head
        content = replace_gtm_in_head(content)
        
        # Заменяем noscript в body
        content = replace_gtm_noscript(content)
        
        # Если изменения были сделаны, сохраняем файл
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    except Exception as e:
        print(f"Ошибка при обработке {file_path}: {e}")
        return False

def main():
    """Главная функция"""
    # Читаем список файлов
    files_list_path = 'ga_gtm_files_list.txt'
    
    if not os.path.exists(files_list_path):
        print(f"Файл {files_list_path} не найден!")
        return
    
    with open(files_list_path, 'r', encoding='utf-8') as f:
        files = [line.strip() for line in f if line.strip()]
    
    print(f"Найдено файлов для обработки: {len(files)}")
    
    processed = 0
    updated = 0
    errors = 0
    
    for file_path in files:
        # Убираем ./ в начале пути
        file_path = file_path.lstrip('./')
        
        if not os.path.exists(file_path):
            print(f"Файл не найден: {file_path}")
            errors += 1
            continue
        
        processed += 1
        if process_file(file_path):
            updated += 1
            if updated % 50 == 0:
                print(f"Обработано: {processed}, Обновлено: {updated}")
    
    print(f"\nГотово!")
    print(f"Всего обработано: {processed}")
    print(f"Обновлено: {updated}")
    print(f"Ошибок: {errors}")

if __name__ == '__main__':
    main()

