# Dev Containerからリモートリポジトリの操作を行う

Dev Containerではコンテナ起動時に、自動的にgitの設定ファイルがコピーされます。そのためコンテナ内で自由にブランチを切ったり、コミットを重ねることができますが、リモートリポジトリとの連携をSSHで行なっている場合、コンテナからローカルマシン上の鍵を参照することができないため`git push`等を行う際にエラーが発生します。

本ドキュメントでは、上記を解消するための設定手順について解説します。

## SSH agentへの鍵の追加

SSH agentにあらかじめ鍵を追加しておくことで、コンテナ側ではSSHを利用したリモートリポジトリとの接続が可能となります（Dev ContainerがSSH agentを自動的に転送するため）。

### SSH agentの起動

ローカルマシンにWindows環境やLinux環境（Ubuntuなど）を使用している場合、はじめにSSH agentの起動が必要です。それぞれの環境に応じて以下のコマンドを実行してください。macOSの場合はあらかじめ起動しているため、追加の作業はありません。

Windowsの場合：
```powershell
Set-Service ssh-agent -StartupType Automatic
Start-Service ssh-agent
Get-Service ssh-agent
```

Linuxの場合：
```shell
eval "$(ssh-agent -s)"
```

### 鍵の追加

SSH agentを起動したら、以下のコマンドでGitHubに登録している鍵を追加します。指定するのは秘密鍵のファイルパスです。

```shell
ssh-add ~/.ssh/github_rsa
```

## 動作確認

リモートリポジトリに接続できることを確認するため、以下のコマンドを実行してください。

```shell
ssh -T git@github.com
```

下記のようなログが表示されれば、動作確認は完了です。以降、Dev Containerから`git pull`や`git push`といった操作が可能となります。

```shell
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

## 参考リンク

- [Sharing Git credentials with your container](https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials)
- [ssh-agent: How to configure ssh-agent, agent forwarding, & agent protocol](https://www.ssh.com/academy/ssh/agent)
