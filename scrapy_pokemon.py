import requests
import urllib.request
import os
from bs4 import BeautifulSoup


def scraping():
    url = "https://www.shutterstock.com/ja/search/pokemon+go"
    folder_name = "pokemon"

    # フォルダ作成
    if not os.path.isdir(folder_name):  # ”member_name”のフォルダがない場合
        print("フォルダ作成")
        os.mkdir(folder_name)

    # 保存枚数カウント用
    cnt = 0

    # BeautifulSoupオブジェクト生成
    headers = {"User-Agent": "Mozilla/5.0"}
    soup = BeautifulSoup(requests.get(
        url, headers=headers).content, 'html.parser')

    # 画像が置かれているhtmlを見つける
    for entry in soup.find_all("div", class_="z_g_a"):  # 全てのentrybodyを取得
        for img in entry.find_all("img"):  # 全てのimgを取得
            cnt += 1
            urllib.request.urlretrieve(
                img.attrs["src"], "./" + folder_name + "/" + folder_name + "-" + str(cnt) + ".jpeg")
    print("画像を" + str(cnt) + "枚保存しました。")


if __name__ == '__main__':
    scraping()
