from flask import Flask, jsonify, request

app = Flask(__name__)


tasks = [{
    "id": 1,
    "title" : "groceries",
    "description" : "milk, cheese, bread",
    "done": False
},
{
    "id": 2,
    "title": "cars",
    "description": "toyota, maruti, viper",
    "done" : False
}]

@app.route("/add-data", methods = ["POST"])

def addTask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data",

        },400)
    task = {
        "id": tasks[-1]["id"]+1,
        "title": request.json["title"],
        "description": request.json.get("description", ''),
        "done": False
    }
    tasks.append(task)
    return jsonify({
        "status": "Succesful",
        "message": "Data added succesfully"
    })



@app.route("/get-data")

def getdata():
    return jsonify({
        "data": tasks
    })


@app.route("/")

def Helloworld():
    return("Helloworld")


@app.route("/try")

def Eighteen():
    return("Hi ritvik")

if(__name__ == "__main__"):
    app.run(debug = True)


