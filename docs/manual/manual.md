---
title: Pubpdf 使い方マニュアル
subtitle: Markdown から本の体裁の PDF を作る
author: Pubpdf プロジェクト
date: 2026-11-07
version: "1.3"
doc-number: PUBPDF-MAN-001
history:
  - version: 0.1
    date: 2026-11-06
    changes: 初版
  - version: 0.2
    date: 2026-11-06
    changes: VS Code 拡張機能、表の題、機密表示の位置、フォント、囲み、ファイル名つきコードブロックの説明を追加
  - version: 0.3
    date: 2026-11-06
    changes: ページの通し番号とバージョン履歴の説明を追加
  - version: 0.4
    date: 2026-11-06
    changes: 文字の大きさ、余白、番号の形式、式の自動の番号、改ページ、図の寄せ、コードの行番号の説明を追加
  - version: 0.5
    date: 2026-11-07
    changes: 見本の原稿 test.md の案内を追加
  - version: 0.6
    date: 2026-11-07
    changes: 文字を右や中央に寄せる書き方の説明を追加
  - version: 0.7
    date: 2026-11-07
    changes: 参考文献、図と表の一覧、付録、概要、値の差し込みの説明を追加
  - version: 0.8
    date: 2026-11-07
    changes: 段組み、ヘッダとフッタの文字、透かし、ロゴと組織名、テーマの色、表の体裁、コードの配色、PDF の文書情報と規格の説明を追加
  - version: 0.9
    date: 2026-11-07
    changes: Mermaid にない図の説明と、URL の画像を読み込まないことの説明を追加
  - version: "1.0"
    date: 2026-11-08
    changes: 承認欄、履歴の列、見出しの番号の形、節ごとの図表の番号、表の網掛け、セルの中の改行、HTML の表の説明を追加
  - version: "1.1"
    date: 2026-11-08
    changes: スイムレーン、FTA、方眼の図、記入の指示の囲み、履歴の様式、ヘッダとフッタの罫線、表紙の枠、表の列の幅と文字の大きさの説明を追加
  - version: "1.2"
    date: 2026-11-08
    changes: ER 図と画面遷移図の説明、Mermaid の図の見た目の説明、見本とテンプレートの案内を追加
  - version: "1.3"
    date: 2026-11-09
    changes: H1 が 1 つでも題にしないことと、表紙がないときは title に書いた題だけを 1 ページ目に出すことを追記
pubpdf:
  cover: formal
  confidential: Confidential
  confidential-position: both
  numbering: chapter
  book:
    odd-start: true
    gutter: 8
  chapters:
    - 01-overview.md
    - 02-quickstart.md
    - 03-metadata.md
    - 04-settings.md
    - 05-book.md
    - 06-writing.md
    - 07-vscode.md
    - 08-troubleshooting.md
---

# 本書について

本書は、Markdown で書いた原稿を Pubpdf で PDF にする人のための手引きです。Quarto や Typst の知識がなくても読めるように書いています。

PDF は、VS Code 拡張機能で作ります。

## 目的別の読み方

| やりたいこと | 読む章 |
|---|---|
| まず1つ PDF を作りたい | [はじめての PDF](02-quickstart.md) |
| タイトルや著者を入れたい | [文書情報の書き方](03-metadata.md) |
| 設定の値を調べたい | [設定一覧](04-settings.md) |
| 両面印刷や製本を前提に組みたい、複数の md を1冊にしたい | [本として組む](05-book.md) |
| 段組み、ヘッダとフッタの文字、透かし、色、PDF の規格を指定したい | [設定一覧](04-settings.md) |
| 表、コード、数式、囲み、段組みの書き方を知りたい | [原稿の書き方](06-writing.md) |
| ディレクトリ構造、グラフ、工程表などの図を描きたい | [原稿の書き方](06-writing.md#sec-figures) |
| VS Code のボタンや設定パネルの使い方を知りたい | [VS Code での操作](07-vscode.md) |
| エラーや警告が出た | [困ったときは](08-troubleshooting.md) |

: 目的別の読み方

## 本書自身について

本書も Pubpdf で組んでいます。原稿は `docs/manual/` にあり、`manual.md` を開いて PDF を作ると同じものができます。

右上と左下の Confidential は、機密表示の見本として付けたものです。本書が機密文書という意味ではありません。
