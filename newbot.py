from flask import Flask, request, jsonify 
import json 

app = Flask(__name__) 
port = '5000' 

@app.route('/', methods=['POST']) 
def index(): 
  print("hihihihihih") 
  return jsonify( 
    status=200, 
    replies=[{ 
      'type': 'text', 
      'content': 'j ai suivit ton sms', 
    }], 
    conversation={ 
      'memory': { 'key': 'value' } 
    } 
  ) 
 
@app.route('/errors', methods=['POST']) 
def errors(): 
  print(json.loads(request.get_data())) 
  return jsonify(status=200) 
 
app.run(port=port)
