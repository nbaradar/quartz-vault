---
created: 2025-06-29

modified: 2025-07-05

published: 2025-06-29

---

>[!note]
>[Cheat Sheet](https://www.mongodb.com/developer/products/mongodb/cheat-sheet/)
# Helpers
Show Database
```
show dbs
db // prints the current database
```

Switch Database
```
use <database_name>
```

Show Collections
```
show collections
```

Run Javascript File
```
load("myScript.js")
```
# CRUD Operations
#### Create
```javascript
db.[dbname].insertOne({name: "Max"})
db.[dbname].insertMany([{name: "Max"}, {name:"Alex"}]) // ordered bulk insert
db.[dbname].insertMany([{name: "Max"}, {name:"Alex"}], {ordered: false}) // unordered bulk insert
db.[dbname].insertOne({date: ISODate()})
db.[dbname].insertOne({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
```
