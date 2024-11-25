from flask import Flask, request
from datetime import datetime, timezone

def get_utc_datetime_string():
    """Returns the current UTC date and time in the specified format."""
    now_utc = datetime.now(timezone.utc)
    return now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

app = Flask(__name__)

ids = {-10: {"id": 0,
        "userName": "dd",
        "password": "",
        "firstName": "",
        "lastName": "",
        "telephone": 0,
        "createdAt": str(get_utc_datetime_string()),
        "modifiedAt": str(get_utc_datetime_string())}}

@app.route('/store/user/<int:id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def get_user(id):
    print(id)
    if request.method == 'GET':

        if id in ids:
            return ids[id]
        else:
            return "User not found", 404

    elif request.method == 'POST':
        data = request.get_json() 
        ids[id] = {"id":data['id'],
                        "userName": data['userName'],
                        "password": data['password'],
                        "firstName": data['firstName'],
                        "lastName": data['lastName'],
                        "telephone": data['telephone'],
                        "createdAt": str(get_utc_datetime_string()),
                        "modifiedAt": str(get_utc_datetime_string())
                        }
        print(ids)
        return ids[id]
    
    elif request.method == 'DELETE': 
        a = ids[id]
        del ids[id]
        print(ids)
        return a
    
    elif request.method == 'PUT':
        data = request.get_json() 
        ids[id] = {"id":data['id'],
                        "userName": data['userName'],
                        "password": data['password'],
                        "firstName": data['firstName'],
                        "lastName": data['lastName'],
                        "telephone": data['telephone'],
                        "createdAt": data[id]['createdAt'],
                        "modifiedAt": str(get_utc_datetime_string())
                        }
        print(ids)
        return ids[id]
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
