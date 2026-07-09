---
created: 2025-06-29

modified: 2025-06-29

published: 2025-06-29

---

# Local Setup
###### First, you want to download MongoDB community
	https://www.mongodb.com/try/download/community
	Windowsx64, .msi file, version 8.0.4
###### Next, Install from .msi package
>[!info]- Which user for installation?
>**For Local Development:**
>
When setting up MongoDB for local development, the **Network Service user** is generally the **most convenient and recommended option**. Here's why:
>
>- **Simplicity:** It requires no extra configuration. You don't need to create a separate user account.
>- **Sufficient Permissions:** For local development, MongoDB primarily needs access to the file system to store data. The Network Service account has enough permissions for this.
>- **Security:** It follows the principle of least privilege. The service runs with the minimum necessary permissions, reducing potential security risks.

>[!info]- Changing the Service Name
Yes, you _can_ change the service name during installation on Windows. When you get to the "Service Configuration" screen in the MongoDB installer, you'll see a field for the "Service Name." By default, it's something like "MongoDB Server (version)." You can change this to "ContextStore" or any other name you prefer.
>
**Important Considerations for Service Names:**
>
>- **Uniqueness:** Service names must be unique on the system. If you already have a service with that name, you'll get an error.
>- **Consistency:** While you _can_ change the service name, it's generally recommended to stick with the standard "MongoDB Server" naming convention unless you have a strong reason to deviate. This makes it easier for others (or your future self) to understand what the service is. If you're using ContextStore as the name of your application that _uses_ MongoDB, it might be confusing to also have a service called ContextStore.
>- **Command-Line Usage:** If you change the service name, you'll need to use the new name when managing the service from the command line (e.g., `net start ContextStore`, `net stop ContextStore`).
###### Next, choose the directory to store the data/logs
Data: `C:\Users\nader\Development Workspaces\ContextCore\ContextWeave\context_weave_poc\contextstore\data`
Logs: `C:\Users\nader\Development Workspaces\ContextCore\ContextWeave\context_weave_poc\contextstore\log`
###### (Optional) Install MongoDB Compass
[MongoDB Compass](https://www.mongodb.com/products/tools/compass) is a GUI tool that makes it easier to visualize and manage your DB
###### Connect to local MongoDB server
The default connection string should be `mongodb://localhost:27017`

>[!warning]- Running from CLI
>Navigate to the MongoDB `bin` directory. This is usually:
>- **Windows:** `C:\Program Files\MongoDB\Server\[version]\bin`
>
>Run the `mongod` command. This starts the MongoDB server. You should see some output in the terminal.
>
>Run the `mongo` command. This opens the MongoDB shell, where you can interact with the database.



%% Begin Waypoint %%
- [[MongoDB Concepts]]
- [[Mongoose]]
- [[Mongosh Commands]]

%% End Waypoint %%

#research #development #mongodb 