# app/summarizer.py

from openai import OpenAI
import os
from dotenv import load_dotenv

# .envファイルをロードする
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def summarize_text(text: str) -> str:
    """
    文章を要約する関数（新バージョンopenai対応版）

    Args:
        text (str): 要約したい本文

    Returns:
        str: 要約文
    """
    if not text:
        return ""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは優れた要約者です。"},
                {"role": "user", "content": f"次のニュース記事を300文字以内で要約してください。\n{text}"}
            ],
            temperature=0.5,
            max_tokens=300
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print(f"要約中にエラーが発生しました: {e}")
        return ""

# テスト
if __name__ == "__main__":
    sample_text = "ここに長いニュース本文を貼り付けてください。"
    summarized = summarize_text(sample_text)
    print("=== 要約文 ===")
    print(summarized)
