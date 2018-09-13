# druid-superset
## Schema Design
We send to Druid data in JSON format. Each segment of data that is sent is considered an **Event**.

This is the format of an **Event** (Note: they are all strings):

'''python
        {
          "type",
          "nodeID",
          "staffID",
          "staff_title",
          "unit",
          "room_number",
          "response_type",
          "response_message"
        }
'''
