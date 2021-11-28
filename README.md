# ping_log_parser

## 実行方法

```sh
python3 ping_log_parser/parser.py --src path/to/logfile
```

## 環境構築 (for developing)

```sh
$ python3.9 -m venv venv
$ . ./venv/bin/activate
(venv) $ pip install poetry
(venv) $ poetry install
```

## テスト

```sh
(venv) $ pytest .
```
