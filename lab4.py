import requests
from bs4 import BeautifulSoup


def main():
    parse_ukd_data()


def parse_ukd_data():
    url = "https://ukd.edu.ua/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("a", string="Спеціальності")
    for li in results.parent.find_all("li"):
        print(li.text)


if __name__ == '__main__':
    main()
