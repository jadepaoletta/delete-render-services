This script is used to delete services in a Render account.

**PLEASE PROCEED WITH CAUTION WHEN TAKING DESTRUCTIVE ACTIONS, AS SERVICE DELETIONS CANNOT BE REVERSED**

**This script is not officially supported by Render. Use at your own risk.**

### Install dependencies
```
pip install -r requirements.txt
```

### Usage: 
```
python delete_services.py [OPTIONS]
-k, --api_key [REQUIED]
-n, --namespace [REQUIED]
--suspended [OPTIONAL]
```

You will be prompted to answer y/n to delete each service

```
Retrieving services for namespace: usr-xxx
Retrieved 12 services

Id: srv-xxx
Name: Next app
Suspended?: not_suspended
Namespace: usr-xxx

Delete service srv-xxx? (y/n) (q to quit):
```
