import requests
import json
import jsonpath

def test_add_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/user/Desktop/StudentDetails/StudentsDetails.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    print(response.text)


'''def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7160756"
    response = requests.get(API_URL)
    json_response=json.loads(response.text)
    id= jsonpath.jsonpath(json_response, 'data.id')
    print(json_response)
    print(id[0])
    assert id[0]==7160756'''

def test_update_student_data():
    API_URL= "https://thetestingworldapi.com/api/studentsDetails/7160756"
    f=open('C:/Users/user/Desktop/StudentDetails/Update.json', 'r')
    json_update=json.loads(f.read())
    response=requests.put(API_URL,json_update)
    print(response.text)

def test_delete_student_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails/7160756"
    response=requests.delete(API_URL)
    print(response.text)

def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7160756"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(json_response)
    print(id[0])
    assert id[0] == 7160756


