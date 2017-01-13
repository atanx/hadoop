# 1. 安装Storm
# 1.1 安装单机版Storm

Storm依赖zookeeper和python。因此需要先安装Zookeeper和Python。我们在Slave5(172.16.0.39)上安装Storm，Python已经安装过了，这里不需要再安装了。因此，只需要安装Zookeeper。

# 1.1.1 下载Zookeeper。
```
cd ~
wget http://mirrors.cnnic.cn/apache/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
tar -zxvf zookeeper-3.4.6.tar.gz
# 进入到解压后的文件夹zookeeper中
cd zookeeper-3.4.6
cd conf
cp zoo_sample.cfg zoo.cfg
```

```
# The number of milliseconds of each tick
tickTime=2000
# The number of ticks that the initial 
# synchronization phase can take
initLimit=10
# The number of ticks that can pass between 
# sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just 
# example sakes.
dataDir=/root/zookeeper-3.4.6/data
dataLogDir=/root/zookeeper-3.4.6/logs
# the port at which the clients will connect
clientPort=2181
# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60
#
# Be sure to read the maintenance section of the 
# administrator guide before turning on autopurge.
#
# http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance
#
# The number of snapshots to retain in dataDir
#autopurge.snapRetainCount=3
# Purge task interval in hours
# Set to "0" to disable auto purge feature
#autopurge.purgeInterval=1

```

运行zookeeper。
```
cd /root/zookeeper-3.4.6/bin
# 启动zookeeper
./zkServer.sh start
# 关闭zookeeper
# ./zkServer.sh stop
```

### 1.1.2 安装Storm

下载Storm
```

```

配置Storm
```

```

启动Storm
```

```

# 2. 使用Storm

测试样例。

```
#example 1: Run the ExclamationTopology in local mode (LocalCluster)
$ ssh slave5
$ cd /root/storm
$bin/storm jar examples/storm-starter/storm-starter-topologies-1.0.2.jar org.apache.storm.starter.ExclamationTopology

# Example 2: Run the RollingTopWords in remote/cluster mode,
#            under the name "production-topology"
$ storm jar examples/storm-starter/storm-starter-topologies-1.0.2.jar org.apache.storm.starter.RollingTopWords production-topology remote
```

