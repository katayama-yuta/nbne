# 概要
このドキュメントは環境構築の方法からDockerコンテナの立ち上げ、SteramLitの立ち上げ方までを説明するドキュメントです。

# 環境構築
## 作成する環境
### For Windows（OS : Windows11）
- WLS2
- Ubuntsu20.04
- Docker 24.0.5
- Docker Compose version v2.20.2
### For Mac


## 環境構築の手順
### For Windows
WLS2でUbuntsuをインストールする
1. メニューからWindows PowerShellを開く
2. 以下コマンドを実行して、WLSをインストールする
  ``` wsl --install -d Ubuntu-20.04```
3. インストール後、PCを再起動
4. 再起動後、コマンドプロンプトが自動で開くので、ユーザー登録を行う
  a. ユーザー名、パスワードを設定
  b. その他項目はデフォルトでOK
Dockerをインストールする
1. Ubuntsuのコマンドプロンプトを開く
2. 以下コマンドを実行して、Dockerに必要なパッケージをインストールする
  ``` sudo apt update # Linuxシステムのアップデート ```
  ``` sudo apt upgrade # アップデート可能なパッケージを更新 ```
  ``` sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common # 必要なパッケージのインストール ```
3. Dockerリポジトリを利用するための認証キー（GPGキー）を取得する
 ``` curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - ```
4. Dockerリポジトリをapt管理下に追加する(apt : Linuxのパッケージを操作するためのCLIツール)
  ``` sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" ```
5. 再度Linuxをアップデートする（ここでDokerをインストールする準備が完了）
  ``` sudo apt update ```
6. Dockerのインストール
  ``` sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin```
7. Dockerのバージョンを確認するコマンド(以下の2つ)を実行して、バージョンが表示されたら、完了
  ``` docker -v ```
  ``` docker -compose -v ```

### For Mac

## プロジェクトへの参加方法
### For Windows
0. （事前準備）githubのプロジェクトにユーザー追加をしてもらう
githubにSSH認証の追加
※既にgithubにSSH認証を登録している場合はスキップ
1. Ubuntsuのコマンドプロンプトで以下のコマンドを実行してSSHキーを作成する（メールアドレスは自分のアドレスを使用）
 ``` ssh-keygen -t ed25519 -C "example@mail.com" ```
2. 作成されたSSHキーをコピーしておく
3. ブラウザ上のgithubでユーザーアイコン > Settingsをクリック
  ![image1](https://github.com/katayama-yuta/nbne/assets/102128177/1b5845fe-4626-4d62-982b-33c97b0430f0)
  ![image2](https://github.com/katayama-yuta/nbne/assets/102128177/fda9b465-11e7-41da-a7cd-5766905fbce5)
4. サイドバーから「SSH and GPG keys」をクリック
5. 「New SSH key」をクリック
6. 以下の値を設定する
  a. Title : 任意のタイトル
  b. key Type : Authentication Key
  c. Key : 手順2でコピーしたSSHキーを貼り付け
7. 「Add SSH key」をクリックして完了
githubのプロジェクトをローカル環境に構築する
1. Ubuntsuのコマンドプロンプトを開く
2. githubからプロジェクトをクローンする
  ``` git clone https://github.com/katayama-yuta/nbne.git ```
3. 以下コマンドを実行して、「nbne」のフォルダが確認できれば完了
 ``` ls ```

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
  ``` cd nbne # カレントディレクトリの移動```
  ``` code . # カレントディレクトリの新しいウィンドウを開く```
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
 ```docker compose pd ```