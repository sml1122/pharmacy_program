import requests
import bs4
from urllib.parse import quote


# 약국의 정보를 찾기
def detect_pharmacy(item, w_day, start_Time, end_Time):
    pharmacy_name = item.find('dutyname').text

    pharmacy_addr = item.find('dutyaddr').text

    pharmacy_tel = item.find('dutytel1').text

    amtime = None
    pmtime = None

    if w_day == "일요일":
        amtime = item.find('dutytime7s')
        pmtime = item.find('dutytime7c')

    elif w_day == "월요일":
        amtime = item.find('dutytime1s')
        pmtime = item.find('dutytime1c')

    elif w_day == "화요일":
        amtime = item.find('dutytime2s')
        pmtime = item.find('dutytime2c')

    elif w_day == "수요일":
        amtime = item.find('dutytime3s')
        pmtime = item.find('dutytime3c')

    elif w_day == "목요일":
        amtime = item.find('dutytime4s')
        pmtime = item.find('dutytime4c')

    elif w_day == "금요일":
        amtime = item.find('dutytime5s')
        pmtime = item.find('dutytime5c')

    elif w_day == "토요일":
        amtime = item.find('dutytime6s')
        pmtime = item.find('dutytime6c')

    elif w_day == "공휴일":
        amtime = item.find('dutytime8s')
        pmtime = item.find('dutytime8c')

    if amtime is not None:
        am_time = int(amtime.text)
        pm_time = int(pmtime.text)
        if (am_time >= int(start_Time)) and (pm_time <= int(end_Time)):
            dictoinary1 = {"pharmacy_name": pharmacy_name, "pharmacy_addr": pharmacy_addr,
                           "pharmacy_tel": pharmacy_tel, "am_time": am_time, "pm_time": pm_time}
            return dictoinary1
    else:
        return None


# UI에서 파라미터 받고 API 이용
def pharmarcy_API(w_day, start_Time, end_Time):
    # 공공데이터 인증키는 공유됨
    serviceKey = "YOUR KEY"

    # 전국 약국 정보 조회 서비스
    endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
    Q0 = quote("울산광역시")
    ORD = "NAME"
    pageNo = "1"
    startPage = "1"
    numOfRows = "500"
    startTime = start_Time
    endTime = end_Time
    wday = w_day

    paramset = "serviceKey=" + serviceKey + "&" + "Q0=" + Q0 + "&" + "ORD=" + ORD + "&" + \
               "pageNo=" + pageNo + "&" + "startPage=" + startPage + "&" + "numOfRows=" + \
               numOfRows

    url = endpoint + paramset
    result = requests.get(url)
    bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
    items = bs_obj.findAll("item")

    pharmacy_list = []
    for item in items:
        data_list = detect_pharmacy(item, wday, startTime, endTime)
        if data_list is not None:
            pharmacy_list.append({"day": wday, "data": data_list})

    return pharmacy_list
