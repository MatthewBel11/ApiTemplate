# Custom API Template

Welcome to the **Custom API Template**! This template is designed to streamline the setup process for API development, making it ideal for hackathons, personal projects, or quick prototypes. It includes basic configurations and routes to get you started with building RESTful APIs.

---

## 🚀 Getting Started

### 1. Fork the Repository

To get started, create your own copy of the repository by forking it:

1. Go to the [Custom API Template repository](https://github.com/MatthewBel11/CustomApiTemplate).
2. Click on the **Fork** button in the top-right corner of the page.
3. This will create a copy of the repository under your GitHub account.

### 2. Clone Your Forked Repository

After forking, clone the repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/CustomApiTemplate.git
```

> Replace `YOUR_USERNAME` with your GitHub username.

Navigate into the project directory:

```bash
cd CustomApiTemplate
```

### 3. Install Required Libraries

To install the necessary libraries, use `pip` to install dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 📄 Code Overview

Below is a breakdown of the core components of the API template.

### **1. Project Structure**

- **`app.py`**: Main file containing the API routes and logic.
- **`requirements.txt`**: Lists all required Python packages to run the API.

### **2. Code Explanation**

#### **Importing Necessary Libraries**

```python
from flask import Flask, request, jsonify
```

- `Flask`: A lightweight WSGI web application framework used to build the API.
- `request`: Allows us to handle incoming requests and retrieve request data.
- `jsonify`: Helps in formatting Python dictionaries into JSON format for responses.

#### **Creating the Flask App**

```python
app = Flask(__name__)
```

- Initializes the Flask application.

#### **Home Route**

```python
@app.route("/")
def home():
    return 'Home - this is a basic API template. Read "README.md" for setup.'
```

- This route serves as the home endpoint, returning a welcome message.

---

### **3. API Routes**

#### **GET Request Example**

```python
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Reggie Roo",
        "email": "reggieroo@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200
```

- **Path Parameter (`<user_id>`)**: Allows passing dynamic values in the URL, e.g., `/get-user/1111`.
- **Query Parameters**: You can also pass additional data as query parameters, like `/get-user/1111?extra=hello+world`.
- **Response**: Returns a JSON object with the user's details and a 200 status code indicating success.

#### **POST Request Example**

```python
@app.route("/create-user", methods=['POST'])
def create_user():
    data = request.get_json()
    # Placeholder for implementing functionality to create a new user.
    return jsonify(data), 201
```

- **Method Specification**: Since this is a POST request, we specify `methods=['POST']`.
- **Request Body**: Expects JSON data from the request body.
- **Response**: Returns the received data with a 201 status code, indicating that a resource has been created successfully.

---

## 🛠️ Running the Application

To start the application in development mode:

```bash
python app.py
```

The application will be accessible at **`http://127.0.0.1:5000/`** by default.

---

## 📌 Conclusion

This **Custom API Template** provides a foundation for building APIs quickly and efficiently. By following the steps outlined in this guide, you should be able to set up, run, and expand upon this API for various projects. Feel free to modify the routes, add new endpoints, and implement additional functionality as needed!


---