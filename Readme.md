# Fast Api Tutorial

## Social Media Application API

### Following Sanjeev Tygarajan Tutorial

## Day 1 of 20

<!-- Path Defination or Route Defination-->

@app.get("/api/")\n
async def root():\n
return {"message": "Hello From FastAPI"}

line 1 represents a decorator of the path or say endpoint, it is important to make the api work
line 2 represents the function which must be invoked when the endpoint is called
line 3 return the data object after the operation is complete

On further breaking down
-> "get" is a http method which returns the data object which we requested
-> "/api/" represents the path of the endpoint, this is really important too. When want the user data we use "/api/users" and when we want the post data we use "/api/post" these two paths are completely different and has different jobs to do. That is why path is provided in the function representing that this method must be invoked only when this path is called
-> "post", "put", "delete" are other http methods we have
-> "async" represents that the method is asynchronous, this is used when the function is interacting with the database and we might have to do something without wait for the response
-> "root" is the method name it can be anything
![Structure of the Route](image-1.png)
