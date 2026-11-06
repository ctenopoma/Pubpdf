# Pubpdf

Markdown の原稿から、Quarto と Typst で PDF を作る VS Code 拡張機能です。Quarto や Typst の設定ファイルを書く必要はありません。

![VS Code で原稿、設定パネル、PDF のプレビューを並べた画面](images/vscode-preview.png)

このリポジトリは配布用で、ソースコードは置いていません。拡張機能は [Releases](https://github.com/ctenopoma/Pubpdf/releases/latest) からダウンロードできます。

## できること

- 1つの md から1つの PDF を作る
- 複数の md を1冊にまとめる
- 表紙、機密表示、目次、ページ番号を設定で切り替える
- 文字の大きさ、行間、余白、用紙の種類と向き、見出しと図表の番号の形式を設定で変える
- frontmatter に書いた履歴を、バージョン履歴のページにする
- 章を奇数ページから始め、綴じ代を取る(両面印刷や製本の前提)
- 表、コード、数式、定理、Mermaid の図、注意書きの囲みを組む
- PDF にしおりを付ける(見出しから自動で作ります)
- フォントを指定し、OS に入れていないフォントも読み込む
- VS Code の中で作成、プレビュー、設定の変更をする

組版に必要な変換は中間コピーに対して行うので、PDF を何度作っても原稿は変わりません。原稿を書き換えるのは、設定パネルと雛形の挿入で frontmatter を編集するときだけです。

## 必要なもの

| ソフト | 用途 | 補足 |
|---|---|---|
| [Quarto](https://quarto.org/) 1.10.18 以上 | 組版 | |
| VS Code 1.90 以上 | 拡張機能 | |
| 日本語フォント | 本文 | Windows なら標準のフォントで動きます |
| Edge か Chrome | Mermaid の図 | 図を使わなければ不要です |

## インストール

1. [最新の Release](https://github.com/ctenopoma/Pubpdf/releases/latest) から `.vsix` ファイルをダウンロードします。
2. ダウンロードしたフォルダのターミナルで、次のコマンドを実行します。版が違うときは、ファイル名を読み替えてください。拡張機能のビューの「...」メニューから「VSIX からのインストール」を選んでも入れられます。

   ```bash
   code --install-extension pubpdf-0.2.0.vsix
   ```

3. VS Code のウィンドウを再読み込みします。
4. コマンドパレット(`Ctrl+Shift+P`)で `Pubpdf: 環境を確認` を実行し、Quarto とフォントの状態を確かめます。

新しい版に更新するときも、同じ手順で入れて、ウィンドウを再読み込みします。

## 使い方

1. Markdown の文書を開きます。
2. エディタ右上の PDF のボタンを押します。コマンドパレットの `Pubpdf: PDF を作成` や、エクスプローラーの右クリックからも実行できます。
3. `Pubpdf: PDF をプレビュー` で、VS Code の中で確認できます。

原稿から PDF を作るときに Quarto と Typst を実行するので、信頼したワークスペースでだけ動きます。

Git で管理している原稿では、`.gitignore` に `.pubpdf/` の行を足しておきます。中間ファイルの置き場所で、消しても問題ありません。

## 設定

設定は、Markdown のタブの右上にある歯車のボタンか、コマンドパレットの `Pubpdf: 設定パネルを開く` で変更します。原稿の先頭に YAML で書くこともできます。

```yaml
---
title: 製品仕様書
author: 開発チーム
history:                       # 表紙の次にバージョン履歴の表を入れる
  - version: 1.0
    date: 2026-11-06
    changes: 初版
pubpdf:
  cover: simple
  toc: 2
  confidential: 社外秘
  confidential-position: both  # none / top-right / bottom-left / both
  page-number: book            # book / right / center / total / none
  font-size: 11                # 本文の文字の大きさ(pt)
  numbering: chapter           # none / chapter(第1章、1.1) / decimal(1、1.1)
  page-count: continuous       # continuous(表紙を 1 として通し番号) / roman
---
```

設定の優先順位は、frontmatter、ワークスペースの設定、ユーザーの設定、既定値の順です。

## マニュアル

原稿の書き方、設定の一覧、合本の作り方、困ったときの対処は、[使い方マニュアル(PDF)](https://github.com/ctenopoma/Pubpdf/releases/latest/download/manual.pdf)を参照してください。
