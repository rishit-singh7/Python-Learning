#7. Write a program to find out whether a given post is talking about “Harry” or not

post = input("Enter your post: ")

if("harry".lower() in post.lower()):
    print("The post is talking about harry")
else:
    print("The post is not talking about harry")
