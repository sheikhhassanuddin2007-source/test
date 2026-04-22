
import requests

def stocks():
    url=("https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata")
    response=requests.get(url)
    data=response.json()

    if data["success"] in data and [data][data]:
        user_data=data["data"]["data"]

        Product_Name=user_data[1]["Name"]
        CurrentPrice=user_data[1]["CurrentPrice"]

        return Product_Name,CurrentPrice
    

def main():

    try:

     Product_Name,CurrentPrice=stocks()

    
    
     print(f"The name of the product:,{Product_Name} and the price of it :,{CurrentPrice}")

    except Exception:
       print("NOT found")

    

if __name__ == "__main__":
   main()    


    

                    


