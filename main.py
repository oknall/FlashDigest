# main.py

from app.fetcher import fetch_article_text
from app.summarizer import summarize_text

def main():
    print("📰 FlashDigest - ニュース要約ツール")
    url = input(">> 要約したいニュース記事のURLを入力してください: ")

    print("\n🔍 記事本文を取得中...")
    article_text = fetch_article_text(url)

    if not article_text:
        print("⚠️ 記事の取得に失敗しました。URLが正しいか確認してください。")
        return

    print("\n🤖 要約を生成中...")
    summary = summarize_text(article_text)

    print("\n=== ✅ 要約結果 ===")
    print(summary)

if __name__ == "__main__":
    main()
