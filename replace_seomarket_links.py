#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для замены ссылок seomarket.ua на top-agency.online
"""

import os
import re
from pathlib import Path

# Список файлов для обработки
FILES_TO_PROCESS = [
    "en/blog/main-types-of-content-and-how-to-properly-format-them/index.html",
    "en/services/advertising-account-audit/index.html",
    "en/services/advertising-in-price-aggregators/index.html",
    "en/services/advertising-on-telegram/index.html",
    "en/services/analytics-settings/index.html",
    "en/services/application-and-site-testing/index.html",
    "en/services/application-development/index.html",
    "en/services/audit-of-advertising-accounts/index.html",
    "en/services/backlink-audit-of-the-website/index.html",
    "en/services/call-tracking/index.html",
    "en/services/chatbot-development/index.html",
    "en/services/competitor-analysis-and-dynamics/index.html",
    "en/services/consulting/index.html",
    "en/services/content-marketing/index.html",
    "en/services/contextual-advertising-dnipro/index.html",
    "en/services/contextual-advertising-kharkiv/index.html",
    "en/services/contextual-advertising-kyiv/index.html",
    "en/services/contextual-advertising-odesa/index.html",
    "en/services/contextual-advertising/index.html",
    "en/services/creating-technical-specifications-for-texts/index.html",
    "en/services/crowd-marketing/index.html",
    "en/services/design-and-development/index.html",
    "en/services/display-advertising/index.html",
    "en/services/e-commerce-setup/index.html",
    "en/services/facebook-advertising-replenishment-with-vat/index.html",
    "en/services/facebook-advertising/index.html",
    "en/services/ga4-audit/index.html",
    "en/services/goals-setup/index.html",
    "en/services/google-ads-audit/index.html",
    "en/services/google-shopping/index.html",
    "en/services/gtm-setup/index.html",
    "en/services/instagram-advertising/index.html",
    "en/services/keyword-research/index.html",
    "en/services/link-building/index.html",
    "en/services/linkedin-advertising/index.html",
    "en/services/mobile-advertising/index.html",
    "en/services/mobile-aso/index.html",
    "en/services/ppc-consultation/index.html",
    "en/services/pr-rozmishhennya/index.html",
    "en/services/promotion-dnipro/index.html",
    "en/services/promotion-kharkiv/index.html",
    "en/services/promotion-kryvyi-rih/index.html",
    "en/services/promotion-kyiv/index.html",
    "en/services/promotion-lutsk/index.html",
    "en/services/promotion-lviv/index.html",
    "en/services/promotion-odesa/index.html",
    "en/services/promotion-of-applications-and-games/index.html",
    "en/services/promotion-vinnytsia/index.html",
    "en/services/promotion-zaporizhzhia/index.html",
    "en/services/promotion-zhytomyr/index.html",
    "en/services/search-engine-advertising/index.html",
    "en/services/seo-at-the-development-stage/index.html",
    "en/services/seo-consultation/index.html",
    "en/services/seo-copywriting/index.html",
    "en/services/seo-for-search-chat-gpt-ai/index.html",
    "en/services/seo-promotion/index.html",
    "en/services/seo-writing/index.html",
    "en/services/serm/index.html",
    "en/services/targeted-advertising-on-social-networks/index.html",
    "en/services/technical-seo-audit/index.html",
    "en/services/text-translation-and-adaptation/index.html",
    "en/services/tiktok-advertising/index.html",
    "en/services/ux-audit/index.html",
    "en/services/web-analytics/index.html",
    "en/services/web-design-creatives-banners/index.html",
    "en/services/website-development/index.html",
    "en/services/website-structure-development/index.html",
    "en/services/youtube-video-advertising/index.html",
]

def replace_seomarket_links(content):
    """Заменяет все ссылки на seomarket.ua на top-agency.online"""
    original_content = content
    
    # Замена https://seomarket.ua/en/services/... на https://www.top-agency.online/en/services/...
    content = re.sub(
        r'https://seomarket\.ua/en/services/([^"\s<>]*)',
        r'https://www.top-agency.online/en/services/\1',
        content
    )
    
    # Замена https://seomarket.ua/en/#website на https://www.top-agency.online/en/#website
    content = re.sub(
        r'https://seomarket\.ua/en/(#website)',
        r'https://www.top-agency.online/en/\1',
        content
    )
    
    # Замена битых ссылок типа https://seomarket.ua/ruhttps://seomarket.ua/en/services/...
    content = re.sub(
        r'https://seomarket\.ua/ruhttps://seomarket\.ua/en/services/([^"\s<>]*)',
        r'https://www.top-agency.online/en/services/\1',
        content
    )
    
    # Замена http://seomarket.ua/en/services/... на https://www.top-agency.online/en/services/...
    content = re.sub(
        r'http://seomarket\.ua/en/services/([^"\s<>]*)',
        r'https://www.top-agency.online/en/services/\1',
        content
    )
    
    # Замена без https:// - seomarket.ua/en/services/...
    content = re.sub(
        r'(?<!https://)(?<!http://)seomarket\.ua/en/services/([^"\s<>]*)',
        r'https://www.top-agency.online/en/services/\1',
        content
    )
    
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
        # Заменяем ссылки
        content = replace_seomarket_links(content)
        
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
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    print("🚀 Начинаю замену ссылок seomarket.ua на top-agency.online...\n")
    
    for file_path in FILES_TO_PROCESS:
        result = process_file(file_path)
        if result:
            updated_count += 1
        elif result is False and "не найден" in str(result):
            skipped_count += 1
        elif result is False:
            error_count += 1
    
    print(f"\n📊 Результаты:")
    print(f"   ✅ Обновлено: {updated_count}")
    print(f"   ⏭️  Пропущено: {skipped_count}")
    print(f"   ❌ Ошибок: {error_count}")
    print(f"   📁 Всего файлов: {len(FILES_TO_PROCESS)}")

if __name__ == "__main__":
    main()

