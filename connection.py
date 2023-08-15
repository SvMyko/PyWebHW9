from mongoengine import connect, ConnectionError


def mongo_connect():
    connection_string = "mongodb+srv://deuterrium:QdW9KTJr3ssa8gMy@cluster0.7r0vvpw.mongodb.net/test?retryWrites=true&w=majority"

    try:
        connect(host=connection_string)
        print("Connection to the database established.")
    except ConnectionError as e:
        print(f"Database connection error: {e}")