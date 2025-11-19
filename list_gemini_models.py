import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルを読み込む
load_dotenv()

# APIキーを環境変数から取得
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

print("=== Gemini API 使用可能なモデル一覧 ===\n")

# 使用可能なモデル一覧を取得
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"モデル名: {model.name}")
        print(f"表示名: {model.display_name}")
        print(f"説明: {model.description}")
        print(f"入力トークン上限: {model.input_token_limit}")
        print(f"出力トークン上限: {model.output_token_limit}")
        print(f"サポートメソッド: {model.supported_generation_methods}")
        print("-" * 70)

# .envファイルで指定されたモデルの情報を表示
specified_model = os.getenv('GEMINI_MODEL')

if specified_model:
    print(f"\n=== .envで指定されているモデル: {specified_model} ===\n")
    
    try:
        # モデル名にmodels/プレフィックスが含まれているかチェック
        model_name = specified_model if specified_model.startswith('models/') else f"models/{specified_model}"
        
        model_info = genai.get_model(model_name)
        print(f"モデル名: {model_info.name}")
        print(f"表示名: {model_info.display_name}")
        print(f"説明: {model_info.description}")
        print(f"入力トークン上限: {model_info.input_token_limit}")
        print(f"出力トークン上限: {model_info.output_token_limit}")
        print(f"サポートメソッド: {model_info.supported_generation_methods}")
    except Exception as e:
        print(f"エラー: {e}")
        print(f"指定されたモデル '{specified_model}' が見つかりませんでした。")
else:
    print("\n.envファイルにGEMINI_MODELが指定されていません。")
