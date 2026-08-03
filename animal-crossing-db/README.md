# あつまれどうぶつの森 生き物データベースアプリ

## 1. システムの概要・用途
本システムは『あつまれどうぶつの森』に登場する 魚・虫・海の幸 のデータを検索できる Web 図鑑アプリです。
生き物の 価格・出現時期・出現時間・出現場所・特殊条件 をまとめて検索でき、プレイヤーが効率よく図鑑を埋めたり、売値を調べたりする用途を想定しています。

Flask（Python）で構築され、Docker コンテナ上で動作します。
ホスト PC のブラウザからアクセスして利用できます。

## 2. 実行方法 (Docker環境)
本アプリケーションはDocker上で動作します。ホストPCにDockerがインストールされている必要があります。

### 3. リポジトリのクローンまたはダウンロード
git clone https://github.com/yuumoon605/Animal-Crossing-DB.git
cd Animal-Crossing-DB

### 4. ファイル構成
animal-crossing-db/
├── app.py                # Flask アプリ本体
├── database.py           # 生き物データ（CREATURES_DATA）
├── requirements.txt      # Flask の依存関係
├── Dockerfile            # Docker イメージ定義
└── templates/
    └── index.html        # Web UI（Bootstrap使用）

### 5. 実行方法（Docker）
docker build -t acnh-db .　#Dockerイメージをビルド
docker run -d -p 5000:5000 --name acnh-container acnh-db　#コンテナを起動
http://localhost:5000 #任意のブラウザでアクセス

### 6.アプリの使い方
検索フォーム
・名前検索：部分一致で検索可能
・カテゴリ絞り込み：魚 / 虫 / 海の幸
・最低価格：指定したベル以上の生き物を表示
・出現時期：例「11月」「3」などで検索可能
一覧表示
・名前
・カテゴリ
・価格
・出現時期
・出現時間
・出現場所（条件含む）

### 7.動作画面
![トップページ](images/acnh-db_explane (2).png)

![検索結果](images/acnh-db_explane (3).png)

![docker ps](images/acnh-db_explane (1).png)

### 8.ライセンス
本リポジトリは自由に改変・利用可能です。
