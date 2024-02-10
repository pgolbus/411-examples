CREATE TABLE IF NOT EXISTS transactions2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    type INTEGER NOT NULL,
    description TEXT,
    deleted INTEGER NOT NULL DEFAULT 0
);

INSERT INTO transactions2 (date, amount, type, description)
SELECT date,
    amount,
    CASE WHEN type="deposit" THEN 1 ELSE -1 END,
    description FROM transactions;

select * from transactions2;

drop table transactions;
alter table transactions2 rename to transactions;

select * from transactions;