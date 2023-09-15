# 概要
このドキュメントにはGitとDockerを初めてWindows環境にインストールする際の環境構築の手順を記載しています。

# 環境構築
## 作成する環境
- WSL2
- Ubuntu 20.04
- Docker git 24.0.5
- Docker Compose version v2.20.2

## 環境構築の手順
### WSL2でUbuntuをインストールする
Windowsの管理者モードでコマンドプロンプトを開き、WSLで利用するUbuntuイメージをインストールしてください。
```shell
$ wsl --install -d Ubuntu-20.04
```
インストール完了後、PCを再起動してUbuntu上にユーザ情報の登録を行ってください。

- ユーザー名、パスワードを設定
- その他項目はデフォルトでOK

### Dockerをインストールする
Ubuntuのコマンドプロンプトを開き、Docker構築に必要なパッケージをインストールしてください。
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
$ git --version
```