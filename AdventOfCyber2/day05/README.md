# Day05 - Someone stole Santa's gift list !

## About SQL and SQL injections

SQL is a language designed to communicate with databases

A SQL injection (SQLi) attack consists of the injection of a SQL query to the remote web application. A successful SQL injection exploit can read sensitive data from the database (usernames & passwords), modify database data (Add/Delete), execute administration operations on the database (such as shutdown the database), and in some cases execute commands on the operating system.

In an SQLi attack, we mainly use 4 commands

| SQL Command | Description |
|-------------|-------------|
| SELECT | Used to select data from a database.|
| FROM | Used to specify which table to select or delete data from.|
| WHERE | Used to extract only those records that fulfil a specified condition.|
| UNION | Used to combine the result-set of two or more SELECT statements.|

*Special note : in SQL, `1=1` stands for __True__*.
