# QuaLLM with MCP

QuaLLM with MCPは、Model Context Protocol (MCP)を活用したAIエージェントです。


## 機能

- Web検索機能付きチャットインターフェース
- Model Context Protocol (MCP)による拡張性
- リアルタイムな対話型インターフェース

## 必要条件

- Docker
- Docker Compose
- Brave Search APIキー
- OpenAI APIキー

## セットアップ

1. リポジトリをクローン:
```bash
git clone https://github.com/permy1225/quallm.git
cd quallm
```

2. 環境変数の設定:
```bash
cp backend.env.example backend.env
```
`backend.env`ファイルに Brave Search APIキーと OpenAI APIキーを設定してください。

3. アプリケーションの起動:
```bash
docker compose up
```

## 使用方法

1. ブラウザで `http://localhost:8501` にアクセス
2. チャットインターフェースで質問を入力
3. アシスタントがWeb検索を活用して回答を生成

## アーキテクチャ

- フロントエンド: Streamlit (ポート: 8501)
- バックエンド: FastAPI (ポート: 8000)
- Model Context Protocol (MCP)による拡張機能