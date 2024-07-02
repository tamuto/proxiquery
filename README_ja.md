# ProxiQuery

ProxiQueryはベクトルDBの構築と検索を行うためのプラットフォームです。
いわゆるRAGを構築するためのツールです。

## 実行方法

### Docker環境

Docker環境での実行方法は以下の通りです。

```bash
docker run -d -p 8000:8000 -v $PWD/proxiquery:/proxiquery --name proxiquery tamuto/proxiquery
```
