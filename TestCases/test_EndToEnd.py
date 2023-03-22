import requests
import json
import jsonpath


def test_Add_student_detail():
    URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:/Users/user/Desktop/StudentDetails/StudentsDetails.json', 'r')
    json_file=json.loads(file.read())
    response= requests.post(URL,json_file)
    id=jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    skill_URL="https://thetestingworldapi.com/api/technicalskills"
    file=open('C:/Users/user/Desktop/StudentDetails/Update.json' , 'r')
    json_file=json.loads(file.read())
    json_file['id']=int(id[0])
    json_file['st_id']=id[0]
    response=requests.post(skill_URL,json_file)
    print(response.text)
    print(type(id[0]))

    address_URL="https://thetestingworldapi.com/api/addresses"
    file=open('C:/Users/user/Desktop/StudentDetails/Address.json','r')
    json_file=json.loads(file.read())
    json_file['stId']=id[0]
    response=requests.post(address_URL,json_file)
    print(response.text)

    finalDetail_URL="https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response=requests.get(finalDetail_URL)
    print(response.text)







