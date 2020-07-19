
# Blog
pythonのフレームワークである、djangoを使って簡単で機能的なブログになっています。 

## 詳細
このブログでは下記の機能を備えており、デザインにはBootstrapを使用しています。
 
## 使用した環境
- Djnago: 2.1.8
- Python: 3.6.5
- Pillow: 7.0.0(ブログ内で画像を扱うため)

## 機能
 
- CRUD処理
- ブログ内検索
- 画像アップロード
- ログイン、ログアウト機能
- カテゴリ、タグ検索機能
 
## 使い方

0. あらかじめ環境構築をしてください<br>

1. このプロジェクトをクローンする<br>git clone https://github.com/katsuhikonakano/blog

2. モデルをデータベースに移行する<br>
python manage.py migrate

3. 管理者ユーザーを作成する<br>python manage.py createsuperuser<br>

4. 作動させる<br>python manage.py runserver

## 最後に
このブログを見ていただき、ありがとうございました。まだまだ未熟者なので至らない点やご指摘がございましたら優しくご教授いただけると幸いです。 

##### 作成日2020/3/4