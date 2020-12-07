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

### How does an SQLi attack work ?

SQLi is carried out through abusing a PHP GET parameter (for example __?username=__, or __?id=__) in the URL of a vulnerable web page. These are usually located in the search fields and login page.

![exemple-php](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day05/exemple-php.png)

After a variable `username` was inputted in the code, PHP automatically uses SQL to select all users with the provided username. __This__ can be abused by an attacker.

Let's say a malicious user provides a quotation mark __( ` )__ as the username input. The SQL code will looke like this :

```
SELECT * FROM users WHERE username = ```
```

The mark creates a third one and generates an error since the username should only be provided with two. This error is what we need to exploit the database.

Most commonly, we use this error to bypass the login authentification or the password.

## SQLMap - best tool for SQLi
*Can be found on BurpSuite.*

|Command||
|-------||
|-url|Provide URL for the attack|
|-dbms|Tell SQLMap the type of database that is running|
|-dump|Dump the data within the database that the application uses|
|--dump-all|Dump the ENTIRE database|
|-batch|SQLMap will run automatically and won't ask for user input|

### SQLMap in BurpSuite

We need the __ProxyFoxy__ again for this.

We go to santa's website `http://$ip:8000/santapanel` to discover a login page, that we bypass.

![santa-panel](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day05/santa-panel.png)

We use the proxy to intercept the query, then we save it to `/root/panel-request` and finally send it to the __repeater__. We can now set off the interception, we won't need it anymore.

![proxy-repeater](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day05/proxy-repeater.png)

![sqlmap](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day05/sqlmap.png)

*Note: `--tamper=space2comment` bypasses the firewall, it is given in the exercise.*

And we have what we're looking for ...


![sql-results1](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day05/sql-results.png)

![sql-results2](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day05/sql-results.png)




