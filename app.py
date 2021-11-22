import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data = [
   { 
  "course": 411,
  "courseName": "Software in Telecommunications",
  "releaseYear": 2021,
  "courseActive": True,
  "droppedStudents": "null",
  "date": 20210218,
  "someData": [
    [
      11,
      2
    ],
    [
      22,
      4
    ],
    [
      33,
      1
    ],
    [
      44,
      5
    ]
  ],
  "scores": {
    "a": 77,
    "b": 46,
    "c": 91
  }
}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Task 02</h1>
<p>A prototype API.</p>'''



@app.route('/api/v1/task2/datas/all', methods=['GET'])
def api_all():
    return jsonify(data)

app.run()