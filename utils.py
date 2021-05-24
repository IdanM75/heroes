import requests


def yad_va_shem():
    content = requests.post("https://photos.yadvashem.org/PhotosWS.asmx/getPhotosList", headers={
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "100",
        "Content-Type": "application/json; charset=UTF-8",
        "Cookie": "userShowDonate=1; ASP.NET_SessionId=pikpcli0cm20k0qlh4d3124k; __za_19763107=%7B%22sId%22%3A4975508"
                  "%2C%22dbwId%22%3A%221%22%2C%22sCode%22%3A%2215d80b973b57b3c0c23a2883a617999e%22%2C%22sInt%22%3A500"
                  "0%2C%22aLim%22%3A2000%2C%22asLim%22%3A100%2C%22na%22%3A4%2C%22td%22%3A1%2C%22ca%22%3A%221%22%7D;"
                  " __za_cd_19763107=%7B%22visits%22%3A%22%5B1617052823%5D%22%2C%22campaigns_status%22%3A%7B%2247572%2"
                  "2%3A1617092718%2C%2247599%22%3A1617089520%2C%2251781%22%3A1617052843%7D%7D; TS0182e6e2=016dcde99e15"
                  "feb180ca5a802c769d9635f7dc12f2e2c6578688b39824719909e03c63644e1f9734d439e00183b5c43fa1cbab3d0e; __"
                  "atuvc=5%7C13; __atuvs=6062de35aef44f73002",
        "Host": "photos.yadvashem.org",
        "Origin": "https://photos.yadvashem.org",
        "Referer": "https://photos.yadvashem.org/index.html?language=en&displayType=list",
        "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 1 1_2_1) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.90 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",

    }, data={"uniqueId": "-7682997668154270557", "langApi": "ENG", "rowNum": 980, "orderBy": "BOOK_ID",
             "orderType": "asc"}).content
    print(content)
    # soup = BeautifulSoup(content, 'html.parser')
    # print(soup.findChildren('table'))
