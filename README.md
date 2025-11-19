# Gemini API モデル一覧取得ツール

Google Gemini APIで使用可能なモデルの一覧を取得し、詳細情報を表示するPythonスクリプトです。

## 概要

このツールを使用することで、以下の情報を取得できます：

- Gemini APIで使用可能な全モデルのリスト
- 各モデルの詳細情報（トークン上限、サポートメソッドなど）
- .envファイルで指定したモデルの詳細情報

## 機能

- ✅ 使用可能な全モデルの一覧表示
- ✅ モデル名、表示名、説明の表示
- ✅ 入力/出力トークン上限の表示
- ✅ サポートされているメソッドの表示
- ✅ .envファイルからの設定読み込み
- ✅ モデル名プレフィックス（`models/`）の自動処理

## 必要な環境

- Python 3.7以上
- Google Cloud APIキー（Gemini API有効化済み）

## インストール

### 1. リポジトリのクローン

```bash
git clone https://github.com/ueponx/gemini-available-models.git
cd gemini-available-models
```

### 2. 必要なパッケージのインストール

```bash
pip install google-generativeai python-dotenv
```

または、requirements.txtを使用する場合：

```bash
pip install -r requirements.txt
```

## 使い方

### 1. .envファイルの作成

プロジェクトのルートディレクトリに`.env`ファイルを作成し、以下の内容を記述します：

```env
GOOGLE_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-pro
```

**APIキーの取得方法:**
1. [Google AI Studio](https://makersuite.google.com/app/apikey)にアクセス
2. 「Get API Key」をクリックしてAPIキーを取得
3. 取得したAPIキーを`.env`ファイルに記述

### 2. スクリプトの実行

```bash
python list_gemini_models.py
```

## 出力例

```
=== Gemini API 使用可能なモデル一覧 ===

モデル名: models/gemini-2.5-pro
表示名: Gemini 2.5 Pro
説明: Stable release (June 17th, 2025) of Gemini 2.5 Pro
入力トークン上限: 1048576
出力トークン上限: 65536
サポートメソッド: ['generateContent', 'countTokens', 'createCachedContent', 'batchGenerateContent']
----------------------------------------------------------------------

=== .envで指定されているモデル: gemini-2.5-pro ===

モデル名: models/gemini-2.5-pro
表示名: Gemini 2.5 Pro
説明: Stable release (June 17th, 2025) of Gemini 2.5 Pro
入力トークン上限: 1048576
出力トークン上限: 65536
サポートメソッド: ['generateContent', 'countTokens', 'createCachedContent', 'batchGenerateContent']
```

## モデル名の指定方法

.envファイルでのモデル名指定は、以下のどちらの形式でも動作します：

```env
# プレフィックスなし
GEMINI_MODEL=gemini-2.5-pro

# プレフィックスあり
GEMINI_MODEL=models/gemini-2.5-pro
```

スクリプトが自動的に適切な形式に変換します。

## 主要なモデル

2025年11月時点で利用可能な主要モデル（Gemini 2.5以上）：

### 汎用モデル

| モデル名 | 説明 | 入力トークン | 出力トークン |
|---------|------|------------|------------|
| gemini-3-pro-preview | Gemini 3.0 Proプレビュー版 | 1,048,576 | 65,536 |
| gemini-2.5-pro | Gemini 2.5 Pro安定版 | 1,048,576 | 65,536 |
| gemini-2.5-flash | 高速で汎用的なモデル | 1,048,576 | 65,536 |
| gemini-2.5-flash-lite | 軽量版Flash | 1,048,576 | 65,536 |

### 特殊用途モデル

| モデル名 | 説明 | 入力トークン | 出力トークン |
|---------|------|------------|------------|
| gemini-2.5-flash-image | 画像生成対応 | 32,768 | 32,768 |
| gemini-2.5-flash-preview-tts | テキスト読み上げ（TTS） | 8,192 | 16,384 |
| gemini-2.5-pro-preview-tts | テキスト読み上げ（TTS） | 8,192 | 16,384 |
| gemini-2.5-computer-use-preview-10-2025 | コンピュータ操作 | 131,072 | 65,536 |

## サポートメソッド

各モデルがサポートするAPIメソッドの説明：

| メソッド名 | 説明 |
|-----------|------|
| `generateContent` | テキスト、画像などのコンテンツを生成する基本メソッド |
| `countTokens` | 入力テキストのトークン数をカウント |
| `createCachedContent` | コンテンツをキャッシュして再利用可能にする（コスト削減・高速化） |
| `batchGenerateContent` | 複数のリクエストをまとめてバッチ処理 |
| `bidiGenerateContent` | 双方向ストリーミング通信（リアルタイム対話用） |

### メソッドの使い分け

- **通常の生成**: `generateContent`を使用
- **コスト最適化**: 同じコンテキストを繰り返し使う場合は`createCachedContent`
- **大量処理**: 多数のリクエストを効率的に処理する場合は`batchGenerateContent`
- **リアルタイム対話**: 音声対話やライブ通信には`bidiGenerateContent`
- **料金見積もり**: 事前に`countTokens`でトークン数を確認

## トラブルシューティング

### エラー: "404 Model is not found"

**原因:** モデル名の指定が正しくない可能性があります。

**解決方法:**
1. スクリプトを実行して利用可能なモデル一覧を確認
2. .envファイルのモデル名を正しいものに修正

### エラー: "API key not valid"

**原因:** APIキーが正しく設定されていません。

**解決方法:**
1. .envファイルが正しい場所に配置されているか確認
2. APIキーが正しくコピーされているか確認
3. APIキーにGemini APIの使用権限があるか確認

## セキュリティに関する注意

⚠️ **重要:** `.env`ファイルには機密情報（APIキー）が含まれています。

- `.gitignore`に`.env`を必ず追加してください
- APIキーを公開リポジトリにコミットしないでください
- APIキーを他人と共有しないでください

### .gitignoreの例

```gitignore
# 環境変数ファイル
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
```

## ライセンス

MIT License

## 作成者

ueponx

## 参考リンク

- [Google AI Studio](https://makersuite.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Google Generative AI Python SDK](https://github.com/google/generative-ai-python)

## 更新履歴

- 2025-11-15: 初版リリース
  - モデル一覧取得機能
  - .envファイル対応
  - モデル名プレフィックス自動処理
