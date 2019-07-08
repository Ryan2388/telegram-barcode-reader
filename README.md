# Telegram Barcode reader

#### Usage:
First of all, you need to set `DB_URI` environment variable:
`export DB_URI=sqlite:////tmptest`
Or add argument to command:
`pytohn -m bot .. --db-uri sqlite:////tmp/test.db`

SQLAlchemy supports PostgreSQL, MySQL, SQLite, Oracle, etc.
You can read [here](https://docs.sqlalchemy.org/en/13/core/engines.html) about 
supported db drivers

Then, you need to set `TOKEN`:
`export TOKEN=123456:AAaaaaaaaaaaaaaaaaaaaaaaaaaa` 

You can get your bot token [here](https://t.me/BotFather).

##### Database setup:
`python -m bot setup-database`

Also, you can drop all data before proceed database setup, if you pass `--rm` 
flag.

##### Starting bot with webhook server
`python -m bot start-webhook --port 8080`

I prefer to use `nginx` as reverse proxy for mine telegram bots. 

##### Starting bot with polling worker
`pythom -m bot start-polling`
