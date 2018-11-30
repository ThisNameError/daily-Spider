from compare_helper import *
import requests
import random
import os

from PIL import Image


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None


def save_img(html):
    words = 'qwertyuioplkjhgfdszxcvbnm'
    filename = ''
    for i in range(6):
        filename += random.choice(words)
    filename += '.jpg'
    with open('./images/%s' % (filename), 'wb') as f:
        f.write(html)


# 切割图片
def get_img():
    imgs = os.listdir('./images')
    for img in imgs:
        big_img = Image.open(f'./images/{img}')
        big_img.crop((0, 0, 76, 76)).save(f'./small_img/1_{img}')
        big_img.crop((76, 0, 152, 76)).save(f'./small_img/2_{img}')
        big_img.crop((152, 0, 228, 76)).save(f'./small_img/3_{img}')
        big_img.crop((228, 0, 304, 76)).save(f'./small_img/4_{img}')


# 图片去重
def uniq_img():
    # 取到所有图片
    imgs = os.listdir('./small_img')
    i = 1
    for img in imgs:
        target_one = Image.open(f'./small_img/{img}')
        for target_img in imgs:
            target_two = Image.open(f'./small_img/{target_img}')
            # 取到文件路径
            path_one = target_one.filename
            path_two = target_two.filename
            # 判断是否为同一个文件，如果是，则不进行比较
            if path_one == path_two:
                continue
            score = get_compare(path_one, path_two)
            # 相似度超过90，则删除重复图片
            if score > 90:
                os.remove(path_two)
                print(f'删除第{i}张')
                i += 1


def main():
    # url = 'http://www.1kkk.com/image3.ashx?t=1543563002000'
    # for i in range(50):
    #     html = get_page(url)
    #     save_img(html)
    #     print(i)
    # get_img()
    uniq_img()


if __name__ == '__main__':
    main()
