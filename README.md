# Welcome to NBNE!

NBNE（Node Based Notion Editor）は、煩雑になりがちなNotionワークスペースを俯瞰的に管理できるよう、ページやDBをノードとして表現しながら編集できるエディターです。

## Getting Started

Coming soon.

## Development

ローカルマシンで開発環境を立ち上げるための手順について解説します。

### Prerequisities

開発を行うにあたり、下記のソフトウェアがあらかじめインストールされていることを前提としています。

- [Git](https://git-scm.com/)をインストールしていること
- [Docker](https://www.docker.com/)をローカルマシンやWSLにインストールしていること
- [VSCode](https://code.visualstudio.com/)をインストールしていること（お気に入りのエディタがあれば、必須ではありません）

### Installation

作業用のディレクトリへ移動し、このリポジトリをローカルマシン（もしくはWSL）上にクローンしてください。

```shell
$ cd /path/to/workspace
$ git clone git@github.com:katayama-yuta/nbne.git
```

`nbne`ディレクトリが作成されたら、VSCode上でこのディレクトリを開いてください。

```shell
$ code nbne/
```

初めて`nbne`で作業をする場合は、新しいターミナルを開き、Dockerイメージをビルドしてください。

```shell
$ docker compose build
```

エラーなくビルドが完了したら、コマンドパレットを開き「Dev Container: Reopen in Container」を検索して実行してください。

VSCode左下の表示が「Dev Container:...」に変わっていれば準備はOKです。[Issues](https://github.com/katayama-yuta/nbne/issues)を読み、ブランチを切って開発を始めましょう！

### Stop Dev Container

コンテナを終了してVSCodeとの接続を切りたい時は、左下「Dev Container: ...」の表示をクリックし「Close Remote Connection」を選択してください。

またコンテナを立ち上げたくなった時は、同じボタンから「Reopen in Container」を選択することで、VSCodeとコンテナが接続されます。