# PSE Seminar Email

- PSE研究室向けのアクションです。
- ゼミ用のレポートをメールに添付して送信します。
- デフォルト設定のまま利用すると[KUMOI](http://www.iimc.kyoto-u.ac.jp/ja/services/mail/kumoi/use/use.html)のSMTPサーバーの設定が適用されます。

## Inputs

| id | Description | Required | Default |
| :-: | :-- | :-: | :-: |
| `smtp_server` | SMTPサーバーのホスト名 | ✅ | `smtp.office365.com` |
| `smtp_port` | SMTPサーバーのポート | ✅ | 587 |
| `ecs_id` | ECS ID | ✅ | - |
| `password` | ECS IDに紐づくパスワード | ✅ | - |
| `to` | 送信先メールアドレス | ✅ | - |
| `from` | 送信元メールアドレス | ✅ | - |
| `subject` | Eメールの件名 | ✅ | See [Default value of `subject`](#default-value-of-subject) |
| `body` | Eメールの本文 | ✅ | See [Default value of `body`](#default-value-of-body) |
| `subtype` | MIMEのサブタイプ (html or plain) | ✅ | html |
| `date_format` | Eメール件名・本文に表示する日付のフォーマット <br> cf. [strftime() と strptime() の書式コード](https://docs.python.org/ja/3/library/datetime.html#strftime-and-strptime-format-codes) | ✅ | `%b %d, %Y` |
| `family_name` | 性。署名・PDFファイルのプレフィックスに使用。 | ✅ | - |
| `given_name` | 名。署名に使用。 | ✅ | - |
| `pdf` | 添付PDFファイルのパス | ✅ | - |
| `date` | ゼミの日付 | ✅ | - |

### Default value of `subject`

cf. [Placeholder](#placeholder)

``` text
Document for the seminar to be held on {date}
```

### Default value of `body`

cf. [Placeholder](#placeholder)

```html
<p>
  Dear all, <br><br>
  Please find attached document to be used in seminar to be held on {date}. <br><br>
  Thank you, <br>
  {name}
<p>
```

## Placeholder

Eメールの件名および本文に**ゼミの日付**と**名前**を埋め込むことができます。
Pythonのformat文字列を利用して埋め込んでいるため、 `subject` / `body` の例に示すように、
`{date}` および `{name}` をプレースホルダーとして指定してください。

```html
Name: {name}, Date: {date}
```

## Usage

```yaml
uses: tarao1006/pse-seminar-email@main
with:
  # Use secrets if credential information
  ecs_id: ${{ secrets.ECS_ID }}
  password: ${{ secrets.PASSWORD }}
  to: ${{ secrets.TO }}
  from: ${{ secrets.FROM }}
  family_name: ${{ secrets.FAMILY_NAME }}
  given_name: ${{ secrets.GIVEN_NAME }}
  # Define dynamically in practice
  pdf: distribution/seminar/20210101/report.pdf
  date: '20210101'
```

## License

[MIT License](LICENSE)
