import requests
import time


def Login(User, PW):
    r = requests.post('https://www.feastogether.com.tw/api/994f5388-d001-4ca4-a7b1-72750d4211cf/custSignIn?act=' + str(User), json = 
    {
    "act": str(User),
    "pwd": str(PW)
    })
    token = r.json()['result']['customerLoginResp']['token']
    token = "Bearer " + token
    # print(token)
    r.close()
    return token


def SaetSearch(User, token):
    url = 'https://www.feastogether.com.tw/api/booking/saveSaets'
    headers = { 'act' : User ,'authorization' : token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"} 
    r = requests.post(url, headers=headers)
    result = r.json()['statusCode']
    r.close()
    return result



def SeatSearch(User, token, storeid, peopleCount, mealPeriod , mealDate, mealTime, zkde):
    url = 'https://www.feastogether.com.tw/api/booking/saveSeats'
    headers = { 'act' : User ,'authorization' : token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"} 
    data = {
  "storeId": str(storeid),
  "peopleCount": int(peopleCount),
  "mealPeriod": str(mealPeriod),
  "mealSeq": 1,
  "mealDate": str(mealDate),
  "mealTime": str(mealTime),
  "zkde":str(zkde)
}
    r = requests.post(url, headers=headers, json=data)
    result = r.json()
    r.close()
    return result


def searchBookingAble(User, token, storeid, peopleCount, mealPeriod , mealDate):
    url = 'https://www.feastogether.com.tw/api/booking/searchBookingAble'
    headers = { 'act' : User ,'authorization' : token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"} 
    data = {
  "storeId": str(storeid),
  "adult": int(peopleCount),
  "child": int(child),
  "mealPeriod": str(mealPeriod),
  "mealDate": str(mealDate)
}

    r = requests.post(url, headers=headers, json=data)
    result = r.json()['result']['targetTimes']
    r.close()
    return result



    
def B00king(User, token):
    url = 'https://www.feastogether.com.tw/api/booking/b00king'
    headers = { 'act' : User ,'authorization' : token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"} 
    r = requests.post(url, headers=headers)
    result = r.json()['result']
    r.close()
    return result


def Booking(User, token, storeid, peopleCount, child , mealPeriod, mealDate, mealTime, mealSeq, yuuO):
    url = 'https://www.feastogether.com.tw/api/booking/booking'
    headers = { 'act' : User ,'authorization' : token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}  # 
    data = {
  "storeId": str(storeid),
  "mealDate": str(mealDate),
  "mealPurpose": "",
  "mealSeq": int(mealSeq),
  "mealTime": str(mealTime),
  "mealPeriod": str(mealPeriod),
  "special": 0,
  "childSeat": 0,
  "adult": int(peopleCount),
  "child": int(child),
  "chargeList": [
    {
      "seq": 201,
      "count": int(peopleCount)
    },
    {
      "seq": 202,
      "count": int(child)
    }
  ],
  "storeCode": "NTBQ",
  "redirectType": "iEat_card",
  "domain": "https://www.feastogether.com.tw",
  "pathFir": "booking",
  "pathSec": "result",
  "yuuO": yuuO
}
    r = requests.post(url, headers=headers, json=data)
    result = r.json()
    r.close()
    return result



if __name__ == '__main__':
    text = """
    Code by David_Zhu
    Version : v0.2
    
    storeid : S2212290042  # 信義旭集
    storeid : S2212290053  # 竹北旭集
    storeid : S2212290010  # 板橋饗食
    storeid : S2212290004  # 微風饗饗
    storeid : S2212290068  # 新莊饗饗
          """
    print(text)

    User = str(input("Please Input Account : "))
    PW = str(input("Please Input Password : "))

    storeid = str(input("Please Input StoreID : "))
    peopleCount = int(input("Please Input Adult Count (Max:8): "))
    child = int(input("Please Input Child Count : "))
    mealDate = str(input("Please Input Date (EX:2023-03-21): "))
    # mealTime =  str(input("Please Input Time (EX:11:30): "))
    mealPeriod = str(input("Please Input mealPeriod (EX:breakfast, lunch, tea, dinner): "))
    
    # Breaklist = ["06:30", "07:00", "07:30"]
    # Lunchlist = ["11:30", "12:00", "12:30"]
    # Afterlist = ["14:30"]
    # DinnerList = ["17:30", "18:00", "18:30"]
    # finalList = []
    # if mealPeriod == "lunch":
    #   finalList = Lunchlist
    # if mealPeriod == "tea":
    #   finalList = Afterlist
    # if mealPeriod == "dinner":
    #   finalList = DinnerList
    # if mealPeriod == "dinner":
    #   finalList = DinnerList
    # if mealPeriod == "breakfast":
    #   finalList = Breaklist


    mealSeq = 1
    zkde = "98djk3jaoisiilillillxch8ue"
    Token = Login(User, PW)
    # print(Login("0912900995", "d89756432"))
    print(Token)
    # time.sleep(5)
    # print(zkde)
    
    while True:
        # for mealSeq in range(1,4):
            # for mealTime in finalList:
            # try:
            result = searchBookingAble(User, Token, storeid, peopleCount, mealPeriod , mealDate)
            print(result)
            # except:
            # print("Time Expair, ReLogin.....")
              # Token = Login(User, PW)
              # print(Token)
              # result = searchBookingAble(User, Token, storeid, peopleCount, mealPeriod , mealDate)

            for able in result:
              if able['isEnable'] == True:
                print(able['time'] + " Have a Seat can be booking")
                # print(able['isEnable'])
                mealSeq = able['mealSeq']
                mealTime = able['time']
                # Token = '123'
                
                LoginConfirm = SaetSearch(User, Token)
                print(LoginConfirm)
                if  LoginConfirm == 104001:
                  Token = Login(User, PW)
                  print(Token)
                    
                print(SeatSearch(User, Token, storeid, peopleCount, mealPeriod, mealDate, mealTime, zkde))
                yuuO = B00king(User, Token)
                print(Booking(User, Token, storeid, peopleCount, child ,mealPeriod, mealDate, mealTime, mealSeq, yuuO))
                time.sleep(3)


              elif able['isEnable'] == False: 
                print("No Seat can be booking ..... Wait for Retry!!")
                time.sleep(3)
              

