# 埼玉県 新型コロナウイルス感染症対策サイト

![](https://github.com/codefortoda/covid19-saitama/workflows/production%20deploy/badge.svg)

[![埼玉県 新型コロナウイルス感染症対策サイト](https://saitama.stopcovid19.jp/ogp.png)](https://saitama.stopcovid19.jp/)

### 日本語 | [English](./README_EN.md)

## 貢献の仕方
Issues にあるいろいろな修正にご協力いただけると嬉しいです。

詳しくは[貢献の仕方](./.github/CONTRIBUTING.md)を御覧ください。


## 行動原則
詳しくは[サイト構築にあたっての行動原則](./.github/CODE_OF_CONDUCT.md)を御覧ください。

## ライセンス
本ソフトウェアは、[MITライセンス](./LICENSE.txt)の元提供されています。

## 元のサイト

### 【東京都】新型コロナウイルス感染症対策サイト
[サイトへのリンク](https://stopcovid19.metro.tokyo.lg.jp/)

[GitHubへのリンク](https://github.com/tokyo-metropolitan-gov/covid19)

## 元のサイトから派生したもの

[Link先](https://github.com/tokyo-metropolitan-gov/covid19/blob/development/FORKED_SITES.md)を御覧ください。

## 開発者向け情報

### 環境構築の手順

- 必要となるNode.jsのバージョン: 10.19.0以上

**yarn を使う場合**
``` bash
# install dependencies
$ yarn install

# serve with hot reload at localhost:3000
$ yarn dev
```

**docker compose を使う場合**
```bash
# serve with hot reload at localhost:3000
$ docker-compose up --build
```

### `Cannot find module ****` と怒られた時

**yarn を使う場合**
```
$ yarn install
```

**docker compose を使う場合**
```bash
$ docker-compose run --rm app yarn install
```

### ステージング・本番環境への反映

`master` ブランチがアップデートされると、自動的に `production` ブランチにHTML類がbuildされます。そして、本番サイト https://saitama.stopcovid19.jp/ が更新されます。

`development` ブランチがアップデートされると、自動的に `dev-pages` ブランチにHTML類がbuildされます。そして、開発用サイト https://dev-stopcovid19.e-toda.jp/ が更新されます。


