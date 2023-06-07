# customer-demo


Create database :

```
localhost:~ # mysql -u root -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 10
Server version: 10.6.12-MariaDB MariaDB package

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> create database db_docaposte;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> CREATE USER 'docapostedemo'@'%' IDENTIFIED BY 'd0cAp0st3_dem0!';
Query OK, 0 rows affected (0.003 sec)

MariaDB [(none)]> GRANT ALL PRIVILEGES ON db_docaposte.* TO 'docapostedemo'@'%';
Query OK, 0 rows affected (0.003 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.000 sec)
```

Create table :

```
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| db_docaposte       |
| information_schema |
+--------------------+
2 rows in set (0.000 sec)

MariaDB [(none)]> use db_docaposte;
Database changed
MariaDB [db_docaposte]> CREATE TABLE doca_test (id MEDIUMINT NOT NULL AUTO_INCREMENT, data CHAR(30) NOT NULL, PRIMARY KEY (id));
Query OK, 0 rows affected (0.019 sec)

MariaDB [db_docaposte]> show tables;
+------------------------+
| Tables_in_db_docaposte |
+------------------------+
| doca_test              |
+------------------------+
1 row in set (0.000 sec)

MariaDB [db_docaposte]> describe doca_test;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| id    | int(11) | YES  |     | NULL    |       |
| data  | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
2 rows in set (0.001 sec)
```

```
ALTER TABLE doca_test ADD id INT PRIMARY KEY AUTO_INCREMENT;
MariaDB [db_docaposte]> ALTER TABLE doca_test ADD CONSTRAINT id PRIMARY KEY (id);
Query OK, 0 rows affected, 1 warning (0.085 sec)
Records: 0  Duplicates: 0  Warnings: 1

MariaDB [db_docaposte]> describe doca_test;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| id    | int(11) | NO   | PRI | NULL    |       |
| data  | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
2 rows in set (0.001 sec)
```