#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для конвертации цен из UAH (гривны) в USD (доллары США)
Курс: 1 USD = 41.22 UAH (по данным НБУ на 1 ноября 2025)
"""

import os
import re
from pathlib import Path

# Курс обмена (1 USD = 41.22 UAH)
UAH_TO_USD_RATE = 41.22

def round_price(usd_amount):
    """Округляет цену в долларах до разумного значения"""
    if usd_amount >= 1000:
        # Для больших сумм округляем до ближайших 50
        return round(usd_amount / 50) * 50
    elif usd_amount >= 100:
        # Для средних сумм округляем до ближайших 10
        return round(usd_amount / 10) * 10
    elif usd_amount >= 10:
        # Для небольших сумм округляем до ближайшего целого
        return round(usd_amount)
    else:
        # Для очень маленьких сумм округляем до 1 знака после запятой или до ближайшего целого
        rounded = round(usd_amount, 1)
        # Если после округления получается целое число, возвращаем целое
        if rounded == int(rounded):
            return int(rounded)
        return rounded

def format_price(usd_amount):
    """Форматирует цену в долларах для отображения"""
    rounded = round_price(usd_amount)
    if isinstance(rounded, float) and rounded < 1:
        return f"{rounded:.2f}"
    elif isinstance(rounded, float) and rounded < 10:
        return f"{rounded:.1f}"
    elif rounded >= 1000:
        # Форматируем с запятой для тысяч: 1000 -> 1,000
        return f"{rounded:,}".replace(",", ".")
    else:
        return str(int(rounded)) if rounded == int(rounded) else str(rounded)

def extract_number_from_string(text):
    """Извлекает число из строки, обрабатывая разные форматы"""
    # Убираем пробелы и находим число
    # Обрабатываем форматы: 15.000, 15,000, 15000, 500, 30 и т.д.
    
    # Ищем паттерн числа (может быть с точкой или запятой как разделителем тысяч)
    patterns = [
        r'(\d{1,3}(?:\.\d{3})+)',  # 15.000, 10.000
        r'(\d{1,3}(?:,\d{3})+)',   # 15,000, 10,000
        r'(\d+)',                    # 500, 30, 90
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            number_str = match.group(1).replace('.', '').replace(',', '')
            return int(number_str)
    
    # Если не нашли через паттерн, просто ищем все цифры подряд
    digits = re.findall(r'\d+', text)
    if digits:
        # Берем первое большое число (скорее всего это цена)
        numbers = [int(d) for d in digits]
        # Возвращаем самое большое число (обычно это цена)
        return max(numbers) if numbers else None
    
    return None

def convert_uah_to_usd(content):
    """Конвертирует все цены из UAH в USD в содержимом файла"""
    original_content = content
    
    # Паттерн 1: <strong>15.000</strong><span>UAH</span> или <strong>90</strong><span>UAH</span>
    def replace_html_price(match):
        price_str = match.group(1)
        price_uah = extract_number_from_string(price_str)
        if price_uah:
            price_usd = price_uah / UAH_TO_USD_RATE
            formatted_price = format_price(price_usd)
            # Заменяем на доллары
            return f'<strong>{formatted_price}</strong><span>$</span>'
        return match.group(0)
    
    content = re.sub(
        r'<strong>([0-9.,\s]+)</strong>\s*<span>UAH</span>',
        replace_html_price,
        content,
        flags=re.IGNORECASE
    )
    
    # Паттерн 2: В тексте "15,000 UAH" или "90 UAH per 1000 characters"
    def replace_text_price(match):
        full_match = match.group(0)
        price_str = match.group(1)
        price_uah = extract_number_from_string(price_str)
        if price_uah:
            price_usd = price_uah / UAH_TO_USD_RATE
            formatted_price = format_price(price_usd)
            
            # Определяем, был ли разделитель тысяч (точка или запятая)
            had_thousands_sep = '.' in price_str or ',' in price_str
            original_int = int(price_str.replace('.', '').replace(',', '').replace(' ', ''))
            
            # Форматируем результат
            if isinstance(formatted_price, str):
                price_int = int(float(formatted_price.replace('.', '').replace(',', '')))
            else:
                price_int = int(formatted_price)
            
            # Если оригинальная цена была большой и с разделителем, форматируем результат
            if original_int >= 1000 and had_thousands_sep:
                formatted_display = f"{price_int:,}".replace(',', '.')
            else:
                formatted_display = str(formatted_price)
            
            # Заменяем UAH на $
            result = full_match.replace(price_str, formatted_display).replace('UAH', '$').replace('uah', '$')
            return result
        return match.group(0)
    
    # Заменяем "X UAH" в тексте (обрабатываем разные варианты)
    patterns = [
        (r'(\d{1,3}(?:\.\d{3})+)\s*UAH', replace_text_price),     # 15.000 UAH
        (r'(\d{1,3}(?:,\d{3})+)\s*UAH', replace_text_price),       # 15,000 UAH
        (r'(\d{1,3}(?:\s\d{3})+)\s*UAH', replace_text_price),     # 50 000 UAH, 1 000 000 UAH
        (r'(\d+)\s*UAH', replace_text_price),                      # 90 UAH, 500 UAH
    ]
    
    for pattern, replacer in patterns:
        content = re.sub(pattern, replacer, content, flags=re.IGNORECASE)
    
    return content

def process_file(file_path):
    """Обрабатывает один файл"""
    full_path = Path(file_path)
    
    if not full_path.exists():
        print(f"⚠️  Файл не найден: {file_path}")
        return False
    
    try:
        # Читаем файл
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Конвертируем цены
        content = convert_uah_to_usd(content)
        
        # Если были изменения, записываем обратно
        if content != original_content:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Обновлен: {file_path}")
            return True
        else:
            print(f"⏭️  Без изменений: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка при обработке {file_path}: {e}")
        return False

def main():
    """Основная функция"""
    # Читаем список файлов
    files_list_path = Path("uah_files_full_list.txt")
    
    if not files_list_path.exists():
        print("❌ Файл uah_files_full_list.txt не найден!")
        return
    
    with open(files_list_path, 'r', encoding='utf-8') as f:
        files = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    print(f"🚀 Начинаю конвертацию цен из UAH в USD...")
    print(f"📊 Курс обмена: 1 USD = {UAH_TO_USD_RATE} UAH\n")
    
    for file_path in files:
        result = process_file(file_path)
        if result:
            updated_count += 1
        elif result is False and "не найден" in str(result):
            skipped_count += 1
        elif result is False:
            skipped_count += 1
        else:
            error_count += 1
    
    print(f"\n📊 Результаты:")
    print(f"   ✅ Обновлено: {updated_count}")
    print(f"   ⏭️  Пропущено: {skipped_count}")
    print(f"   ❌ Ошибок: {error_count}")
    print(f"   📁 Всего файлов: {len(files)}")

if __name__ == "__main__":
    main()

