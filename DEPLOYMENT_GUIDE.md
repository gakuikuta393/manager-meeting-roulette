# GitHub PagesとNotion組み込み手順

## 📌 概要

このガイドでは、ルーレットアプリケーションをGitHub Pagesにデプロイし、Notionページに埋め込む手順を説明します。

---

## 🚀 GitHub Pagesへのデプロイ手順

### 前提条件

- GitHubアカウントを持っていること
- Gitがインストールされていること（確認: `git --version`）

### ステップ1: GitHubリポジトリの作成

1. **GitHubにアクセス**
   - [github.com](https://github.com) にアクセスしてログイン

2. **新規リポジトリを作成**
   - 右上の「+」ボタンをクリック → 「New repository」を選択
   - リポジトリ名を入力（例: `manager-meeting-roulette`）
   - 公開設定を「Public」にする（GitHub Pagesは無料プランではPublicのみ）
   - 「Create repository」をクリック

### ステップ2: ローカルでGitリポジトリを初期化

PowerShellまたはコマンドプロンプトで以下を実行：

```powershell
# ルーレットフォルダに移動
cd "C:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット"

# Gitリポジトリを初期化
git init

# index.htmlをステージング
git add index.html

# コミット
git commit -m "Initial commit: Add roulette application"

# GitHubリポジトリをリモートとして追加（★自分のリポジトリURLに置き換え）
git remote add origin https://github.com/あなたのユーザー名/manager-meeting-roulette.git

# メインブランチにリネーム（Gitの最新版では必要な場合があります）
git branch -M main

# GitHubにプッシュ
git push -u origin main
```

> [!IMPORTANT]
> **認証について**
> 
> GitHubへのプッシュ時に認証が求められます。パスワードではなく「Personal Access Token」が必要です：
> 
> 1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
> 2. 「Generate new token」をクリック
> 3. `repo` スコープにチェック
> 4. トークンを生成してコピー
> 5. プッシュ時のパスワード入力でトークンを使用

### ステップ3: GitHub Pagesを有効化

1. **GitHubリポジトリにアクセス**
   - `https://github.com/あなたのユーザー名/manager-meeting-roulette`

2. **Settings（設定）を開く**
   - リポジトリページの上部メニューから「Settings」をクリック

3. **Pagesセクションに移動**
   - 左サイドバーから「Pages」をクリック

4. **ソースを設定**
   - 「Source」のドロップダウンから「main」ブランチを選択
   - フォルダは「/ (root)」を選択
   - 「Save」をクリック

5. **公開URLを確認**
   - 数分後、ページが公開されます
   - 公開URL: `https://あなたのユーザー名.github.io/manager-meeting-roulette/`
   - このURLをコピーしてください

---

## 📝 Notionへの埋め込み手順

### 方法1: 直接URLを貼り付ける（最も簡単）

1. **Notionページを開く**

2. **URLを貼り付け**
   - GitHub PagesのURL（`https://あなたのユーザー名.github.io/manager-meeting-roulette/`）をコピー
   - Notionページの任意の場所に貼り付け
   - エンターキーを押す

3. **埋め込みオプションを選択**
   - URLを貼り付けると自動的にポップアップが表示されます
   - 「Create embed」または「埋め込みを作成」を選択

4. **サイズ調整**
   - 埋め込みブロックをドラッグしてサイズを調整できます

### 方法2: 埋め込みブロックを使用

1. **Notionページで新しい行を作成**

2. **埋め込みブロックを追加**
   - `/` を入力して「Embed」または「埋め込み」を検索
   - または `/embed` と入力して表示されるメニューから選択
   
   > [!NOTE]
   > `/embed` が動作しない場合は：
   > - `/` だけ入力して、検索ボックスで「embed」や「埋め込み」と検索
   > - または、ブロックメニュー（+ボタン）から「Embed」を探す

3. **URLを入力**
   - GitHub PagesのURLを入力
   - 「Embed link」をクリック

### 方法3: iframeコードを使用（高度）

1. **コードブロックを追加**
   - Notionで `/code` を入力

2. **HTMLコードを貼り付け**
   ```html
   <iframe src="https://あなたのユーザー名.github.io/manager-meeting-roulette/" 
           width="100%" 
           height="800px" 
           frameborder="0">
   </iframe>
   ```

> [!CAUTION]
> Notionの仕様により、一部の埋め込みが制限される場合があります。その場合は、ページへのリンクを貼り、別タブで開く方法をご利用ください。

---

## 🔄 アプリケーションを更新する場合

ルーレットアプリケーションに変更を加えた場合の更新手順：

```powershell
# ルーレットフォルダに移動
cd "C:\Users\gakuikuta\OneDrive - ABEJA, Inc\デスクトップ\Antigravity\ルーレット"

# 変更をステージング
git add index.html

# コミット
git commit -m "Update: 変更内容の説明"

# GitHubにプッシュ
git push
```

GitHub Pagesは自動的に数分以内に更新されます。

---

## 🎯 簡易版：Gitを使わない方法

Gitの操作が難しい場合、以下の簡易的な方法もあります：

### GitHub Webインターフェースでアップロード

1. **GitHubでリポジトリを作成**（上記と同じ）

2. **ファイルをアップロード**
   - リポジトリページで「Add file」→「Upload files」をクリック
   - `index.html` をドラッグ&ドロップ
   - 「Commit changes」をクリック

3. **GitHub Pagesを有効化**（上記と同じ）

この方法なら、コマンドライン操作なしでデプロイできます。

---

## 🆘 トラブルシューティング

### GitHub Pagesが表示されない

- 設定後、最大10分程度かかる場合があります
- リポジトリが「Public」になっているか確認
- ファイル名が `index.html` になっているか確認（大文字小文字も一致）

### Notionで埋め込みができない

- `/embed` の代わりに `/` だけ入力して「embed」を検索
- URLを直接貼り付けて「Create embed」を選択する方法を試す
- Notionのブロックメニュー（左の ⋮⋮ アイコン）から「Turn into」→「Embed」を試す

### GitHubへのプッシュ時に認証エラー

- Personal Access Tokenを使用（上記参照）
- ユーザー名とトークンが正しいか確認
- トークンに `repo` スコープが付与されているか確認

---

## ✅ チェックリスト

デプロイ完了までの確認リスト：

- [ ] GitHubアカウント作成済み
- [ ] リポジトリを作成
- [ ] `index.html` をプッシュ
- [ ] GitHub Pagesを有効化
- [ ] 公開URLにアクセスして動作確認
- [ ] NotionページにURLを埋め込み
- [ ] Notion上で動作確認

---

## 📞 サポート

何か問題が発生した場合は、具体的なエラーメッセージやスクリーンショットとともにお知らせください。
