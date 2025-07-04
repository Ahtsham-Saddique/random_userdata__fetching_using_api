# user_data_acess_using_api.py
import requests
import json

def get_data():
    url='https://api.freeapi.app/api/v1/public/randomusers/user/random'

    response=requests.get(url)

    data=response.json()

    if data["success"] and 'data' in data:
        user_data=data["data"]

        title=user_data["name"]["title"]
        first_name=user_data["name"]["first"]
        last_name=user_data["name"]["last"]

        username=user_data["login"]["username"]
        password=user_data["login"]["password"]
        picture=user_data["picture"]["thumbnail"]

        return title,first_name,last_name,username,password,picture
    else:
        raise Exception ("Failes to connect")
    
def main():
    try:
       title,first_name,last_name,username,password,picture= get_data()

       print(f"Title={title}\n")
       print(f"First_name={first_name}\n")
       print(f"Last_name={last_name}\n")
       print(f"Username={username}\n")
       print(f"Password={password}\n")
       print(f"Picture={picture}\n")
    except Exception as e:
        print(str(e))


if __name__=="__main__":
    main()