# LEMONADE
サーバーのストレステストプログラムです。

Dos攻撃は電子計算機損壊等業務妨害罪などに問われます

config.jsonのjson機能はpostでないと機能しません。

またこれは教育目的及び娯楽、プログラミングスキルの向上などのために作成されました

プロキシはHTTPのみ対応しています

dictknifeモジュールが必要です

## 実行中の画面

![top-page](https://raw.githubusercontent.com/distriful5061/LEMONADE/images/lemonade.png)

# config.jsonの使い方

"url" リクエストを行うアドレスのリストです。Listの知識があればできると思います

"useconfigurl" config.jsonのurlを使用するかどうかです。これだと複数urlを使用できます

"method" リクエストのメソッドです。普通はgetでいいですか下のpayloadと合わせて連投ツールとして使用することも可能です

"payload" リクエストのペイロードです。以上！！！

"json" リクエストのjsonパラメーターです。json受け取りを使用しているapiなどに有効です(廃止されました。LEMONADE VODKA SPECIALにて再実装予定です)

"useragents" ユーザーエージェントのパスです。

"referers" リファラーです。どこのサイトから来たのかっていうリストです。検索エンジンがおすすめ

"safemode" 想定外のステータスコードが帰ってきた場合、そのリクエストへの送信を停止します

"ignorestatuscode" 正しいステータスコードのリストです。これ以外が返され、safemodeが有効な場合はそのリクエストへの送信を停止します

"proxies" プロキシリストのパスです。プロキシーを使用したリクエストを送信する場合にご使用ください

"useproxies" プロキシを使用するかどうかです。

"thread" スレッド関係のconfigです

## thread

"nodelay" これをオンにすると他の設定をガン無視してリクエストを送信しまくります

"mindelay" randomdelayオプションが有効な場合にランダム生成したスリープミリ秒の最小値です

"maxdelay" randomdelayオプションが有効な場合にランダム生成したスリープミリ秒の最大値です

"randomdelay" スリープミリ秒をランダムにするかどうかです。Limiterが有効な場合はそちらが優先されます

"normaldelay" スリープミリ秒の値です。usenormaldelayが有効な場合このミリ秒だけスリープされます。

"usenormaldelay" 一定のスリープミリ秒を使用しスリープするかどうかです。Limiter及びrandomdelayのどちらかが有効な場合、そちらが優先されます

"maxthreads" Limiterが有効な場合、これ以上のスレッド数の作成は許可されません。

"limiter" リミッターです。色々と安全(適当)に作られています

"timeout" リクエストのタイムアウト秒数です
