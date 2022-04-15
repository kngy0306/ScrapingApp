import requests
import urllib.request
import os
from bs4 import BeautifulSoup


def scraping():
    base_url = "https://www.nogizaka46.com"
    member_name = "manatsu_akimoto"
    url = base_url + "/s/n46/diary/MEMBER/list?ima=2105&ct=7639"

    # フォルダ作成
    if not os.path.isdir(member_name):  # ”member_name”のフォルダがない場合
        print("フォルダ作成")
        os.mkdir(member_name)

    # 保存枚数カウント用
    cnt = 0

    # BeautifulSoupオブジェクト生成
    headers = {"User-Agent": "Mozilla/5.0"}
    soup = BeautifulSoup(requests.get(
        url, headers=headers).content, 'html.parser')

    content_source = []
    for blog_list in soup.find_all("div", class_="bl--list"):
        for a_class in blog_list.find_all("a", class_="bl--card"):
            content_source.append(a_class.attrs["href"])

    print(content_source)
    exit()

    # 画像が置かれているhtmlを見つける
    for entry in soup.find_all("div", class_="entrybody"):  # 全てのentrybodyを取得
        for img in entry.find_all("img"):  # 全てのimgを取得
            cnt += 1
            urllib.request.urlretrieve(
                img.attrs["src"], "./" + member_name + "/" + member_name + "-" + str(cnt) + ".jpeg")
    print("画像を" + str(cnt) + "枚保存しました。")


if __name__ == '__main__':
    scraping()
