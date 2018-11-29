import requests
import json

from sqlalchemy_helper import save_db


# 抓网页
def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None


def get_html(html):
    i = html.index('(')
    html = html[i+1:]
    html = html[:-2]
    result_dict = json.loads(html)
    is_end = result_dict['result']['wall']['isEnd']
    if is_end:
        return None
    results = result_dict['result']['wall']['docs']
    # print(results)
    mogu_list = []
    for item in results:
        # print(item.get('price', ''))
        mogu_dict = {}
        mogu_dict['tradeItemId'] = item.get('tradeItemId', '')
        mogu_dict['img'] = item.get('img', '')
        mogu_dict['itemType'] = item.get('itemType', '')
        mogu_dict['clientUrl'] = item.get('clientUrl', '')
        mogu_dict['link'] = item.get('link', '')
        mogu_dict['itemMarks'] = item.get('itemMarks', '')
        mogu_dict['acm'] = item.get('acm', '')
        mogu_dict['title'] = item.get('title', '')
        mogu_dict['type'] = item.get('type', '')
        mogu_dict['orgPrice'] = item.get('orgPrice', '')
        mogu_dict['hasSimilarity'] = item.get('hasSimilarity', '')
        mogu_dict['cfav'] = item.get('cfav', '')
        mogu_dict['price'] = item.get('price', '')
        mogu_dict['similarityUrl'] = item.get('similarityUrl', '')
        mogu_list.append(mogu_dict)
    return mogu_list


def write_json(result_list):
    html_str = json.dumps(result_list, ensure_ascii=False)
    with open('./mogu.json', 'a') as f:
        f.write(html_str)


def main():
    page = 1
    total_list = []
    while True:
        print(page)
        url = 'https://list.mogujie.com/search?callback=jQuery21108929871970406824_1543377785475&_version=8193&ratio=3%3A4&cKey=43&sort=pop&page=' + str(page) + '&q=%25E7%2589%259B%25E4%25BB%2594%25E8%25A3%25A4&minPrice=&maxPrice=&ppath=&cpc_offset=&ptp=1.5y18ub.0.0.yNGsrOvo&_=1543377785476'
        html = get_one_page(url)
        if '(' not in html:
            print('+++++++error+++++++')
            # t = random.randint(1, 3)
            # time.sleep(t)
            continue
        print(html)
        result_list = get_html(html)
        if result_list is None:
            break
        total_list.extend(result_list)
        page += 1
        save_db(total_list)
    # print(result_list)
    # print(len(result_list))
    #     write_json(total_list)


if __name__ == '__main__':
    main()
