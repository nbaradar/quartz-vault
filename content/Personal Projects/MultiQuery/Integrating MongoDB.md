---
title: Integrating MongoDB
tags:
  - lab
  - multiquery
  - contextcore
  - mongodb
created: 2025-06-29

modified: 2025-06-29

published: 2025-06-29

---
Let's integrate MongoDB so the exported result.json file gets stored in a database called "MultiQuery" in the collection "result" 

Things you need to do...
- Setup the database
- Add connection info to config file
- Create mongodb util for CRUD operations
- Modify export functionality to include MongoDB CRUD

---

First of all, installing MongoDB on mac is different. 
Remember where you store your mongod.conf file, you need to use it when starting the DB:
```bash
mongod --config /usr/local/mongodb/mongod.conf
```