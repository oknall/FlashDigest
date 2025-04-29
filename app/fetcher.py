# app/fetcher.py

import requests
from bs4 import BeautifulSoup

def fetch_article_text(url: str) -> str:
    """
    ニュース記事のURLを受け取り、本文を抽出して返す関数。
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 200以外なら例外
    except requests.RequestException as e:
        print(f"ページ取得に失敗しました: {e}")
        return ""
    
    soup = BeautifulSoup(response.content, "html.parser")  # .textではなく.contentを使う
    soup.encoding = soup.original_encoding  # BeautifulSoupに自動推定させる

    article = soup.find('article')
    if article:
        text = article.get_text(separator="\n", strip=True)
        return text

    paragraphs = soup.find_all('p')
    if paragraphs:
        text = "\n".join(p.get_text(strip=True) for p in paragraphs)
        return text

    print("記事本文を抽出できませんでした。")
    return ""

# テスト
if __name__ == "__main__":
    test_url = "https://www.city.nagareyama.chiba.jp/life/1001107/1001188/index.html"  # テスト用URL
    content = fetch_article_text(test_url)
    print("=== 取得した記事本文 ===")
    print(content[:500] + "...\n（以下省略）")
