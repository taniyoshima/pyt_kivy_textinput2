# pyt_kivy_textinput2

<br>

## 内容 

textinputのサンプルプログラム。（複数行のTextInputの設定）

### テキスト周りの隙間を指定する

テキスト周りの隙間はpaddingによって指定します。paddingの値は、四方の隙間をそれぞれ指定する場合は[左側の隙間、上側の隙間、右側の隙間、下側の隙間]の形で指定します。その他にも水平方向と垂直方向で隙間を指定する場合は[水平方向の隙間、垂直方向の隙間]の形で指定し、四法の隙間をまとめて指定する場合は[隙間]の形で指定します。

```
        TextInput:
            text:'テキスト１：multiline\nテキスト１：multiline\nテキスト１：multiline\nテキスト１：multiline\nテキスト１：multiline'
            font_name: 'MPLUS1-Medium.ttf'
            font_size: '20pt'
            line_spacing: 10
            lines_to_scroll: 2
            padding: [20]
```

<br>

### テキストの行間を指定する

TextInputの行間は、line_spacingで指定します。(line_spacingのデフォルト値は0です)

```
        TextInput:
            text:'テキスト１：multiline\nテキスト１：multiline\nテキスト１：multiline\nテキスト１：multiline\nテキスト１：multiline'
            font_name: 'MPLUS1-Medium.ttf'
            font_size: '20pt'
            line_spacing: 10
            line_to_scroll: 2
```

### マウスホイールによるテキストのスクロール量を指定する

TextInputでのマウスホイールによるスクロール量は、lines_to_scrollにより指定します。(lines_to_scrollのデフォルト値は3です)

```
        TextInput:
            text:'テキスト１：multiline\nテキスト１：multiline\nテキスト１：multiline\nテキスト１：multiline\nテキスト１：multiline'
            font_name: 'MPLUS1-Medium.ttf'
            font_size: '20pt'
            line_spacing: 10
            lines_to_scroll: 2
```

<br>

### テキストを読み込み専用にする

TextInputを読み込み専用にするには、readonlyにTrueを指定します。

```
        TextInput:
            text:'テキスト２：multiline\nテキスト２：multiline\nテキスト２：multiline\nテキスト２：multiline\nテキスト２：multiline'
            font_name: 'MPLUS1-Medium.ttf'
            font_size: '20pt'
            readonly: True
```

<br>

## 参考にしたHP

## 履歴

2024/7/18 サンプルプログラム作成
