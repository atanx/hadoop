		all_visits[visit_key]["channel_name"] = parts[17]
[TOC]
phoenix安装分如下三步。

### 1.1 下载合适版本的Phoenix

> phoenix与HBase版本对应关系如下。

```
graph LR
Phoenix2.x-->HBase0.94.x
Phoenix3.x-->HBase0.94.x
Phoenix4.x-->HBase0.98.1+
```
 

我们目前使用的HBase版本为 0.98,因此，下载[Phoenix4.9](http://mirrors.cnnic.cn/apache/phoenix/apache-phoenix-4.9.0-HBase-0.98/bin/apache-phoenix-4.9.0-HBase-0.98-bin.tar.gz)。


### 1.2 上传到主节点
上传到master节点，解压缩。解压后，将phoenix目录下的 __core.jar__ 拷贝至各个hadoop集群各个节点 __Hbase__ 的 __lib__ 目录。
```bash
#下载的压缩包位于/root目录下
cd /root
tar –zxvf phoenix.tar.gz
```

### 1.3 重启HBase
重启HBase后，进入master节点Phoenix目录的bin目录下，执行如下命令进入CLI。
```bash
./sqlline.py master:2181
#查看phoenix表
!tables
```


## 2. Phoenix使用
### 2.1 快速入门
> 已经有了HBase表，如何映射到Phoenix中？

有 __create view__ 和 __create table__ 两种方式。

## 3. FAQ
### 3.1 映射HBase表之后多出一列 ___0__

来自[stackoverflow](http://stackoverflow.com/questions/34507470/why-phoenix-always-add-a-extra-column-named-0-to-hbase-when-i-execute-upsert)的解释。

### 3.2 关于大小写。

Phoenix对于表名是大小写敏感的，SQL关键字貌似大小写不敏感。例如，如果表名为h_loupan_info选择10条记录，下列的写法是错误的。
```sql
SELECT * FROM h_loupan_info LIMIT 10;
```
因为此时Phoenix默认会将表名认为是H_LOUPAN_INFO,正确的写法是用 双引号 __"__ 将含有小写字母的表名引起来。
```sql
SELECT * FROM "h_loupan_info"
```math
E = mc^2
```
 LIMIT 10;
```
更多关于大小写的示例

错误的写法
```sql
drop view test_view;
```
上述代码有一处错误，`test_view`需要用双引号包裹。

正确的写法
```sql
DROP VIEW "test_view";
```

# 实际应用
```sh
cd /root/apache-phoenix-4.9.0-HBase-0.98-bin/bin/
./sqlline.py master:2181
0: jdbc:phoenix:master:2181> select * from "d_developer" limit 10;
```
















