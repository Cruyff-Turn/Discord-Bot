# Discord-Bot
個人利用を目的に開発しているdiscordのチャットbotです。
手軽に使えることを目標に、汎用性よりも利用コストを下げる方針で開発しています。
主に以下の機能を提供します
* ボイスチャンネルの参加者をランダムに振り分ける
* リアクション機能を使って人が集まったら通知する

## 機能
### チーム分け機能
* 使い方：以下のコマンドをチャット欄に入力
    * /team
    * 自分が居るボイスチャンネルのユーザを2チームに分けます．

* オプション：
  * -h : ヘルプを表示します
  * -num 数字：チーム数を指定．指定が無い場合は2
  * -user [文字列]：チーム分けにユーザを追加(-を付けると除外)．スペース区切りで複数追加可能
      * 例) /team -num 4 -user [taro,tanaka,-mike,bob] 
     VC中のユーザにtaro, tanaka, bobを加え，mikeを除いて4チームに分ける
  * -lol :LoLのカスタムゲーム向けに振り分け
      * 5人チーム2つに分けて、余った人を「抽選漏れ」枠に入れます

### プレイヤー募集/通知機能
* 複数人でプレイするゲームに人が集まりそうか確認したいときに使用します。
* 使い方
    * テキストチャンネルのメッセージにリアクションをすると、同じリアクションが一定人数集まるとその旨を通知します
    * メッセージ投稿者のリアクションはカウントされません
* 現在はロケットリーグにのみ対応し、、リアクション「:rl:」が6集まったときに通知します。
