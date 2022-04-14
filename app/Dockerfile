# ベースイメージ
FROM python:3.9

RUN mkdir /var/www
# workdirの指定
WORKDIR /var/www

# 依存Pythonライブラリ一覧コピー
COPY requirements.txt ./

# 依存Pythonライブラリインストール
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


#デバッグ用
# CMD ["python","./run.py"]

#本番環境用
CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
