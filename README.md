# druid-superset

#Prerequisites
You will need:

 - Java 8 or higher
 - Linux, Mac OS X, or other Unix-like OS (Windows is not supported)
 - 8G of RAM
 - 2 vCPUs

#Druid
Go to druid-0.12.2 folder 
 - Run zookeeper
 ```sh
 ./zookeeper-3.4.10/bin/zkServer.sh start
 ```
 - Start up Druid services
 ```sh 
 bin/init
 java `cat examples/conf/druid/coordinator/jvm.config | xargs` -cp "examples/conf/druid/_common:examples/conf/druid/_common/hadoop-xml:examples/conf/druid/coordinator:lib/*" io.druid.cli.Main server coordinator

 java `cat examples/conf/druid/overlord/jvm.config | xargs` -cp "examples/conf/druid/_common:examples/conf/druid/_common/hadoop-xml:examples/conf/druid/overlord:lib/*" io.druid.cli.Main server overlord

 java `cat examples/conf/druid/historical/jvm.config | xargs` -cp "examples/conf/druid/_common:examples/conf/druid/_common/hadoop-xml:examples/conf/druid/historical:lib/*" io.druid.cli.Main server historical

 java `cat examples/conf/druid/middleManager/jvm.config | xargs` -cp "examples/conf/druid/_common:examples/conf/druid/_common/hadoop-xml:examples/conf/druid/middleManager:lib/*" io.druid.cli.Main server middleManager

 java `cat examples/conf/druid/broker/jvm.config | xargs` -cp "examples/conf/druid/_common:examples/conf/druid/_common/hadoop-xml:examples/conf/druid/broker:lib/*" io.druid.cli.Main server broker

 ```
 - Resetting cluster state
 ```sh
 rm -rf log
 rm -rf var
 bin/init
 ```
 - Start Tranquility
 ```sh 
 tranquility-distribution-0.8.2/bin/tranquility server -configFile ../examples/conf/tranquility/wikipedia-server.json -Ddruid.extensions.loadList=[]
 ```
 change the path `../examples/conf/tranquility/wikipedia-server.json` to custom json configuration.

 - Receive at http://localhost:8200/v1/post/`datasourcenamehere`
 - sql query at http://localhost:8082/druid/v2/sql
 - json query at http://localhost:8082/druid/v2?pretty

#Superset

* Install superset
```sh
pip install superset
```
* Create an admin user (you will be prompted to set username, first and last name before setting a password)
```sh
fabmanager create-admin --app superset
```
* Initialize the database
```sh
superset db upgrade
```
* Load some data to play with
```sh
superset load_examples
```
* Create default roles and permissions
```sh
superset init
```
* To start a development web server on port 8088, use -p to bind to another port
```sh
superset runserver -d
```
