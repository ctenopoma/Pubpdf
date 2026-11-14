---
title: Pubpdf でできること
subtitle: 原稿の test.md と見比べてください
author: Editor
organization: 見本の組織         # 表紙に出る組織名
date: 20xx-xx-xx
version: "1.0"
history:
  - version: 0.9
    date: 2026-10-01
    changes: 初版
  - version: 1.0
    date: 2026-11-06
    changes:           # 複数あるときはリストで。1項目ずつ改行します
      - 第2章を追加
      - 誤字を修正
doc-number: xxx-xxx-xxx
abstract: この文書は Pubpdf の見本です。ここに書いた概要は、表紙と履歴の次のページに出ます。
pubpdf:
  cover: formal                  # none / simple / formal
  confidential: Confidential(機密表示)
  confidential-position: both    # none / top-right / bottom-left / both
  numbering: chapter             # none / chapter(第1章、1.1) / decimal(1、1.1)
  page-number: center            # book / right / center / total / none
  # font-size: 11                # 本文の文字の大きさ(pt)
  # line-spacing: 1.8            # 行間
  # first-line-indent: true      # 段落の先頭を1文字下げる
  # orientation: landscape       # すべてのページを横向きにする
  # code-line-numbers: true      # すべてのコードに行番号を付ける
  # list-of-figures: true        # 目次の後に図の一覧を出す
  # list-of-tables: true         # 目次の後に表の一覧を出す
  bibliography: test.bib         # 文献のファイル(test.md と同じフォルダに置く)。本文に [@キー] と書いて引用する
  # citation-style: sist02       # 文献の書式。ieee([1])/ sist02((1))/ apa など
  # footnotes: list              # 脚注をページの下ではなく、番号つきの一覧(参考文献)にまとめる
  # table-fit: true              # 短い表を版面いっぱいに広げず、中身の幅に合わせる
  # code-display: show           # コードの見せ方。auto(そのまま、縮める、付録の順)/ show / fit / appendix / attach
  # code-appendix-title: ソースコード  # 1 ページに入らないコードを移す付録の題
  # code-appendix-note: "{ref} を参照"  # 付録へ移したコードの場所に出す文。{ref}、{name}、{lines} が埋まる
  # code-attach: named           # 表示したコードも PDF に添付するか。none(既定)/ all / named(ファイル名のあるものだけ)
  # lint:                        # VS Code で書いている間の文章の点検(組版には使わない)
  #   style: desumasu            # 文体。dearu(である調)/ desumasu / consistent / off
  #   spacing: no-space          # 和文と英数字の間の空白を知らせる
  # columns: 2                   # 本文を 2 段に組む
  # watermark: 下書き            # 背景に斜めの文字を出す
  # logo: docs/manual/img/vscode-panel.png  # 表紙のロゴ
  # header-left: '{title}'       # ヘッダの左。中央と右は header-center、header-right
  # footer-right: '{page} / {total}'  # フッタの右。{page} を書くと自動の番号は出ない
  # accent-color: '#0a7d5a'      # 題、見出し、リンクの色
  # table-style: booktabs        # 表の体裁。grid / lines / booktabs / striped
  # code-theme: github           # コードの配色。github / atom-one / solarized / nord / dracula / monochrome
  # pdf-standard: a-2b           # PDF の規格。a-2b / a-3b / ua-1 / a-2b,ua-1
  book:
    odd-start: false             # true で章を奇数ページから始める(余った偶数ページは白紙)
    gutter: 8                    # 綴じ代(mm)。odd-start が true のときだけ効く
---

# 本書について

この文書は、Pubpdf でできることの見本です。原稿の `test.md` と、作った PDF を見比べてください。

表紙、バージョン履歴、概要、目次、機密表示、ページ番号は、原稿の先頭の YAML から作っています。`#` を外した行の設定も試してみてください。

YAML の値は本文にも差し込めます。この文書の版は {{< meta version >}} で、`{{< meta version >}}` と書いています。

ここに載せたのは代表的な機能だけです。フォントの指定、参考文献、付録、複数の md の合本、ヘッダとフッタの文字、透かし、ロゴ、色、PDF の規格などは、使い方マニュアル(`docs/manual/manual.pdf`)を参照してください。YAML の `#` を外すと試せるものもあります。

# 表、図、数式

## 表の題と番号

表の下に `: 題` を書くと、題と番号が付きます。`{#tbl-名前}` を付けると、`@tbl-名前` で参照できます。

| 設定 | 内容 |
|---|---|
| `cover` | 表紙の型 |
| `numbering` | 見出しの番号の形 |
| `page-number` | ページ番号の位置 |

: よく使う設定 {#tbl-settings}

@tbl-settings は、題の行の `{#tbl-settings}` を参照しています。

表は版面の幅いっぱいに広げます。中身の短い表は、題に `.fit` を書くと中身の幅になります(@tbl-fit)。文書のすべての表をそうするには、YAML の `table-fit: true` を使います。

| 記号 | 意味 |
|---|---|
| ○ | 合格 |
| × | 不合格 |
| － | 対象外 |

: 中身の幅に合わせた表 {#tbl-fit .fit}

## 図の番号と寄せ

画像の後ろの `{ }` に、ID、幅、寄せを書けます。

![VS Code の設定パネル](docs/manual/img/vscode-panel.png){#fig-panel width=60% fig-align="center"}

@fig-panel のように、図も番号で参照できます。

幅は、Zenn の書き方で px の数でも指定できます(`![説明](パス =240x)`)。`=50%x` は本文の幅に対する割合です。図のブロック(Mermaid と Pubpdf が描く図)では、先頭に `%%| width: 240` か `%%| width: 50%` と書きます。

![](docs/manual/img/vscode-preview.png =240x)

題のない画像も中央に置きます。左や右に寄せるときは `{fig-align="left"}` を付けます(図のブロックでは `%%| fig-align: left`)。

## Mermaid の図

コードブロックの言語を `mermaid` にすると、図になります。`%%|` の行で番号と題を付けられます。Pubpdf は、Mermaid の図をほかの図と同じ色とフォントで描かせ、flowchart の線を角の丸い折れ線にします。

```mermaid
%%| label: fig-flow
%%| fig-cap: PDF ができるまで
flowchart LR
    A[Markdown の原稿] --> B[Pubpdf] --> C[PDF]
```

判断の菱形、subgraph の枠、破線の矢印は @fig-mermaid-flowchart のようになります。

```mermaid
%%| label: fig-mermaid-flowchart
%%| fig-cap: 判断と subgraph のある flowchart
flowchart TB
  S([注文を受ける]) --> Q{在庫がある}
  Q -- はい --> R[引き当てる]
  Q -- いいえ --> P[生産を依頼する]
  subgraph W[倉庫の作業]
    R --> K[ピッキングする] --> H[梱包して出荷する]
  end
  P -. 完成したら .-> R
```

```mermaid
%%| label: fig-mermaid-sequence
%%| fig-cap: シーケンス図
sequenceDiagram
  actor U as 利用者
  participant W as 画面
  participant S as サーバ
  U ->> W: 注文を確定する
  W ->> S: 注文を登録する
  activate S
  alt 在庫がある
    S -->> W: 受注番号
  else 在庫がない
    S -->> W: 回答納期
  end
  deactivate S
  Note over W,S: 通信は HTTPS
  W -->> U: 結果を表示する
```

```mermaid
%%| label: fig-mermaid-class
%%| fig-cap: クラス図
classDiagram
  direction LR
  class Order["受注"] {
    -受注番号
    -受注日
    +確定する()
  }
  class OrderLine["受注明細"] {
    -数量
    +引き当てる()
  }
  class Product["製品"] {
    -製品コード
  }
  Order "1" *-- "1..*" OrderLine
  OrderLine --> Product
```

```mermaid
%%| label: fig-mermaid-state
%%| fig-cap: 状態遷移図
stateDiagram-v2
  direction LR
  [*] --> 受付: 登録
  受付 --> 引当済: 引き当てる
  引当済 --> 出荷済: 出荷する
  受付 --> 取消: 取り消す
  引当済 --> 取消: 取り消す
  出荷済 --> [*]
  取消 --> [*]
```

```mermaid
%%| label: fig-mermaid-er
%%| fig-cap: Mermaid の ER 図
erDiagram
  得意先 ||--o{ 受注 : 発注
  受注 ||--|{ 受注明細 : 含む
  製品 ||--o{ 受注明細 : 注文
  受注 {
    string 受注番号 PK
    string 得意先コード FK
    date 受注日
  }
```

@fig-mermaid-er と同じ書き方で、言語を `er` にすると、Pubpdf が描きます(@fig-er)。

`%%{init: {"theme": "default"}}%%` のように theme を選ぶと、Mermaid の元の見た目になります(@fig-mermaid-default)。

```mermaid
%%| label: fig-mermaid-default
%%| fig-cap: theme を選んだ図(Mermaid の元の見た目)
%%{init: {"theme": "default"}}%%
flowchart LR
    A[Markdown の原稿] --> B[Pubpdf] --> C[PDF]
```

## 数式

独立した式には、自動で番号が入ります。

$$
a^2 + b^2 = c^2
$$

`{#eq-名前}` を付けると、`@eq-名前` で参照できます。

$$
E = mc^2
$$ {#eq-energy}

@eq-energy のように参照できます。番号を入れない式には `\notag` を書きます。

$$
\int_0^1 x^2 \, dx = \frac{1}{3} \notag
$$

文中の式は $f(x) = x^2$ のように書きます。日本語との間は自動で少し空きます。

# コードと囲み

## ファイル名つきのコード

言語名の後に `: ファイル名` を書くと、左上にファイル名が出ます。YAML で `code-attach: named` にすると、このコードを `app.py` という名前で PDF の添付ファイルにもでき、書いたとおりの文字(字下げを含む)で取り出せます。添付ファイルのある PDF は会社によっては受け取れないので、既定では添付しません。

```python: app.py
def greet(name):
    return f"こんにちは、{name} さん"
```

`include` にファイルのパスを書くと、ファイルの中身をコードとして載せます。次のコードは、同じフォルダの `test-files/hello.py` を参照しています。

```{.python include="test-files/hello.py"}
```

長いコードは、文字を縮めて 1 ページに収め、それでも入らなければ文書の最後の付録へ移します(`code-display: auto`)。`.appendix` を書くと、大きさによらず付録へ移します。付録へ移したコードの場所には、既定では「このコード(10 行)は、付録の A.1 に載せています。」の文が出ます。文は YAML の `code-appendix-note` で書き換えられ、コードごとには `note` で上書きできます(`{ref}` は付録の節へのリンク、`{name}` はファイル名、`{lines}` は行数)。

```{.python .appendix include="test-files/hello.py" filename="hello-appendix.py" note="{name}({lines} 行)は {ref} に載せています。"}
```

## 行番号つきのコード

`code-line-numbers="true"` を付けると、行番号が出ます。

```{.python code-line-numbers="true"}
for i in range(3):
    print(i)
```

## 差分(diff)

言語名を `diff` にすると、`+` の行に薄い緑、`-` の行に薄い赤の背景が付きます。Zenn の ```` ```diff js ```` や Qiita の ```` ```diff_javascript ```` のように言語名も書くと、その言語で色分けします。

```diff js:price.js
 const total = items.length;
-const tax = 0.08;
+const tax = 0.10;
```

## 色付きの囲み

`:::` の記法で書けます。

:::message
`:::message` は黄色の囲みです。
:::

:::note warn
`:::note warn` はオレンジの囲みです。
:::

:::message alert
`:::message alert` は赤の囲みです。
:::

:::details 詳しい説明の題
`:::details 題` は灰色の囲みです。PDF では中身を常に表示します。
:::

## 文字の寄せ

`::: {.right}` の囲みの中は右に、`::: {.center}` の囲みの中は中央に寄ります。行の途中で改行するときは、行末に `\` を書きます。

::: {.right}
2026年11月7日\
**開発チーム**
:::

::: {.center}
以上
:::

## 段組み

`::: {.columns}` の囲みの中は 2 段に組みます。`count` で段数を変えられ、段の長さは自動で揃います。

::: {.columns}
段組みにした文章は、左の段から右の段へ流れます。長い説明の一部だけを段組みにしたいときに使います。文書全体を段組みにするときは、YAML の `columns` を使います。
:::

`.column` の囲みを並べると、幅を指定して横に並べられます。

::: {.columns}
::: {.column width="30%"}
左の列(30%)
:::

::: {.column width="70%"}
右の列(70%)。説明と図を左右に並べたいときなどに使います。
:::
:::

# Markdown を拡張した記法

通常の Markdown にはない記法のうち、代表的なものです。

## 文字の修飾

| 書き方 | 組み上がり |
|---|---|
| `~~取り消し~~` | ~~取り消し~~ |
| `H~2~O` | H~2~O |
| `x^2^` | x^2^ |
| `[下線]{.underline}` | [下線]{.underline} |
| `[蛍光ペン]{.mark}` | [蛍光ペン]{.mark} |

: 文字の修飾

文中のコードには、`print()` のように薄い灰色の角丸の背景が付きます(`inline-code-background: false` で消せます)。`:smile:` のような絵文字の名前は、絵文字(:smile:)になります。

## パスと URL

共有フォルダのパスや長い URL は、文中のコードに `{.path}` を付けると、背景と枠が付き、`\` と `/` の後ろで改行できます。`\` は書いたとおりに出ます。`\\fileserver\share\設計\2026\基本設計書.docx`{.path} に置きます。URL はリンクになります。`https://github.com/ctenopoma/Pubpdf/releases/latest`{.path} から入手します。

## HTML のタグ

Qiita や Zenn 向けに書いた HTML のタグも使えます。<kbd>Ctrl</kbd>+<kbd>S</kbd> で保存します(`<kbd>`)。x<sup>2</sup> と H<sub>2</sub>O、<mark>蛍光ペン</mark>、<font color="red">赤い字</font> も書けます。

<details><summary>HTML の折りたたみ</summary>

`<details><summary>題</summary>` は、`:::details 題` と同じ灰色の囲みになります。

</details>

## 脚注とチェックリスト

文の途中に `^[脚注の文]` と書くと、ページの下に脚注が出ます^[これが脚注の文です。]。

`[^名前]` と書いて、本文の後に `[^名前]: 脚注の文` を書くこともできます。同じ箇所で複数の脚注を引くときは `[^a,b]` と並べます[^first,second]。

[^first]: 並べた脚注の 1 つ目です。
[^second]: 並べた脚注の 2 つ目です。

行の先頭に `- [x]` か `- [ ]` と書くと、チェックリストになります。

- [x] 終わった作業
- [ ] まだの作業

## 文献の引用と参考文献

YAML の `bibliography` に `.bib` のファイルを指定すると、本文に `[@キー]` と書いて引用できます。この見本は、同じフォルダの `test.bib` を使っています。組版の教科書 [@knuth1984] と、Markdown の仕様 [@commonmark] を引用しました。ページも書けます [@knuth1984, p. 10]。複数をまとめて引用することもできます [@commonmark; @sigmaframe2013]。

```markdown
組版の教科書 [@knuth1984] と、Markdown の仕様 [@commonmark] を引用しました。
```

```text
@book{knuth1984,
  title = {The TeXbook},
  author = {Knuth, Donald E.},
  year = {1984},
  publisher = {Addison-Wesley},
}
```

引用した文献は、「参考文献」の一覧に番号順に並びます。一覧は、`::: {#refs}` と `:::` の 2 行を書いた位置に出ます。書かなければ文書の最後に出ます。この見本では、最後の章「ページの制御」の前に置いています。引用の形は `citation-style` で選びます(既定は [1] の形の IEEE)。

文献のファイルを用意しないときは、脚注で引用を書けます。YAML に `footnotes: list` と書くと、脚注をページの下ではなく番号つきの一覧にまとめ、本文には [1] の形で番号を出します(Zenn の脚注と同じ書き方です)。同じ脚注を何度引いても同じ番号です。

```markdown
組版の教科書[^tex]を参照しました。

[^tex]: D. E. Knuth, The TeXbook, Addison-Wesley, 1984.
```

## 注意書きの囲み

`:::message` のほかに、Quarto の書き方もあります。`callout-note`、`callout-tip`、`callout-warning`、`callout-important`、`callout-caution` の 5 種類です。

::: {.callout-note title="題を書けます"}
`::: {.callout-note title="題"}` の囲みです。
:::

::: {.callout-warning}
`::: {.callout-warning}` の囲みです。
:::

## 定理と証明

`{#thm-名前}` の囲みに番号が付き、`@thm-名前` で参照できます。定義は `def-`、補題は `lem-`、例は `exm-` で始めます。

::: {#thm-pythagoras}
## 三平方の定理
直角三角形では $a^2 + b^2 = c^2$ です。
:::

@thm-pythagoras の証明は次のとおりです。

::: {.proof}
`::: {.proof}` の囲みです。
:::

## 図の横並び

`::: {#fig-名前 layout-ncol=2}` の囲みに画像を並べると、横に並びます。最後の行が全体の題です。

::: {#fig-side layout-ncol=2}
![設定パネル](docs/manual/img/vscode-panel.png){#fig-side-a}

![プレビュー](docs/manual/img/vscode-preview.png){#fig-side-b}

横に並べた図
:::

@fig-side の全体と、@fig-side-a の個々の図を参照できます。

## 見出しへの参照 {#sec-reference}

見出しの後ろに `{#sec-名前}` と書くと、`@sec-名前` で参照できます。この節は @sec-reference です。番号を付けない見出しには `{.unnumbered}` と書きます。

## 表の網掛けとセルの中の改行

セルの中身を `[文字]{.shade}` と書くと、網掛けになります。`<br>` でセルの中を改行します。`<br>` で区切った行を `- ` で始めると箇条書き、`1. ` で始めると番号つきのリストになります。

| 項目 | 内容 |
|---|---|
| [PU ID]{.shade} | PU-0101 |
| [処理内容]{.shade} | 温度を読む<br>PV を更新する |
| [確認]{.shade} | 次の 2 点<br>- 上限を超えていない<br>- 下限を下回っていない |
| [手順]{.shade} | 1. 読む<br>2. 比べる<br>3. 記録する |

: 網掛けと改行のある表

## HTML の表

`<table>` で書いた表も組めます。`rowspan` と `colspan` でセルを結合できます。

<table>
<tr><th rowspan="2">機能</th><th colspan="2">エンティティ</th></tr>
<tr><th>顧客</th><th>受注</th></tr>
<tr><td>受注の登録</td><td>R</td><td>C</td></tr>
</table>

: HTML で書いた表

## 記入の指示と小さい文字の表

テンプレートの書き方の説明は、`::: {.guide}` の囲みに書きます。設定の `guides: false` で組むと消えます。

::: {.guide}
＊ ここに本書の目的を書く。
:::

表の題に `.small` を書くと、その表の文字が小さくなります。`tbl-colwidths` で列の幅の比も決められます。

| ID | 分類 | 内容 | 期待結果 | 結果 |
|---|---|---|---|---|
| T-01 | 起動 | 電源を入れて起動を確かめる | 3 秒以内に停止の状態になる | ○ |

: 文字を小さくした表 {.small tbl-colwidths="[10,10,40,30,10]"}

## Typst を直接書く

コードブロックの言語を `{=typst}` にすると、Typst の記法を直接書けます。設定や Markdown で足りないときに使います。

```{=typst}
#text(fill: rgb("#0a7d5a"))[Typst で色を付けた文字です。]
```

## そのほかの記法

| 書き方 | 内容 |
|---|---|
| `[@キー]` | 文献の引用。YAML の `bibliography` に `.bib` ファイルを指定します |
| `::: {#refs}` と `:::` | 参考文献の一覧を置く位置 |
| `# 見出し {.appendix}` | 付録にします。「付録 A」と番号が付きます |
| `{{< meta version >}}` | YAML の値を差し込みます |
| `{{< pagebreak >}}` | 改ページします |
| `::: {.landscape}` | その部分を横向きのページにします |

: そのほかの記法

# Pubpdf が描く図

コードブロックの言語を次の名前にすると、図になります。文字は検索でき、ブラウザも要りません。`%%| label: fig-名前` で参照でき、`%%| fig-cap: 題` で題と番号が付きます。

| 言語 | 図 | 書き方 |
|---|---|---|
| `tree` | ディレクトリ構造 | 字下げか `tree` コマンドの出力 |
| `chart` | 棒、折れ線、円グラフ | Markdown の表 |
| `schedule` | 工程表 | 「作業: 期間」の行 |
| `bits` | ビット配置 | 「ビット数 名前」の行 |
| `layers` | 層構造 | 1 行が 1 層。縦棒で区切る |
| `timing` | 信号の波形 | 「名前: 波形」の行 |
| `wbs` | 作業分解、組織図 | 字下げ |
| `wireframe` | 画面の模式図 | `[ボタン]` や `"入力"` の行 |
| `data` | JSON と YAML の図 | JSON か YAML |
| `network` | ネットワーク図 | ネットワークの行と字下げした機器の行 |
| `usecase` | ユースケース図 | 「利用者: 機能, 機能」の行 |
| `swimlane` | スイムレーンの業務フロー | 「レーン: 記号 文字」の行 |
| `fta` | 故障の木(FTA) | 字下げ。下に事象のある事象は先頭に AND か OR |
| `grid` | 帳票と画面の方眼 | 「行, 桁: 文字」の行 |
| `er` | ER 図 | Mermaid の erDiagram と同じ。置き場所は表の形の行 |
| `screenflow` | 画面遷移図 | 「画面 -> 操作: 画面」の行。置き場所は表の形の行 |

: 図の種類

代表的なものを載せます。残りの書き方は、使い方マニュアルを参照してください。

## ディレクトリ構造

```tree
%%| label: fig-tree
%%| fig-cap: 説明つきのディレクトリ構造
project/
  src/               # ソースコード
    main.py          # 入口
    共通処理.py       # 日本語の名前でも線がずれません
  docs/
    manual.md
  README.md
```

@fig-tree は字下げで書いています。`#` の後ろは右の列の説明になります。

## グラフ

```chart
%%| label: fig-chart
%%| fig-cap: 表から作ったグラフ
unit: 万円
lines: 費用            # 折れ線にする列。type: line、type: pie も書けます
| 月 | 売上 | 費用 |
|---|---|---|
| 4月 | 120 | 90 |
| 5月 | 135 | 95 |
| 6月 | 128 | 92 |
```

## 工程表

```schedule
%%| fig-cap: 組むたびに変わらない工程表
columns: 4月, 5月, 6月, 7月, 8月, 9月
設計
基本設計: 4月-5月
詳細設計: 5月-6月
開発
実装: 6月-8月
結合試験: 8月-9月
◆ リリース: 9月
```

`2026-04-01 ~ 2026-05-15` のように日付でも書けます。行の先頭の `◆` は節目の印です。

## ビット配置

```bits
%%| fig-cap: ヘッダの形式
width: 16
4 版
4 長さ
8 種別
16 チェックサム
```

## 信号の波形

```timing
%%| fig-cap: 読み出しの波形
clk: p.......
req: 0.1...0.
data: x..=.=.x A, B
```

`p` はクロック、`0` と `1` は信号の高さ、`x` は不定、`=` は値、`.` は前の続きです。

## 作業分解

```wbs
%%| fig-cap: 作業分解
プロジェクト
  設計
    基本設計
    詳細設計
  開発
    実装
    単体試験
  試験
    結合試験
```

## 故障の木

```fta
%%| label: fig-fta
%%| fig-cap: 葉の多い故障の木
OR 搬送装置が<br>停止しない
  AND 非常停止が効かない
    非常停止ボタンの接点の溶着
    安全リレーの故障
    \OR 回路の誤配線
  OR 制御が停止を指示しない
    センサの故障
    通信の途絶を検知しない
    プログラムの誤り
    ◇ 保守作業による改変
  OR 駆動が止まらない
    インバータの故障
    ブレーキの摩耗
    電磁接触器の溶着
```

基本の事象が多くて横に入らないので、@fig-fta はゲートの下に縦に並べています。名前の中の `<br>` は改行です。`OR` で始まる名前は、先頭に `\` を付けて書きます。

## ER 図

```er
%%| label: fig-er
%%| fig-cap: ER 図(er)
| 社員   | 受注 | 受注明細 |
| 得意先 |      | 製品     |
社員 ||--o{ 受注 : 担当
得意先 ||--o{ 受注 : 発注
受注 ||--|{ 受注明細 : 含む
製品 ||--o{ 受注明細 : 注文
社員 |o..o{ 得意先 : 営業担当
受注 ORDER_HEADER {
  string 受注番号 PK
  string 得意先コード FK
  string 担当者コード FK
  date 受注日
}
受注明細 ORDER_DETAIL {
  受注番号 PK, FK
  明細番号 PK
  製品コード FK
  数量
}
得意先 CUSTOMER {
  得意先コード PK
  得意先名
}
```

先頭の `|` の行が箱の置き場所です。属性を書かない箱(社員、製品)は小さな箱になります。`..` の関係(営業担当)は破線になります。

## 画面遷移図

```screenflow
%%| label: fig-screenflow
%%| fig-cap: 画面遷移図
| SC-01 ログイン |                | SC-90 エラー   |
| SC-02 メニュー |                |                |
| SC-03 注文入力 | SC-04 商品検索 | SC-05 注文履歴 |
| RP-01 注文書   | EX-01 決済代行 |                |
小画面: SC-04
帳票: RP-01
共通: SC-90
外部: EX-01
SC-01 -> ログイン: SC-02
SC-02 -> 注文: SC-03, 履歴: SC-05
SC-03 -> 検索: SC-04
SC-04 -> 選択: SC-03
SC-03 -> 確定: RP-01
SC-03 ..> 支払い: EX-01
```

画面は窓の形、別ウィンドウの小画面は破線の枠、帳票は文書の形、どの画面からも移るエラーの画面は黄色、ほかのシステムは灰色の箱で描きます。

::: {#refs}
:::

# ページの制御

## 横向きのページ

幅の広い表などは `.landscape` の囲みに入れると、その部分だけ横向きのページになります。

::: {.landscape}

| 項目 | 4月 | 5月 | 6月 | 7月 | 8月 | 9月 | 10月 | 11月 | 12月 | 1月 | 2月 | 3月 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 売上 | 120 | 135 | 128 | 142 | 150 | 138 | 160 | 155 | 170 | 148 | 152 | 180 |
| 費用 | 90 | 95 | 92 | 101 | 108 | 99 | 112 | 110 | 118 | 104 | 107 | 121 |

: 横向きのページに置いた表

:::

## 改ページ

改ページしたい場所に、`{{< pagebreak >}}` か `\newpage` を1行で書きます。次の行で改ページします。

{{< pagebreak >}}

このページは、前の行で改ページした後のページです。ページ番号は表紙を1として通しで数えています。
