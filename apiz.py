import requests

# GET request to retrieve a list of posts
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.json())

# GET request to retrieve a specific post by ID
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())


# POST request to create a new post
new_post = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts/1", json=new_post)
print(response.json())



# PUT request to update a specific post by ID
updated_post = {
    "id": 1,
    "title": "updated title",
    "body": "updated body",
    "userId": 1
}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_post)
print(response.json())


# DELETE request to delete a specific post by ID
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)