from flask import Flask, request, jsonify

app = Flask(__name__)

# GET - REQUEST DATA FROM A SPECIFIC RESOURCE
# POST - CREATE A RESOURCE E.G AN AI PROMPT
# PUT - UPDATE A RESOURCE
# DELTE - DELETE A RESOURCE

@app.route("/")
def home():
    return 'Home this is a basic api template, read "README.md" for setup.'

# EXAMPLE GET REQUEST
# The thing in <> is a path parameter and allows us to pass paramaters to a url e.g url would be "/get-user/1111
# We can then directly access the path parameter in the function allowing us to do use it.
@app.route("/get-user/<user_id>") 
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name" : "Reggie Roo",
        "email": "reggieroo@example.com"
    }

    # We can also pass something called QUERY parameters which is essential additional variables. an example url with a query parameter would be 
    # "/get-user/1111?extra=hello+world"
    # Also be mindful when using these, we have to use URL encoding e.g we cannot use spaces " " so instead we denote them by doing %20 or alternatively a + sign for better readability

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200 # JSON - javascript object notation, 200 if the default status code for success




# EXAMPLE POST REQUEST
# As we aren't using the default GET rwquest we have to  specify in the METHODS, multiple can be accepted e.g ['POST', 'GET']
# As its a POST request we will be recieveing JSON data 
@app.route("/create-user", methods=['POST']) 
def create_user(user_id):
    data = request.get_json()
    # This is where you would implement functionality for creating a user or whatever you are using this for.
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
