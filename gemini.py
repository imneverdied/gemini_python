import requests
import json

# 設定 API 的 URL 和金鑰
api_url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'
api_key = 'API-key'  # 請替換成您的 API 金鑰

def call_gemini(prompt):
    # 設定要 POST 的資料
    data = {"contents":[{"parts":[{"text":prompt}]}]}
    # 將資料轉換為 JSON 格式
    json_data = json.dumps(data)
    # 發送 POST 請求並取得回應
    response = requests.post(f'{api_url}?key={api_key}', data=json_data)
    # 檢查回應是否成功
    if response.status_code == 200:
        # 解析 JSON 数据
        data = response.json()
        # 提取"text"内容
        text_content = data["candidates"][0]["content"]["parts"][0]["text"]
        print(text_content)
        return text_content
    else:
        print('POST 請求失敗，狀態碼：', response.status_code)
        return None

# 輸出結果到 gemini輸出.txt 檔案
with open("gemini輸出.txt", "a+", encoding="utf-8") as file:
    file.write(call_gemini("早安") + "\n")

# 輸出結果到 gemini輸出.txt 檔案
with open("gemini輸出.txt", "a+", encoding="utf-8") as file:
    file.write(call_gemini("造一個20字的詩") + "\n")