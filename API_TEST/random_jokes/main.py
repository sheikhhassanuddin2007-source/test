


import requests

def main():
    response=requests.get("https://api.freeapi.app/api/v1/public/randomjokes/100")
    result=response.json()

    print(result["data"]["content"])  


if __name__ == "__main__":
    main()                        
                          
