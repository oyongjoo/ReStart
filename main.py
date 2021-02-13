# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pprint

from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
bb = kiwoom.CommConnect(block=True)
print(f"블록킹 로그인 완료, bb = {bb}")

"""
사용자 정보 얻어오기

키움 OpenAPI+는 로그인을 수행한 후 GetLoginInfo 메서드를 호출하여 사용자 정보를 얻을 수 있습니다. 
GetLoginInfo 메서드의 인자값에 따라 얻어올 수 있는 정보는 다음 표와 같습니다.
"""
account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")    # 전체 계좌수
accounts = kiwoom.GetLoginInfo("ACCNO")             # 전체 계좌 리스트
user_id = kiwoom.GetLoginInfo("USER_ID")            # 사용자 ID
user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명
keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")        # 키보드보안 해지여부
firewall = kiwoom.GetLoginInfo("FIREW_SECGB")       # 방화벽 설정 여부

print(account_num)
print(accounts)
print(user_id)
print(user_name)
print(keyboard)
print(firewall)

"""
종목 코드 얻기

API 사용에 있어 가장 먼저 할 일은 종목코드를 얻는것입니다. 
로그인이 완료되면 GetCodeListByMarket 메서드를 호출하여 
각 시장에 상장된 종목코드 리스트를 얻을 수 있습니다.

파라미터	시장
"0"	코스피
"3"	ELW
"4"	뮤추얼펀드
"5"	신주인수권
"6"	리츠
"8"	ETF
"9"	하이얼펀드
"10"	코스닥
"30"	K-OTC
"50"	코넥스
"""
kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
etf = kiwoom.GetCodeListByMarket('8')

print(f"kospi_len={len(kospi)}, kospi={kospi}")
print(f"kosdaq_len={len(kosdaq)}, kosdaq={kosdaq}")
print(f"len(etf)={len(etf)}, etf={etf}")

"""
종목명 얻기

증권사 API를 사용할 때 주로 종목코드를 사용합니다. 
그러나 종목코드만 보고는 어떤 종목인지 알기 어렵지요? 
키움 OpenAPI+의 GetMasterCodeName 메서드에 종목코드를 전달하면 종목명을 얻을 수 있습니다.
"""
name = kiwoom.GetMasterCodeName("005930")
print(name)

'''
연결 상태 확인

CommConnect 메소드를 통해 로그인을 수행한 후 
GetConnectState 메소드를 호출하여 연결 상태를 확인할 수 있습니다. 
GetConnectState 메소드의 리턴값이 
0이면 서버에 연결되지 않은 상태이고 
1이면 서버에 연결 상태임을 의미합니다.
'''
state = kiwoom.GetConnectState()
if state == 0:
    print("미연결")
else:
    print("연결중")

'''
상장 주식수 얻기

현재 키움증권의 API에는 버그가 있어서 상장 주식수가 21억을 넘더라도 
21억까지만 표현할 수 있습니다. 
삼성전자의 경우 약 59억주가 상장되어 있는데 이 값을 제대로 얻어올 수 없습니다.
'''
stock_cnt = kiwoom.GetMasterListedStockCnt("005930")
print(f"삼성전자 상장주식수: {stock_cnt}")

'''
감리구분

감리구분은 '정상', '투자주의', '투자경고', '투자위험', '투자주의환기종목'의 값을 갖습니다. 
삼성전자(005930)의 경우 '정상' 값이 출력됩니다.
'''
감리구분 = kiwoom.GetMasterConstruction("005930")
print(감리구분)

"""
상장일

어떤 종목의 상장일을 확인할 때 GetMasterListedStockDate 메소드를 사용합니다. 
위 코드는 다음과 같이 삼성전자의 상장일과 데이터 타입을 출력합니다.
"""
상장일 = kiwoom.GetMasterListedStockDate("005930")
print(상장일)
print(type(상장일))

"""
전일가

종목별 전일가는 GetMasterLastPrice 메소드를 통해 쉽게 얻을 수 있습니다. 
해당 메소드의 인자로 종목 코드를 입력하면 전일 종가를 리턴합니다.
"""
전일가 = kiwoom.GetMasterLastPrice("005930")
print(전일가)
print(type(전일가))

"""
종목상태
GetMasterStockState는 종목 상태를 리턴하는 메소드입니다. 메소드의 인자로 종목 코드를 입력하면 됩니다.
"""
종목상태 = kiwoom.GetMasterStockState("005930")
print(종목상태)

"""
테마그룹
GetThemeGroupList 메소드는 테마그룹명과 각 테마그룹에 대한 아이디 값을 얻을 수 있습니다.
"""
group = kiwoom.GetThemeGroupList(1)
pprint.pprint(group)

# 조건식을 PC로 다운로드
kiwoom.GetConditionLoad()

# 전체 조건식 리스트 얻기
conditions = kiwoom.GetConditionNameList()
print(f"conditions = {conditions}")

# 0번 조건식에 해당하는 종목 리스트 출력
condition_index = conditions[0][0]
condition_name = conditions[0][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(codes)

"""
pykiwoom 모듈을 사용하면 쉽게 TR 요청을 할 수 있습니다. 
opt10001 (주식 기본정보요청)은 한 종목에 대한 기본 정보를 얻을 수 있는 TR입니다. 
입력은 종목코드이고 출력은 싱글데이터로 한 로우 데이터입니다.
"""
df = kiwoom.block_request("opt10001",
                          종목코드="005930",
                          output="주식기본정보",
                          next=0)
print(df)

"""
멀티데이터 TR
싱글 데이터는 결괏값이 한 행(row)으로 구성된 데이터를 의미합니다. 
이에 반해 멀티 데이터는 여러 행으로 구성된 데이터를 의미합니다. 다음 그림을 보면 쉽게 이해가 될 겁니다.

출력(OUTPUT) 항목에 싱글데이터와 멀티데이터가 둘 다 존재하는 경우 
멀티데이터를 받으려면 멀티데이터의 이름(예: 주식일봉차트조회)를 사용합니다.
"""
# TR 요청 (연속조회)
dfs = []
df = kiwoom.block_request("opt10081",
                          종목코드="005930",
                          기준일자="20200424",
                          수정주가구분=1,
                          output="주식일봉차트조회",
                          next=0)
print(df.head())
dfs.append(df)

while kiwoom.tr_remained:
    df = kiwoom.block_request("opt10081",
                              종목코드="005930",
                              기준일자="20200424",
                              수정주가구분=1,
                              output="주식일봉차트조회",
                              next=2)
    dfs.append(df)
    time.sleep(1)

df = pd.concat(dfs, ignore_index=True) # 각각의 결과에 대한 index를 무시하고 재정렬 시키기
df.sort_values(by='일자')
df.to_excel("005930.xlsx")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
