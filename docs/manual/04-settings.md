# 設定一覧

設定は frontmatter の `pubpdf:` の下に書きます。VS Code では、設定パネルからも変更できます。@tbl-settings に全項目をまとめます。

| キー | 値 | 既定 | 内容 |
|---|---|---|---|
| `cover` | `none`、`simple`、`formal` | `none` | 表紙の型 |
| `cover-frame` | `true`、`false` | `false` | 表紙を二重の線で囲む |
| `approval-stamp` | `true`、`false` | `false` | 承認欄の押印欄 |
| `history-number` | `true`、`false` | `false` | バージョン履歴の項番の列 |
| `history-columns` | 列のリスト | なし | バージョン履歴の列の順と見出し |
| `history-title` | 文字列 | `バージョン履歴` | バージョン履歴のページの題 |
| `history-blank-rows` | 0 から 50 | `0` | バージョン履歴の手書き用の空の行 |
| `guides` | `true`、`false` | `true` | 記入の指示(`::: {.guide}`)を出すか |
| `confidential` | `false`、`true`、文字列 | `false` | 機密表示の文字 |
| `confidential-position` | `none`、`top-right`、`bottom-left`、`both` | `top-right` | 機密表示の位置 |
| `logo` | 原稿のフォルダの中の画像 | なし | 表紙のロゴ |
| `watermark` | 文字列 | なし | 透かしの文字 |
| `header-left`、`header-center`、`header-right` | 文字列 | 左は章の名前 | ヘッダの文字 |
| `footer-left`、`footer-center`、`footer-right` | 文字列 | なし | フッタの文字 |
| `header-rule`、`footer-rule` | `true`、`false` | `false` | ヘッダの下とフッタの上の罫線 |
| `columns` | `1`、`2`、`3`、`4` | `1` | 本文の段数 |
| `accent-color` | `"#0a7d5a"` の形の色 | なし | テーマの色 |
| `table-style` | `grid`、`lines`、`booktabs`、`striped` | `grid` | 表の体裁 |
| `code-theme` | `default`、`github`、`atom-one`、`solarized`、`nord`、`dracula`、`monochrome` | `default` | コードの配色 |
| `pdf-standard` | `none`、`a-2b`、`a-3b`、`ua-1`、`a-2b,ua-1` | `none` | PDF の規格 |
| `toc` | `false`、`true`、`1`、`2`、`3` | `2` | 目次の有無と深さ |
| `list-of-figures` | `true`、`false` | `false` | 図の一覧 |
| `list-of-tables` | `true`、`false` | `false` | 表の一覧 |
| `paper` | `a3`、`a4`、`a5`、`b4`、`b5`、`letter`、`legal` | `a4` | 用紙サイズ |
| `orientation` | `portrait`、`landscape` | `portrait` | 用紙の向き |
| `margin` | `top`、`bottom`、`inner`、`outer` に数値(mm) | 用紙で決まる | 余白 |
| `font-size` | 数値(pt)。5 から 30 | `10.5`。A5 は `9.5` | 本文の文字の大きさ |
| `line-spacing` | 数値。1 から 3 | `1.6` | 行間 |
| `first-line-indent` | `true`、`false` | `false` | 段落の字下げ |
| `page-number` | `book`、`right`、`center`、`total`、`none` | `center`。奇数ページ始まりでは `book` | ページ番号の出し方 |
| `page-count` | `continuous`、`roman` | `continuous` | ページの数え方 |
| `numbering` | `none`、`chapter`、`decimal` | `none` | 見出しの番号 |
| `heading-format` | 番号の形のリスト | なし | 階層ごとの見出しの番号の形 |
| `figure-numbering` | `chapter`、`section`、`continuous` | 見出しの番号があれば `chapter` | 図、表、コード、式の番号 |
| `equation-numbering` | `all`、`labeled` | `all` | 番号を入れる式 |
| `code-line-numbers` | `true`、`false` | `false` | コードの行番号 |
| `chapter-break` | `true`、`false` | `true` | 章の前の改ページ |
| `book.odd-start` | `true`、`false` | 単一 md は `false`、合本は `true` | 奇数ページ始まり |
| `book.gutter` | 数値(mm) | `8` | 綴じ代 |
| `chapters` | ファイルのリスト | なし | 合本にする章 |
| `appendices` | ファイルのリスト | なし | 付録にする章 |
| `bibliography` | 原稿のフォルダの中の `.bib` | なし | 文献のファイル |
| `citation-style` | `ieee`、`sist02` など | `ieee` | 文献の書式 |
| `output` | 原稿のフォルダの中の `.pdf` | `<原稿名>.pdf` | 出力先 |
| `font` | フォント名 | 自動 | 本文のフォント |
| `font-heading` | フォント名 | 本文と同じ | 見出しと題のフォント |
| `font-code` | フォント名 | DejaVu Sans Mono | コードのフォント |
| `font-math` | 数式用のフォント名 | New Computer Modern Math | 数式のフォント |
| `font-paths` | パス、またはそのリスト | なし | フォントの読み込み先 |

: pubpdf の設定項目 {#tbl-settings}

## 表紙

`cover` で表紙の型を選びます。

```yaml
pubpdf:
  cover: formal
```

| 値 | 内容 |
|---|---|
| `none` | 表紙なし。1ページ目の先頭に題を出します |
| `simple` | 題、副題、著者、日付だけの表紙 |
| `formal` | 文書番号、版数、発行日、作成者の表が付いた表紙 |

: 表紙の型

`formal` の表には、frontmatter に書いた項目だけが出ます。

`cover-frame: true` で、表紙を二重の線の枠で囲みます(IPA の様式の表紙の形です)。

### ロゴと組織名

`logo` に画像を指定すると、表紙の上部に出します。`simple` では左上、`formal` では中央です。組織名は frontmatter の `organization` に書きます。`simple` では著者の下、`formal` では表の「組織」の行に出ます。

```yaml
organization: 株式会社見本
pubpdf:
  cover: simple
  logo: images/logo.png
```

- 使える画像は、原稿のフォルダの中の png、jpg、gif、svg、webp、pdf です。フォルダの外を指定すると、警告を出して使いません。
- ロゴは縦横比を保って、幅 6cm、高さ 2cm の枠に収めます。
- 表紙がないときは、`logo` は警告を出して使いません。`organization` は 1ページ目の題の下に出ます。

## 機密表示

`confidential` に表示する文字を、`confidential-position` に位置を指定します。

```yaml
pubpdf:
  confidential: 社外秘
  confidential-position: both
```

| 位置の値 | 表示する場所 |
|---|---|
| `none` | 出さない |
| `top-right` | 右上のみ |
| `bottom-left` | 左下のみ |
| `both` | 右上と左下 |

: 機密表示の位置

- 文字だけを指定すると右上に出します。位置だけを指定すると「Confidential」と出します。`true` と書いても「Confidential」になります。
- 表紙、目次、章の開始ページにも出します。自動で入る白紙には出しません。
- 偶数ページでも同じ位置に出します。製本すると、偶数ページの右上は綴じ側に来ます。
- book 形式のページ番号と左下の機密表示が重なる偶数ページでは、番号を外側に置き、その右に機密表示を並べます。

::: {.callout-warning title="見た目だけの表示です"}
機密表示は文字を印刷するだけで、PDF を保護するものではありません。誰でも開いて読めます。
:::

## 透かし

`watermark` に書いた文字を、ページの背景に斜めに薄く出します。

```yaml
pubpdf:
  watermark: 下書き
```

- 文字はページの対角線に沿って置き、長さに合わせて大きさを決めます。
- 表紙を含むすべてのページに出します。自動で入る白紙には出しません。
- 本文の後ろに出るので、色のある表や画像に隠れることがあります。
- 機密表示と同じく、見た目だけの表示です。文字は PDF から検索でき、閲覧を制限するものではありません。

## 目次

```yaml
pubpdf:
  toc: 3
```

数字は目次に載せる見出しの深さです。`false` で目次を出しません。`true` は `2` と同じです。見出しが1つもない文書には、目次を出しません。

## 図と表の一覧

```yaml
pubpdf:
  list-of-figures: true
  list-of-tables: true
```

目次の後に、「図目次」と「表目次」を出します。載るのは、Markdown で書いた番号のある図と表です。横に並べた個々の図は載らず、全体の題だけが載ります。Typst を直接書いて作った図は載りません。該当する図や表が1つもなければ、一覧を出しません。

## 参考文献

`bibliography` に文献のファイルを指定すると、本文から引用でき、文書の最後に文献の一覧が出ます。書き方は[原稿の書き方](06-writing.md#sec-citations)を参照してください。

```yaml
pubpdf:
  bibliography: refs.bib
  citation-style: sist02
```

| `citation-style` の値 | 本文の引用の形 |
|---|---|
| `ieee` | [1] |
| `sist02` | (1) |
| `springer-vancouver` | (1) |
| `nature` | 上付きの 1 |
| `apa` | (Knuth, 1984) |
| `chicago-author-date` | (Knuth 1984) |
| `mla` | (Knuth) |

: 文献の書式

原稿のフォルダの中の `.csl` ファイルを指定して、他の書式を使うこともできます(`citation-style: my-journal.csl`)。

## 用紙サイズと向き

```yaml
pubpdf:
  paper: b5
  orientation: landscape
```

`b4` と `b5` は JIS の寸法です(B5 は 182 × 257mm)。余白と本文の文字の大きさは、用紙に合わせて自動で決まります。

`orientation: landscape` で文書全体を横向きにします。一部のページだけを横向きにする方法は、[原稿の書き方](06-writing.md#sec-landscape)を参照してください。

## 余白

```yaml
pubpdf:
  margin:
    top: 30
    bottom: 25
    inner: 28
    outer: 20
```

単位は mm です。書かなかった辺は既定のままです。既定は上が 27、下が 24 です。左右は用紙で決まり、A3 は 30、B4 は 26、A4、Letter、Legal は 24、B5 は 20、A5 は 16 です。

`inner` と `outer` の意味は、奇数ページ始まりの設定で変わります。

| 奇数ページ始まり | `inner` | `outer` |
|---|---|---|
| オン | 綴じる側(綴じ代はこの値に足します) | 綴じない側 |
| オフ | 左に固定 | 右に固定 |

: 内側と外側の余白

余白や綴じ代が大きすぎて、本文の幅か高さが 50mm 未満になるときは、警告を出して既定の値で組みます。一部のページだけが横向きの文書では、用紙の短い辺でも確かめます。

## 段組み

`columns` で本文の段数を指定します。本文の一部だけを段組みにする方法は、[原稿の書き方](06-writing.md#sec-columns)を参照してください。

```yaml
pubpdf:
  columns: 2
```

- 表紙、履歴、概要のページ、目次は 1 段のままで、本文から段組みにします。
- 前付けがない文書では、題と概要を段の上に通して出し、同じページから段組みを始めます。
- 新しいページから始まる章の題は、段の上に通して出します。`chapter-break: false` では段の中に出します。
- 長い概要(版面の 3 分の 1 ほどを超えるもの)は、題の下ではなく概要のページに出します。
- 独立した式は折り返さないので、段の幅より長い式は段からはみ出します。
- 最後のページでは、左の段から順に埋めるので、段の長さは揃いません。
- 段の間は 6mm です。段の幅が 30mm より狭くなるときは、警告を出して 1 段で組みます。

## 文字の大きさと行間

```yaml
pubpdf:
  font-size: 11
  line-spacing: 1.8
  first-line-indent: true
```

`font-size` は本文の文字の大きさです。見出し、コード、表、数式も比例して変わります。ヘッダ、フッタ、表紙の題は変わりません。

`line-spacing` は、文字の大きさに対する行送りの倍率です。段落の間隔も行間に合わせて広がります。表とコードの行間は変わりません。

`first-line-indent: true` にすると、本文の段落の先頭を1文字下げます。リスト、引用、囲み、表、図の題、脚注は下げません。

## ページ番号

`page-number` で番号の出し方を選びます。表紙には番号を出しません。

| 値 | 出し方 |
|---|---|
| `book` | book 形式。紙の上で奇数枚目は右下、偶数枚目は左下 |
| `right` | 右下に固定 |
| `center` | 中央に固定 |
| `total` | 中央に「3 / 12」の形で出す。分母は最後のページの番号で、白紙も数えます |
| `none` | 出さない |

: ページ番号の出し方

`page-count` でページの数え方を選びます。

```yaml
pubpdf:
  page-count: continuous
```

| 値 | 数え方 | 表紙、履歴、目次、第1章の番号の例 |
|---|---|---|
| `continuous` | 表紙を1ページ目として、最後まで通して数える | 1(非表示)、2、3、4 |
| `roman` | 本文の前をローマ数字で数え、本文を1から数え直す | i(非表示)、ii、iii、1 |

: ページの数え方

自動で入る白紙も1ページとして数えます。番号は出しません。`roman` と `total` を組み合わせると、本文の前には分母を出さず、分母は本文のページ数になります。表紙のすぐ次から本文が始まる奇数ページ始まりの文書では、`roman` でも通して数えます。

## ヘッダとフッタの文字 {#sec-running}

ヘッダとフッタの左、中央、右に文字を入れられます。

```yaml
pubpdf:
  header-left: '{title}'
  header-right: '{chapter}'
  footer-left: '{organization}'
  footer-center: '{page} / {total}'
```

`{名前}` は、次の値に置き換わります。`{` で始まる値は YAML の決まりで引用符が必要です。

| 書き方 | 置き換わる値 |
|---|---|
| `{title}`、`{subtitle}`、`{author}`、`{organization}`、`{date}`、`{version}`、`{doc-number}` | frontmatter の値 |
| `{chapter}` | そのページの章の名前。番号があれば番号も出します |
| `{page}` | ページ番号。`page-count` の数え方に従います |
| `{total}` | 最後のページの番号 |

: ヘッダとフッタに書ける値

- `{title}` などの Markdown として読む値は、記号を除いて出します。
- `{page}` をどこかに書くと、`page-number` による自動のページ番号は出しません。`{total}` だけなら自動の番号も出します。
- `header-left` を指定しないときは、これまでどおり章の名前を出します。章の名前を消すときは `header-left: ""` と書きます。
- 文字は Markdown として読まず、書いたとおりに出します。
- 表紙と、自動で入る白紙には出しません。
- `header-rule: true` でヘッダの下に、`footer-rule: true` でフッタの上に罫線を引きます。表紙には引きません。
- 機密表示やページ番号と同じ場所を指定すると、少し空けて並べます。
- 使えない `{名前}` は、警告を出して文字のまま出します。値のない `{version}` などは、警告を出して空にします。

## 見出しと図表の番号

`numbering` で見出しの番号の形を選びます。

```yaml
pubpdf:
  numbering: chapter
```

| 値 | 章 | 節 |
|---|---|---|
| `none` | 番号なし | 番号なし |
| `chapter` | 第1章 | 1.1 |
| `decimal` | 1 | 1.1 |

: 見出しの番号の形

`heading-format` で、階層ごとに番号の形を指定できます。設計書でよく使う「1. → 1.1 → (1) → ①」の形は、次のように書きます。`numbering` が `chapter` か `decimal` のときだけ使います。

```yaml
pubpdf:
  numbering: decimal
  heading-format: ["1.", "1.1", "(1)", "①"]
```

| 形の例 | 出る番号 |
|---|---|
| `1.` | 1. 2. 3. |
| `第1章` | 第1章 第2章 |
| `1.1`、`1-1` | 2.1 2.2 のように、上の階層の番号を含む |
| `(1)`、`①`、`(ア)`、`a)` | 自分の階層の番号だけ |

: 番号の形の書き方

- 形の中の数える記号(`1`、`a`、`A`、`i`、`I`、`ア`、`あ`、`一`、`①` など)の数だけ、下の階層から番号を使います。`1.1` なら上の階層と自分、`(1)` なら自分だけです。
- 指定より深い階層は、最後の形を使います。
- 付録の章は「付録 A」です。上の階層の番号を含む形では、章の番号を A の形にします(`1.1` なら A.1)。
- 形は 6 個まで、1 つ 20 文字までです。数える記号のない形は使えません。

`figure-numbering` で、図、表、コード、定理、式の番号の振り方を選びます。

| 値 | 例 | 振り方 |
|---|---|---|
| `chapter` | 図 1-1、表 2-1、(1-1) | 章ごとに振り直す |
| `section` | 図 1.1-1、表 2.3-1、(1.1-1) | 節ごとに振り直す。章の最初の節より前は「図 1-1」 |
| `continuous` | 図 1、表 2、(3) | 文書全体を通して数える |

: 図表の番号の振り方

既定は、見出しの番号があれば `chapter`、なければ `continuous` です。見出しの番号がないときに `chapter` か `section` を指定すると、警告を出して通し番号にします。

序文や `{.unnumbered}` を付けた章は、番号のある章の外として扱います。その中の節にも番号を付けません。図と式には章の番号を付けず、番号を振り直さずに続けて数えます。

本書は `chapter` で組んでいます。

## 式の番号

`equation-numbering` で番号を入れる式を選びます。

| 値 | 番号を入れる式 |
|---|---|
| `all` | すべての独立した式。`\notag` と `\nonumber` を書いた式を除きます |
| `labeled` | `{#eq-名前}` を付けた式だけ |

: 番号を入れる式

書き方は[原稿の書き方](06-writing.md#sec-math)を参照してください。

## コードの行番号

`code-line-numbers: true` にすると、すべてのコードに行番号を付けます。コードごとに指定する方法は、[原稿の書き方](06-writing.md#sec-code)を参照してください。

## 章の前の改ページ

`chapter-break: false` にすると、章の前で改ページしません。短い文書で間延びするときに使います。ただし、奇数ページ始まりのときは、章は必ず新しいページから始まります。

## 色と体裁

### テーマの色

`accent-color` で、題、見出し、章と表紙の線、リンクと参照、表の見出しの色を変えます。`#` は YAML ではコメントの印なので、引用符で囲みます。

```yaml
pubpdf:
  accent-color: "#0a7d5a"
```

### 表の体裁

`table-style` で、本文の表の罫線を選びます。バージョン履歴の表にも効きます。表紙の表は変わりません。

| 値 | 体裁 |
|---|---|
| `grid` | 格子。見出しの行を塗ります |
| `lines` | 横線だけ。見出しの行を塗ります |
| `booktabs` | 表の上下と見出しの下の線だけ。論文でよく使う形です |
| `striped` | 線なしで、行ごとに色を分けます |

: 表の体裁

### コードの配色

`code-theme` で、コードブロックの背景と色分けを選びます。

| 値 | 配色 |
|---|---|
| `default` | 既定 |
| `github` | GitHub |
| `atom-one` | Atom One |
| `solarized` | Solarized。背景が淡い黄色 |
| `nord` | Nord。背景が暗い |
| `dracula` | Dracula。背景が暗い |
| `monochrome` | 白黒 |

: コードの配色

背景が暗い配色では、文中のコード(`` `code` ``)は色分けせず、本文と同じ色で出します。

## フォント {#sec-fonts}

本文、見出し、コード、数式のフォントを別々に指定できます。

```yaml
pubpdf:
  font: BIZ UDPGothic
  font-heading: Noto Sans JP
  font-code: Consolas
  font-math: Cambria Math
```

本文のフォントを指定しないときは、インストールされているフォントから、次の順に最初に見つかったものを使います。

1. Noto Sans JP
2. Noto Sans CJK JP
3. BIZ UDPGothic
4. Yu Gothic
5. Meiryo

欧文だけのフォントを指定しても、日本語の文字はこの順に見つかったフォントで補います。リストで書くと、前のフォントにない文字を次のフォントで補います。

```yaml
pubpdf:
  font:
    - Times New Roman
    - BIZ UDPGothic
```

指定したフォントが見つからないときは、警告を出して別のフォントで組みます。

### フォントの読み込み

OS に入れていないフォントも使えます。`font-paths` にフォントのあるフォルダかフォントファイルを指定し、`font` などでフォント名を指定します。相対パスは原稿のフォルダが基準です。読み込めるのは ttf、otf、ttc、otc です。

```yaml
pubpdf:
  font-paths:
    - fonts-custom
    - assets/MyFont-Regular.otf
  font: My Font
```

原稿と同じフォルダの `fonts/` は、指定しなくても読み込みます。VS Code では設定パネルのフォント名の欄に、読み込めるフォントが候補として出ます。ファイルを指定したときは、同じフォルダの他のフォントも候補に出ますが、使えるのは指定したファイルだけです。

### 数式のフォント

`font-math` には数式用のフォントだけが使えます。数式用でないフォントを指定すると、大きな括弧や総和の記号が崩れます。Windows の Cambria Math のほか、Fira Math、STIX Two Math、Libertinus Math などを `font-paths` で読み込めば使えます。

## PDF の規格 {#sec-standard}

`pdf-standard` で、長期保存やアクセシビリティの規格に沿った PDF を作ります。

```yaml
pubpdf:
  pdf-standard: a-2b
```

| 値 | 規格 | 用途 |
|---|---|---|
| `a-2b` | PDF/A-2b | 長期保存 |
| `a-3b` | PDF/A-3b | 長期保存 |
| `ua-1` | PDF/UA-1 | アクセシビリティ(読み上げなど) |
| `a-2b,ua-1` | PDF/A-2b と PDF/UA-1 | 両方 |

: PDF の規格

- 組むときに Typst が規格の条件を確かめ、合わない内容があれば組まずに止めます。
- PDF/A と PDF/UA には、PDF の画像を使えません。PNG か SVG にしてください。
- PDF/UA では見出しの段を飛ばせません(`#` の次に `###` など)。`skipped from heading level` や `the first heading must be of level 1` と出たら、見出しの段を直してください。
- 外部の検証ツールでの確認が必要なときは、`quarto install verapdf` で veraPDF を入れます。入っていれば、Quarto が組んだ後に検証します。Pubpdf の開発では veraPDF での確認はしていません。

PDF/UA では、画像と式に代替テキスト(読み上げ用の文)が必要です。次の順に自動で入れます。

| 対象 | 代替テキスト |
|---|---|
| 画像 | `fig-alt` の値、`![説明](画像)` の説明の順。どちらもなければ「図」とし、警告を出します |
| Mermaid の図 | `%%\| label: fig-名前` と `%%\| fig-cap:` で書いた題。なければ「図」とし、警告を出します |
| 式 | 式の TeX の文字。文献の題の中の式は「数式」 |
| ロゴ | 組織名。なければ「ロゴ」 |

: PDF/UA の代替テキスト

`{=typst}` で直接書いた画像は「図」、式は「数式」になります。説明を付けるときは、式の前の行に `#set math.equation(alt: "説明")` と書きます。
