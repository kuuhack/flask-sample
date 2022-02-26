# Flask sample

## Development

```shell
# 任意のディレクトリを作成
mkdir flask

# venvでPython3の仮想環境を作成
python3 -m venv flask

# 仮想環境の中にflaskプロジェクトをクローン
cd flask
git clone https://github.com/kuuhack/flask-sample.git

# 仮想環境突入
source ../bin/activate

# 依存関係をインストール
pip install -r requirements.txt

# flask サーバ開始 オートリロードオプション付き
flask run --debugger --reload

# 仮想環境抜け出し
deactivate
```

### Command

```shell
pip freeze >| ./requirements.txt
```
