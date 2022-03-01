# Flask sample

## Development

```shell
# 任意のディレクトリを作成
mkdir flask

# venvでPython3の仮想環境を作成
python3 -m venv flask

# 仮想環境内にFlaskプロジェクトをクローン
cd flask
git clone https://github.com/kuuhack/flask-sample.git

# 仮想環境突入
source ../bin/activate

# 依存関係をインストール
pip install -r requirements.txt

# Flask サーバ開始 オートリロードオプション付き
flask run --debugger --reload

# 仮想環境抜け出し
deactivate
```

### Command

```shell
# 現在の依存関係を書き出し
pip freeze >| ./requirements.txt
```

## Deployment

https://vercel.com/
