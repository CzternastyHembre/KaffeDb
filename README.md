# KaffeDb

A python/sqlite application used to describe Coffee

### Vscode

Download the [SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) extention in vscode and open the command pallet and run "SQLite: Open Database" og choose the file Coffee.db to open the Coffee.db database

```sql

PRAGMA FOREIGN_keys = ON;

DROP TABLE IF EXISTS Farm;
CREATE TABLE Farm (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Region_FK TEXT NOT NULL,
);

INSERT INTO Farm VALUES (0, "Stavanger farm");


SELECT * FROM Farm;

```
