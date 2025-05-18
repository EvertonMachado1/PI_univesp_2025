#!/bin/bash

DB="db.sqlite3"

# Pega a lista das tabelas
tables=$(sqlite3 $DB "SELECT name FROM sqlite_master WHERE type='table';")

for table in $tables; do
  echo "Exportando tabela $table..."
  sqlite3 -header -csv $DB "SELECT * FROM $table;" > "${table}.csv"
done

echo "Exportação concluída!"
