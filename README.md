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

## Schema Design
We send to Druid data in JSON format. Each segment of data that is sent is considered an **Event**.

This is the format of an **Event** (note: they are all strings):


```python
        {
          "time",
          "type",
          "nodeID",
          "staffID",
          "staff_title",
          "unit",
          "room_number",
          "response_type",
          "response_message"
        }
```
An example POST payload is:

```
{
        "time": "2008-09-15T15:53:00",
        "type": "entry",
        "nodeID": "NSICU2500",
        "staffID": "6785246213",
        "staff_title": "Nurse",
        "unit": "ICU",
        "room_number": "2500",
        "response_type": "entry",
        "response_message": "clean"
}

```


### Legend:

- *time* - ISO 8601 formated timestamp
- *type* - The type of event. This can be `entry, alert, dispeser`
- *nodeID* - The ID of the physical node placed in the hospital. This ID will have a specific coding to it so that you can find the Unit and Room Number from it.
- *staffID* - The ID associated with the specific staff member. This can be either a name or a specific number.
- *unit* - This is the unit name within the hospital which will be derived from the coding of the *nodeID* (ex. ICU)
- *room_number* - This is the room number where the node resides. This is also derived from the *nodeID* (ex. RM301)
- *response_type* - Type of response that is being given to user. This can be `entry, alert, dispeser`
- *response_message* 
   - `entry` can have either `"clean" or "not clean"`
   - `alert` can have either `"alert given" or "no alert"`
   - `dispenser` can have `"none"``
  