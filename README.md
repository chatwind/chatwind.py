<div align="center">
  <br>

# chatwind.py
<br>
<p>
Official RESTful Python API wrapper for the Chatwind API
</p>
<br>
<p>
<br>
<a href="https://www.pypi.org/project/chatwind.py"><img src="https://static.pepy.tech/badge/chatwind.py/month" alt="PyPi downloads" /></a>
<a href="https://www.pypi.org/project/chatwind.py"><img src="https://api.ghprofile.me/view?username=chatwind-chatwind.py&label=repository%20view%20count&style=flat" alt="Repository view count" /></a>
</p>

<br>

</div>

# Usage

## Add the package
To start, you will need to add the package. To do that, simply run `pip install chatwind.py`. In your code, add the following:
```py
import chatwind
```
Now you can use any of the functions below!

---

### Getting a user's information
```py
user = chatwind.user("USERNAME")
print(user)
```
The code above should return a 200 OK message. (JSON)

### Get a list of the Chatwind voice servers
```py
servers = chatwind.servers()
print(servers)
```
The code above should return a 200 OK message. (JSON)

### Check if a custom meeting code is valid
```py
customcode = chatwind.customcode("CODE")
print(customcode)
```
The code above should return a 200 OK message. (JSON)

### Get the statistics for Chatwind
```py
stats = chatwind.stats()
print(stats)
```
The code above should return a 200 OK message. (JSON)
