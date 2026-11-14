# VS Code での操作

## コマンド

エディタ右上のボタン、エクスプローラーの右クリック、コマンドパレットから実行します。

| コマンド | 内容 | 場所 |
|---|---|---|
| `Pubpdf: PDF を作成` | PDF を作ります | ボタン、右クリック、コマンドパレット |
| `Pubpdf: PDF をプレビュー` | VS Code の中で PDF を表示します。原稿の md が PDF より新しければ作り直します | ボタン、右クリック、コマンドパレット |
| `Pubpdf: 設定パネルを開く` | 設定パネルを開きます | ボタン、コマンドパレット |
| `Pubpdf: frontmatter の雛形を挿入` | 原稿の先頭に frontmatter を入れます | コマンドパレット |
| `Pubpdf: 環境を確認` | Quarto、フォント、ブラウザの状態を一覧で示します | コマンドパレット |
| `Pubpdf: ライブプレビューを開始/停止` | 編集中の内容を、保存せずに組み直して表示し続けます。表示は作る PDF と同じです | タブの右上の `...`、コマンドパレット |
| `Pubpdf: 文章の誤りをまとめて直す` | 文章の点検で見つかった誤りのうち、自動で直せるものを直します | コマンドパレット |
| `Pubpdf: 表の見やすい表示をオン/オフ(試験的)` | 編集中の表の表示を切り替えます | コマンドパレット |

: 拡張機能のコマンド

## PDF を作る

- 実行中は通知に進捗を表示します。通知の「キャンセル」で止められます。
- 未保存の変更は、保存してから組みます。
- 親の md が同じワークスペースのフォルダにあれば、章の md を開いた状態で実行しても本全体を組みます。本が複数あれば、選択肢を示します。
- 実行中にもう一度実行すると、前の処理を止めて最新の内容で組み直します。
- 設定 `pubpdf.renderOnSave` をオンにすると、保存したときに PDF を作り直します。対象は `pubpdf:` のある原稿と合本の章です。
- PDF を他のアプリで開いていて上書きできないときは、原因を知らせます。
- ワークスペースのフォルダの直下に `.git` があるときは、最初に PDF ができた後に、`.pubpdf/` を `.gitignore` に追加するかを尋ねます。`pubpdf.renderOnSave` で作ったときと、`pubpdf.buildDirectory` が `global` のときは尋ねません。
- 信頼していないワークスペース(制限モード)では、拡張機能は動きません。
- Mermaid の図は、前に描いた図を再利用します(設定 `pubpdf.diagramCache`、既定はオン)。図の中身か Quarto の版が変わったときだけ描き直すので、2 回目からは速く組めます。再利用した図は、描き直した図と同じに組み上がります。図は中間フォルダの `cache` に保存し、使わなくなった古いものから消します。

## 設定パネル

Markdown のタブの右上にある歯車のボタンか、コマンドパレットの `Pubpdf: 設定パネルを開く` で開きます。ボタンが見当たらないときは、タブの右上の `...` の中を確認してください。

@fig-panel のパネルで、表紙、目次、図と表の一覧、参考文献、機密表示の文字と位置、ページ番号の位置と数え方、用紙の種類と向き、余白、章の前の改ページ、奇数ページ始まり、綴じ代、見出しと図表と式の番号、コードの行番号、文字の大きさ、行間、字下げ、フォントを変更できます。バージョン履歴と付録はパネルにはないので、frontmatter に書きます。文献のファイルは文書ごとの設定なので、パネルの「この文書」でだけ指定できます。

段組み、ヘッダとフッタの文字、透かし、テーマの色、表の体裁、コードの配色、PDF の規格、組織名、キーワード、主題も変更できます。ロゴと文献のファイルは原稿のフォルダの中を指すので、保存先に「この文書」を選んだときだけ変更できます。

![設定パネル。左の原稿の frontmatter と連動します](img/vscode-panel.png){#fig-panel width=100%}

パネルの上で保存先を選びます。

| 保存先 | 書き込む場所 | 効く範囲 |
|---|---|---|
| この文書 | 開いている md の frontmatter | その文書だけ |
| ワークスペースの既定 | ワークスペースの `settings.json` | ワークスペースの文書で、frontmatter に書いていない項目 |

: 設定パネルの保存先

- 「既定」を選ぶと、その項目を frontmatter から消します。括弧の中に、そのときに使われる値を示します。
- frontmatter へ書き戻すときも、コメント、キーの順序、値、本文は変えません。ただし frontmatter 全体を書き直すので、値の後のコメントの前の空白、折り返した文字列の改行、リストの字下げは揃うことがあります。
- 変更は未保存の編集として入るので、取り消せます。PDF を作るときに保存します。
- 章の md を開いているときは、親の md の設定を変更します。
- フォント名の欄には、読み込めるフォントが候補として出ます。

パネルの最後の「編集中の表示(VS Code の設定)」では、表の見やすい表示、列を揃えてたたむ表示、たたむセルの長さ、行の終わりの Enter で行を足すか、ライブプレビューで編集中の箇所を追うかと待ち時間を変更できます。この欄は文書には書かず、VS Code の設定に保存します。保存先の選択によりません(ワークスペースの `settings.json` に指定があればそこを、なければユーザーの設定を書き換えます)。

## プレビュー

@fig-preview のように、VS Code の中で PDF を確認できます。PDF を作り直すと、表示している位置を保ったまま更新します。拡大と縮小、幅に合わせる表示ができます。画像や VS Code の設定を変えただけでは、プレビューのコマンドは PDF を作り直しません。`Pubpdf: PDF を作成` を実行してください。

![プレビュー。作り直しても表示位置を保ちます](img/vscode-preview.png){#fig-preview width=100%}

## ライブプレビュー

`Pubpdf: ライブプレビューを開始/停止` を実行すると、横にライブプレビューを開き(タブの題の後ろに「(ライブ)」と付きます)、保存していない内容のまま組み直して表示し続けます。表示するのは `Pubpdf: PDF を作成` と同じ組版の PDF そのものです。用紙、余白、フォント、見出し、表、図、番号、表紙、目次の見た目は、作る PDF と変わりません。

- 編集を止めて少したったら(既定は 1 秒。設定 `pubpdf.liveDelay`)組み直します。組み始めてすぐに編集したときは組み直しをやり直し、それより後の編集は、組み終えてから続けて組みます。書き続けていても、表示は少しずつ新しくなります。
- PDF の見た目に関わる VS Code の設定(設定パネルの「ワークスペースの既定」で変えたものを含みます)を変えたときと、画像、文献のファイル、ロゴ、`include` で読み込むコードのファイル、開いていない章の md を変えたときも組み直します。
- 組んだ PDF は中間フォルダの `live` に置きます。原稿の PDF は上書きしません。原稿の PDF は、これまでどおり `Pubpdf: PDF を作成` で作ります。
- ライブプレビュー中の文書は、保存しても(`pubpdf.renderOnSave` がオンでも)組みません。
- もう一度実行するか、ステータスバーの「Pubpdf ライブ」を選ぶか、プレビューを閉じると止まります。組んでいる間は、ステータスバーの印が回ります。
- 組み直しには、ふつうに PDF を作るのと同じ時間がかかります(数秒から十数秒)。変わったところだけを組み直すことはできません。ページの割り付け、番号、目次、参照は文書の全体で決まるためです。Mermaid の図は前に描いたものを再利用するので、図の多い文書でも 2 回目からは速くなります。

ツールバーに、表示が原稿に追いついているかを出します。

| 表示 | 意味 |
|---|---|
| 最新 | 今の原稿と設定で組んだ PDF を表示しています |
| 未反映の編集があります | 編集を止めるのを待っています。少したつと組み直します |
| 組み直しています… | 組んでいます。表示の上端に細い帯が流れます |
| 組めませんでした | 書きかけなどで組めませんでした |
| ライブ表示を止めました | 最後に組んだ PDF を表示したままです |

: ライブプレビューの状態

組めなかったときは、ツールバーの下に理由を出し、前に組めた PDF を表示し続けます。詳しい内容は問題パネルで確認できます。原稿を直すと組み直します。

### 編集中の箇所を追う

カーソルを動かすと、編集中の箇所が見えるようにプレビューをスクロールし、その行に目印を出します。目印は、ページの左の縁の線と、行の薄い帯です。消えずにカーソルについて動きます。

- 目印が画面の中ほどにあるうちは、打つたびに揺れないようにスクロールしません。画面の外や端に近づくと、画面の上から 3 割のあたりに来るようにスクロールします。
- 組み直して PDF が入れ替わっても、表示している位置を保ちます。プレビューを読んでいる(エディタにフォーカスがない)ときは、組み直してもカーソルの位置へ引き戻さず、目印だけを動かします。
- 組んだ後に書き足した文は、まだ PDF にありません。書き足した場所(前の段落の終わりのあたり)に目印を出します。
- プレビューのページをダブルクリックすると、原稿のその箇所の行へ移ります。合本では章の md を開きます。
- 追わないようにするには、設定 `pubpdf.liveFollow` をオフにします(設定パネルの最後でも変えられます)。ダブルクリックで原稿へ移る操作は、オフでも使えます。

ライブプレビューの PDF には、段落とリストの項目の先頭の位置を添付ファイル(`pubpdf-sync.json`)として書き込み、編集中の行を探すのに使います。見た目は変わりません。`Pubpdf: PDF を作成` で作る PDF には付けません。次のときは、位置がおおよそになります。

- Mermaid の図の中の行は、図のあたりに目印を出します。図は画像なので、行ごとの位置がありません。
- `pdf-standard` に PDF/A-2b(`a-2b`)を指定した文書は、添付ファイルを付けられないので、位置を書き込みません。見出しと PDF の文字から探すので、文字が PDF にない行(図や数式の中など)は、前後の見出しから見当を付けた位置になります。
- `include` で読み込んだコードの中をダブルクリックすると、その文字が原稿にないので、近くの行に移ります。

## 文章の点検

Markdown の原稿を書いている間に文章を点検し、問題パネルに出します。電球のアイコン(クイックフィックス)から 1 か所ずつ直すか、同じ種類の誤りを文書の中でまとめて直せます。`Pubpdf: 文章の誤りをまとめて直す` は、自動で直せるものを全部直します。コード、数式、URL、リンク先、HTML のタグ、frontmatter は点検しません。

| 点検 | 設定(既定) | 内容 |
|---|---|---|
| 和文と英数字の間の空白 | `spacing`(`off`) | `no-space` は「日本語 eng 日本語」の空白を知らせて消します。`space` は和文と英字の間に空白がないところを知らせます |
| 文字の幅 | `width`(オン) | 全角の英数字(ｋ、Ａ、１)を半角に、半角のカナ(ｶﾅ)を全角にします |
| つづり | `spelling`(オン) | よくある英単語のつづりの誤り(recieve、seperate など)と、同じ語の重なり(the the)。語を足すときは VS Code の設定 `pubpdf.lint.words` か frontmatter の `words` に `{ 誤り: 正しい語 }` の形で書きます |
| 文体 | `style`(`off`) | `dearu`(である調。ビジネスや技術の文書)は「です」「ます」の文を、`desumasu`(です・ます調)は「である」「だ」や普通の形(「する。」)の文を知らせます。`consistent` は混在を知らせ、多い方にそろえます。段落の文の終わり(「。」の前)だけを見て、リスト、表、見出し、引用は見ません |
| 日本語の誤り | `grammar`(オン) | ら抜き言葉(見れる → 見られる)、い抜き言葉(してる → している)、助詞の重なり(をを)、句読点の重なり(。。) |
| ひらがなで書く語 | `notation`(オフ) | 下さい → ください、出来る → できる、致します → いたします、この様に → このように、殆ど → ほとんど など |

: 文章の点検

設定は VS Code の `pubpdf.lint.*`(`pubpdf.lint.style` など)で決め、文書ごとには frontmatter の `pubpdf.lint` に書きます。frontmatter が優先されます。`lint: false` でその文書の点検を止め、`pubpdf.lint.enabled` をオフにするとすべての文書で止めます。

```yaml
pubpdf:
  lint:
    style: dearu        # である調の文書
    spacing: no-space   # 和文と英数字の間に空白を入れない
    notation: true
```

- 文体の自動の修正は、形の決まった終わり方(「します」→「する」、「です」→「である」、「されます」→「される」など)だけです。「示します」(示す)のように見分けられないものは、知らせるだけにします。
- 英単語のつづりは、よくある誤りの一覧と照らし合わせるだけです。すべての誤りは見つけられません。

## 表の見やすい表示(試験的)

設定 `pubpdf.tableView.enabled` をオンにする(コマンド `Pubpdf: 表の見やすい表示をオン/オフ(試験的)` と、設定パネルの最後の「編集中の表示」でも切り替えられます)と、編集中のパイプ表を見やすくします。原稿の文字は変えません。

- 表の行を 1 行おきに塗り、行の終わりに ⏎ の印を付けます。長い行が折り返しても、どこまでが 1 行かが分かります。
- 見出しの行を太字にします。
- カーソルのない行は、列を揃えて表示します。原稿の空白で揃えていなくても、縦線が揃って見えます(原稿の空白は変えません)。全角の字は全角の空白で埋めるので、フォントによらず揃います。
- 長いセル(既定は半角 24 字。設定 `pubpdf.tableView.cellWidth`)は、後ろをたたんで「…」にします。たたんだセルにマウスを重ねると全部の文字を出します。
- カーソルを置いた行は、書いたとおりに出します。行を離れると揃います。
- 揃える表示とたたむ表示をやめるには `pubpdf.tableView.fold` をオフにします。VS Code の文字の飾りの仕組みで文字を見えなくしているので、VS Code の版によって崩れたときもオフにしてください。

表の行の終わりで Enter を押すと、次の行(空のセル)を足し、カーソルを最初のセルに置きます。見出しの行の終わりなら、区切りの行の次に足します。縦線を空白で揃えた表では、足す行も同じ幅にします。空の最後の行で Enter を押すと、その行を消して表を抜けます(空行を挟んで次の文を書けます)。取り消すと、改行ごと戻ります。この動きは表の見やすい表示がオフでも効きます。止めるには `pubpdf.tableView.enterNewRow` をオフにします。

## エラーと警告

- エラーと警告を問題パネルに出します。章ファイル、画像、リンク、frontmatter の誤りは、選ぶと原稿の該当行へ移動します。
- 組版中のエラーは原稿の行に対応しないので、親の md の先頭に出します。内容は出力パネルの Pubpdf で確認できます。

## 設定のキー

VS Code の設定は、frontmatter に書いていない項目の既定値になります。`font-paths` だけは例外で、frontmatter と VS Code の設定の両方を読み込みます。

| VS Code の設定 | frontmatter のキー |
|---|---|
| `pubpdf.cover` | `cover` |
| `pubpdf.toc` | `toc`(`none`、`1`、`2`、`3`) |
| `pubpdf.listOfFigures` | `list-of-figures`(`on`、`off`) |
| `pubpdf.listOfTables` | `list-of-tables`(`on`、`off`) |
| `pubpdf.citationStyle` | `citation-style` |
| `pubpdf.footnotes` | `footnotes` |
| `pubpdf.footnotesTitle` | `footnotes-title` |
| `pubpdf.confidential.text` | `confidential` |
| `pubpdf.confidential.position` | `confidential-position` |
| `pubpdf.watermark` | `watermark` |
| `pubpdf.header.left`、`pubpdf.header.center`、`pubpdf.header.right` | `header-left`、`header-center`、`header-right` |
| `pubpdf.footer.left`、`pubpdf.footer.center`、`pubpdf.footer.right` | `footer-left`、`footer-center`、`footer-right` |
| `pubpdf.pageNumber` | `page-number`(`auto` は既定に任せます) |
| `pubpdf.pageCount` | `page-count` |
| `pubpdf.paper` | `paper` |
| `pubpdf.orientation` | `orientation` |
| `pubpdf.columns` | `columns` |
| `pubpdf.margin.top`、`pubpdf.margin.bottom` | `margin.top`、`margin.bottom` |
| `pubpdf.margin.inner`、`pubpdf.margin.outer` | `margin.inner`、`margin.outer` |
| `pubpdf.numbering` | `numbering` |
| `pubpdf.figureNumbering` | `figure-numbering`(`auto` は既定に任せます) |
| `pubpdf.equationNumbering` | `equation-numbering` |
| `pubpdf.codeLineNumbers` | `code-line-numbers`(`on`、`off`) |
| `pubpdf.codeDisplay` | `code-display` |
| `pubpdf.codeFitMin` | `code-fit-min` |
| `pubpdf.codeAttach` | `code-attach` |
| `pubpdf.codeAttachNote` | `code-attach-note` |
| `pubpdf.codeAppendixTitle` | `code-appendix-title` |
| `pubpdf.codeAppendixNote` | `code-appendix-note` |
| `pubpdf.fontSize` | `font-size` |
| `pubpdf.lineSpacing` | `line-spacing` |
| `pubpdf.firstLineIndent` | `first-line-indent`(`on`、`off`) |
| `pubpdf.chapterBreak` | `chapter-break`(`on`、`off`) |
| `pubpdf.oddStart` | `book.odd-start`(`auto`、`on`、`off`) |
| `pubpdf.gutter` | `book.gutter` |
| `pubpdf.accentColor` | `accent-color` |
| `pubpdf.tableStyle` | `table-style` |
| `pubpdf.codeTheme` | `code-theme` |
| `pubpdf.inlineCodeBackground` | `inline-code-background`(`on`、`off`) |
| `pubpdf.tableFit` | `table-fit`(`on`、`off`) |
| `pubpdf.pdfStandard` | `pdf-standard` |
| `pubpdf.font.body` | `font` |
| `pubpdf.font.heading` | `font-heading` |
| `pubpdf.font.code` | `font-code` |
| `pubpdf.font.math` | `font-math` |
| `pubpdf.font.paths` | `font-paths`(相対パスはワークスペースのフォルダが基準です) |

: VS Code の設定と frontmatter の対応

次の設定は VS Code だけのものです。

| 設定 | 内容 |
|---|---|
| `pubpdf.quartoPath` | Quarto の実行ファイルのパス |
| `pubpdf.outputDirectory` | PDF の出力フォルダ。frontmatter の `output` が優先されます |
| `pubpdf.buildDirectory` | 中間ファイル(`.pubpdf`)の置き場所。`workspace`(既定)はワークスペースのフォルダの直下、`document` は原稿と同じフォルダ、`global` は拡張機能の保管場所(プロジェクトのフォルダには作りません) |
| `pubpdf.renderOnSave` | 保存時に PDF を作り直す |
| `pubpdf.liveDelay` | ライブプレビューで、編集を止めてから組み直すまでの時間(ミリ秒。既定は 1000) |
| `pubpdf.liveFollow` | ライブプレビューで、編集中の箇所が見えるようにプレビューをスクロールし、その行に目印を出す(既定はオン) |
| `pubpdf.diagramCache` | 前に描いた Mermaid の図を再利用する(既定はオン) |
| `pubpdf.lint.enabled`、`pubpdf.lint.*` | 文章の点検。frontmatter の `pubpdf.lint` が優先されます |
| `pubpdf.tableView.enabled`、`pubpdf.tableView.fold`、`pubpdf.tableView.cellWidth` | 表の見やすい表示(試験的) |
| `pubpdf.tableView.enterNewRow` | 表の行の終わりの Enter で次の行を足す(既定はオン) |

: VS Code だけの設定

ライブプレビューと表の見やすい表示の設定は、設定パネルの最後の「編集中の表示」でも変えられます。frontmatter には書けません。
