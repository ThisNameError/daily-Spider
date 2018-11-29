import re
import requests


def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None


def parse_page(html):
    pattern = re.compile('downurls=.*?集\$(.*?)/#', re.S)
    items = re.findall(pattern, html)
    return items


def main():
    url = 'https://www.mkv99.com/vod-detail-id-9462.html?tdsourcetag=s_pctim_aiomsg'
    html = get_one_page(url)
    items = parse_page(html)
    print(items)


if __name__ == '__main__':
    main()
