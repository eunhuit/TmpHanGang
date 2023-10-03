import requests, json, random, openpyxl
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
url = 'https://hangang.life/api/'
result = requests.get(url,headers=headers).text
data = json.loads(result)
tmp = data['temp'] #현재온도
date = data['time']
year = date[0:4].strip()
mon = date[5:7].strip()
day = date[8:10].strip()
time = date[11:13].strip()
min = date[14:16].strip()
min1 = min + "분"
if int(min) == 00:
    min1 = ""
if int(time) > 13:
    time1 = int(time) - 12
    time1 = "오후 " + str(time1)
else:
    time1 = int(time)
wb = openpyxl.load_workbook('hanganggang.xlsx',data_only=True)
ws = wb.active
say = random.choice(tuple(ws.rows))
print(say[0].value)
print(f"💧한강 물 온도: {tmp}℃")
print(f"⏰측정시각: {year}년{mon}월{day}일ㅣ{time1}시{min1}")
print(f"🧭측정장소: 서울 노량진")