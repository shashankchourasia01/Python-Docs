import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)

    data = response.json()

    if data["success"] and "data" in data:
        user_Data = data["data"]

        user_name = user_Data ["name"] ["last"]

        country = user_Data ["location"] ["state"]

        return user_name, country
    
    else:
        raise Exception("Failed to fetch user data")




def main():
    try:
        user_name , country = fetch_random_user_freeapi()
        print(f"User_name: {user_name} \n Country: {country}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

