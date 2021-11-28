# ping_log_parser

## 実行方法

```sh
python3 -m ping_log_parser --src path/to/logfile --retry 3
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
