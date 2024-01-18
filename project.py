import time
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


bot = telebot.TeleBot ("6366025247:AAHxq1ItTERwWPuRFI1OUhWasEDaS_r4CEg")
last_sent_url=""

while True:
    try:

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.lsm.lv/zinas/latvija/")

        submit_button = driver.find_element(By.XPATH, "//span[@class=' cf1y60' and text()='Pieņemt visus']")
        submit_button.click()

        sort_button = driver.find_element(By.XPATH, "//span[@class='txt-open' and text()='Sadaļas']")
        sort_button.click()

        latvia_news = driver.find_element(By.XPATH, "//a[@href='/zinas/latvija/']")
        latvia_news.click()

        header_news = driver.find_element(By.XPATH, "//span[@class='thumbnail__caption_text' and text()]")
        header_news.click()

        time.sleep(2)

        page_source = driver.page_source

        soup = BeautifulSoup(page_source, 'html.parser')

        article = soup.find('h1', class_ = 'article-title')
        title = article.text
        #img_tag = soup.find('figure', class_ = 'block gallery-single photo landscape')
        #image_url = img_tag.find('img')['src']
        head= soup.find('head')
        link = head.find('link', {'rel': 'canonical'})['href']

        if link != last_sent_url:
            article_lead = soup.find('h2', class_= 'article-lead')
            title_lead = article_lead.text


            message_text = f"<b>{title}</b>\n{title_lead}\n\nVairāk par ziņu: {link}"
            bot.send_message(chat_id=507643624, text=message_text, parse_mode="HTML")
            last_sent_url = link

            with open('news_database.txt', 'a', encoding='utf-8') as file:
                file.write(f"{title}\n{title_lead}\nVairāk par ziņu: {link}\n\n")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()

    time.sleep(1800)