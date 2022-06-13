# ScrapingApp

乃木坂46と日向坂46のブログをスクレイピングする

## 乃木坂４６ブログ
https://www.nogizaka46.com/s/n46/diary/MEMBER?ima=3627

## 実行環境の構築(Docker)

```sh
docker build -t scraping_app .

docker run --name scraping_app <IMAGE ID>

docker run -it -v "$PWD/src":/usr/src/app scraping_app bash
```

### scraping.py

乃木坂46ブログをスクレイピング([秋元真夏のページ](http://blog.nogizaka46.com/manatsu.akimoto/))  
[プログラム説明記事](https://qiita.com/xxPowderxx/items/e9726b8b8a114655d796)

### scraping_hinata.py

日向坂46ブログをスクレイピング([佐々木美玲のページ](https://www.hinatazaka46.com/s/official/diary/member/list?ima=0000&ct=8))
