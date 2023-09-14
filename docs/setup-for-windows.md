# 概要
このドキュメントは環境構築の方法からDockerコンテナの立ち上げ、SteramLitの立ち上げ方までを説明するドキュメントです。

# 環境構築
## 作成する環境
- WLS2
- Ubuntsu20.04
- Docker 24.0.5
- Docker Compose version v2.20.2


## 環境構築の手順
### WLS2でUbuntsuをインストールする
Windowsの管理者モードでコマンドプロンプトを開き、WSL（Ubuntsu）をインストールしてください。
```shell
$ wsl --install -d Ubuntu-20.04
```
インストール完了後、PCを再起動してUbuntsu上にユーザ情報の登録を行ってください。
  a. ユーザー名、パスワードを設定
  b. その他項目はデフォルトでOK

### Dockerをインストールする
Ubuntsuのコマンドプロンプトを開き、Docker構築に必要なパッケージをインストールしてください。
```shell
$ sudo apt update # Linuxシステムのアップデート
$ sudo apt upgrade # アップデート可能なパッケージを更新
$ sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common # 必要なパッケージのインストール
```
Dockerリポジトリを利用するために認証キー（GPGキー）を取得してください。
```shell
 $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - 
```
Dockerリポジトリをapt管理下に追加する(apt : Linuxのパッケージを操作するためのCLIツール)
```shell
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```
Linuxの更新を行い、Dockerをインストールしてください。
```shell
$ sudo apt update
$ sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Dockerのバージョンを確認するコマンド(以下の2つ)を実行して、バージョンが正しく表示されたら環境構築は完了となります。
```shell
$ docker -v
$ docker -compose -v
```
## Dockerコンテナの立ち上げ方
### For Windows
VScode上でWSL2+Ubuntsu環境に接続する
1. VScodeを立ち上げる
2. VScodeの左下をクリックして、「Connect to WSL」をクリック
  ![image3](https://github.com/katayama-yuta/nbne/assets/102128177/2af5944d-2246-4e36-94f0-518120caedda)
3. VScodeの左下の青いところが「WSL: Ubuntsu-20.04」になっていれば完了
Dockerコンテナを立ち上げる
※以降操作はVScode上にて実施
1. [ctrl + shift + @]を押してターミナルを開く
2. ターミナル上で以下コマンドを入力
```shell
$ cd nbne # カレントディレクトリの移動
$ code.
```
3. 左下の青い「WSL: Ubuntsu-20.04」をクリックして、「Reopen in Container」をクリック
  ![image](https://github.com/katayama-yuta/nbne/assets/102128177/16aee4c6-0814-42eb-9f59-d199a768d9a3)
4. Dockerコンテナが立ち上がって、新しいウィンドウ上で左下の青いところが「Dev Container～」になっていれば完了
StreamLitへの接続方法
※Dockerコンテナを立ち上げると自動的にStreamLitは立ち上がるようになっている
1. ブラウザを立ち上げる
2. URLに「http://localhost:8501/」と入力すると、StreamLitの画面になる
3. Stream Litを終了したい時には、Dockerコンテナを終了させる
Dockerコンテナの終わり方
1. 左下の青いところ「Dev Container～」をクリック
2. 「Close Remote Connection」をクリックして終了
3. Ubuntsuのコマンドプロンプトで以下のコマンド入力して、コンテナ名が表示されなければ完了
```shell
$ docker compose pd
```