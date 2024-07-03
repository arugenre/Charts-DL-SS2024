import time
import json

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions


LEETCODE_URL = "https://leetcode.com/problemset/"


def scrape():
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--headless=new')
    driver = Chrome(options=chrome_options)
    driver.get(url=LEETCODE_URL)
    time.sleep(3)
    content = driver.page_source

    bs = BeautifulSoup(markup=content, features="html.parser")

    categories = []
    companies = []

    category_divs = bs.find_all(
        name="div",
        attrs={"class": "m-[10px]"}
    )

    for category_div in category_divs:
        spans = category_div.find_all(name="span")
        categories.append({
            "label": spans[0].text,
            "value": int(spans[1].text)
        })

    swiper_wrapper = bs.find_all(name="div", attrs={"class": "swiper-wrapper"})[1]
    swipers = swiper_wrapper.find_all(name="div", attrs={"class": "swiper-slide"})
    for swiper in swipers:
        company_spans = swiper.find_all(
            name="span",
            attrs={"class": "text-label-3"}
        )

        for company_span in company_spans:
            spans = company_span.find_all(name="span")
            companies.append({
                "label": spans[0].text,
                "value": spans[1].text
            })

    with open("leetcode_categories.json", "w") as f:
        json.dump(categories, f, indent=4, ensure_ascii=False)

    with open("leetcode_companies.json", "w") as f:
        json.dump(companies, f, indent=4, ensure_ascii=False)


def main():
    scrape()


if __name__ == "__main__":
    main()
