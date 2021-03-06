# インストールしたパッケージのインポート
from flask import Flask

# appという名前でFlaskのインスタンスを作成
app = Flask(__name__)

# どこのアドレスで実行するか指定
# 今回は http://127.0.0.1:5000/ にアクセスされたらhello_worldを実行するよ
@app.route('/')
def hello_world():

    message = "Hello World"

    return message

if __name__ == '__main__':
    # 作成したappを起動
    # ここでflaskの起動が始まる
    app.run()