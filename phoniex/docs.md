[TOC]

# Phoenix安装

phoenix安装分如下三步。

## 1.1 下载合适版本的Phoenix

> phoenix与HBase版本对应关系如下。

```
graph LR
Phoenix2.x-->HBase0.94.x
Phoenix3.x-->HBase0.94.x
Phoenix4.x-->HBase0.98.1+
```
 

我们目前使用的HBase版本为 0.98,因此，下载[Phoenix4.9](http://mirrors.cnnic.cn/apache/phoenix/apache-phoenix-4.9.0-HBase-0.98/bin/apache-phoenix-4.9.0-HBase-0.98-bin.tar.gz)。


## 1.2 上传到主节点
上传到master节点，解压缩。解压后，将phoenix目录下的 __core.jar__ 拷贝至各个hadoop集群各个节点 __Hbase__ 的 __lib__ 目录。
```bash
#下载的压缩包位于/root目录下
cd /root
tar –zxvf phoenix.tar.gz
```

## 1.3 重启HBase
重启HBase后，进入master节点Phoenix目录的bin目录下，执行如下命令进入CLI。
```bash
./sqlline.py master:2181
#查看phoenix表
!tables
```


# 2. Phoenix使用

## 2.1. 在phoenix中创建视图

关联HBase d_developer表。
```sql
CREATE VIEW "d_developer" (code VARCHAR PRIMARY KEY, "info"."name" VARCHAR, "info"."unique_code" VARCHAR, "info"."registration_no" VARCHAR, "info"."active_state" VARCHAR, "info"."company_type" VARCHAR, "info"."found_date" VARCHAR, "info"."legal_person" VARCHAR, "info"."capital" VARCHAR, "info"."operation" VARCHAR, "info"."authority" VARCHAR, "info"."issue_date" VARCHAR, "info"."address" VARCHAR, "info"."bussiness_scope" VARCHAR, "info"."url" VARCHAR, "info"."phone" VARCHAR, "info"."mail" VARCHAR, "info"."province" VARCHAR, "info"."city" VARCHAR, "info"."qu" VARCHAR, "info"."related_code" VARCHAR, "info"."is_crawled" VARCHAR);
```

```sh
cd /root/apache-phoenix-4.9.0-HBase-0.98-bin/bin/
./sqlline.py master:2181
0: jdbc:phoenix:master:2181> select * from "d_developer" limit 10;
```

## 2.2. 在Phoenix中创建表
`TODO`

## 2.3. 使用Phoenix查询数据



##2.4. 在Python中使用Phoenix
使用phoenixdb库在Python中调用Phoenix，详情参考(phoenixdb文档)[http://python-phoenixdb.readthedocs.io/en/latest/]。

> STEP.1 开启query server
1在master节点，启用Phoenix Query Server。
```bash
cd /root/apache-phoenix-4.9.0-HBase-0.98-bin/bin
python queryserver.py start
# queryserver.py的日志位于/tmp/phoenix/root-queryserver.log
# 从日志中可知，queryserver服务端口位于：8765
```

> STEP.2 编写python脚本
```python
# !/usr/bin/env python
#coding=utf-8

import phoenixdb

database_url = 'http://localhost:8765/'
conn = phoenixdb.connect(database_url, autocommit=True)

cursor = conn.cursor()
cursor.execute('select "name","city" from "d_developer" limit 10')
data = cursor.fetchall()
for name, city in data:
	    print name, city

```

# 4. FAQ
> 1.已经有了HBase表，如何映射到Phoenix中？

有 __create view__ 和 __create table__ 两种方式。

> 2. 使用create table映射HBase表之后多出一列 ___0__

来自[stackoverflow](http://stackoverflow.com/questions/34507470/why-phoenix-always-add-a-extra-column-named-0-to-hbase-when-i-execute-upsert)的解释。

> 3 关于大小写敏感

Phoenix对于表名是大小写敏感的，也就是说`my_table`和`MY_TABLE`是在phoenix中指的不是同一张表。
默认情况下，所有的小写字母都会转换成大写字母。如果表名为小写形式，需要使用双引号（注意是双引号，单引号同样会报错）包裹，否则会出错。

例如，如果表名为h_loupan_info选择10条记录，下列的写法是错误的。

```sql
SELECT * FROM h_loupan_info LIMIT 10;
```
因为此时Phoenix默认会将表名转为大写形式，即H_LOUPAN_INFO，将表名使用双引号包裹。
```sql
SELECT * FROM "h_loupan_info" LIMIT 10;
```

更多关于大小写的示例

错误的写法
```sql
DROP VIEW test_view;
```
上述代码有一处错误，`test_view`需要用双引号包裹。

正确的写法
```sql
DROP VIEW "test_view";
```




# 5. Phoenix SQL语法参考

(官方语法参考)[http://phoenix.apache.org/language/index.html]

`Commands`

命令			|	说明
---				|	---
SELECT			|查询		
UPSERT VALUES	|插入更新
UPSERT SELECT	|插入更新
DELETE			|删除
CREATE TABLE	|创建表
DROP TABLE		|删除表
CREATE FUNCTION	|创建函数
DROP FUNCTION	|删除函数
CREATE VIEW		|创建视图
DROP VIEW		|删除视图
CREATE SEQUENCE	|
DROP SEQUENCE	|
ALTER			|修改
CREATE INDEX	|创建索引
DROP INDEX		|删除索引
ALTER INDEX		|修改索引
EXPLAIN			|
UPDATE STATISTICS|
CREATE SCHEMA	|
USE				|
DROP SCHEMA		|
```

`Other Grammar`

命令		|		说明
---			|		---
Constraint		|   
Options			|
Hint			|
Scan Hint		|
Cache Hint		|
Index Hint		|
Small Hint		|
Seek To Column Hint	|
Join Hint		|
Serial Hint		|
Column Def		|
Table Ref		|
Sequence Ref	|
Column Ref		|
Select Expression	|
Select Statement	|
Split Point			|
Table Spec			|
Aliased Table Ref	|
Join Type			|
Func Argument		|
Class Name			|
Jar Path			|
Order				|
Expression			|
And Condition		|
Boolean Condition	|
Condition			|
RHS Operand			|
Operand				|
Summand				|
Factor				|
Term				|
Array Constructor	|
Sequence			|
Cast				|
Row Value Constructor	|
Bind Parameter			|
Value					|
Case					|
Case When				|
Name					|
Quoted Name				|
Alias					|
Null					|
Data Type				|
SQL Data Type			|
HBase Data Type			|
String					|
Boolean					|
Numeric					|
Int						|
Long					|
Decimal					|
Number					|
Comments				|










