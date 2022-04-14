# Iframe型マルチページ

[この記事](https://towardsdatascience.com/embed-multiple-dash-apps-in-flask-with-microsoft-authenticatio-44b734f74532)にインスパイアされた方法


1. flaskのwith app.app_context()でDashのページを登録。
1. それぞれ別Dashとして登録しているので、ロードが非常に遅い。
1. それぞれ別Dashとして登録しているのでIDかぶりが問題ない。
1. navbarでそれぞれのページはiframeとして埋め込む。