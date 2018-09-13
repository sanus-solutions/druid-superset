# druid-superset
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
   
  
