import yfinance as yf
from fpdf import FPDF
import os

def search_target(target) :
    target = yf.Ticker(target)
    return target


def make_PDF(target, name):
    pdf = FPDF()
    pdf.add_page()
    directory = os.getcwd()
    pdf.add_font("Nanum", "", f"{directory}/data/NanumGothic.ttf", uni=True)
    pdf.set_font("Nanum", size=12)
    pdf.cell(200, 20, txt= f"요청하신 {name}의 주식 정보입니다.", ln=True, align='L', border=1)
    pdf.cell(200,10,ln=True)

    pdf.cell(200, 10, txt="1. 기본 정보", align="L", ln=True)
    company_info(pdf, target, '주소', 'address1')
    company_info(pdf, target, '전화번호', 'phone')
    company_info(pdf, target, '웹사이트', 'website')
    company_info(pdf, target, '산업', 'industry')
    company_info(pdf, target, '섹터', 'sector')
    
    # 재무 정보 섹션
    pdf.cell(200,10,ln=True)
    pdf.cell(200, 10, txt="2. 재무 정보", align="L", ln=True)
    company_info(pdf, target, '총 수익', 'totalRevenue','$')
    company_info(pdf, target, '순이익', 'netIncomeToCommon','$')
    company_info(pdf, target, '총 현금', 'totalCash','$')
    company_info(pdf, target, '총 부채', 'totalDebt')
    company_info(pdf, target, '부채 비율', 'debtToEquity',' - 부채비율은 회사의 부채가 자본에 비해 얼마나 많은지를 나타냅니다.')
    company_info(pdf, target, '순이익', 'netIncomeToCommon','$')
    company_info(pdf, target, "이익률", "profitMargins", " - 이익률은 회사가 매출에서 얼마를 순이익으로 남겼는지를 나타냅니다.")
    company_info(pdf, target, "자기자본 수익률", "returnOnEquity", " - 자기자본 수익률은 회사가 자본을 얼마나 잘 활용하는지를 나타냅니다.")
    company_info(pdf, target, "순이익 성장률", "earningsGrowth", " - 순이익 성장률은 회사의 순이익이 얼마나 성장했는지를 나타냅니다.")
    company_info(pdf, target, "매출 성장률", "revenueGrowth", " - 매출 성장률은 회사의 매출이 얼마나 성장했는지를 나타냅니다.")
    
    # 주식 데이터 섹션
    pdf.cell(200,10,ln=True)
    pdf.cell(200, 10, txt="3. 주식 데이터", align="L", ln=True)
    company_info(pdf, target, '시가총액', 'marketCap','$')
    company_info(pdf, target, '현재 주가', 'currentPrice','$')
    company_info(pdf, target, '주당 수익 (Trailing EPS)', 'trailingEps')
    company_info(pdf, target, '배당률', 'dividendRate', ' - 배당률은 주식이 투자자에게 얼마나 배당금을 지급하는지를 나타내는 지표로, 주식의 투자 수익률을 평가하는 데 사용됩니다.')
    company_info(pdf, target, '배당 수익률', 'dividendYield', ' - 주식 투자자에게 배당금이 얼마나 지급되는지를 나타내는 비율로, 안정적인 현금 흐름을 제공하는 기업에 투자하려는 투자자에게 중요합니다.')
    company_info(pdf, target, '최근 배당 금액', 'lastDividendValue')
    company_info(pdf, target, '배당 성향', 'payoutRatio',' - 배당 성향은 기업이 순이익 중 얼마나 많은 비율을 배당금으로 지급하는지를 나타내는 지표입니다.')
    company_info(pdf, target, '52주 최고가', 'fiftyTwoWeekHigh','$',' - 52주 최고가는 1년동안 해당 주식이 기록한 가장 높은 가격을 의미합니다')
    company_info(pdf, target, '52주 최저가', 'fiftyTwoWeekLow','$', ' - 52주 최저가는 1년 동안 해당 주식이 기록한 가장 낮은 가격을 의미합니다.')
    company_info(pdf, target, '거래량', 'regularMarketVolume','$')
    company_info(pdf, target, '순이익 성장률', 'earningsGrowth','$',' - 순이익 성장률은 기업의 순이익이 일정 기간 동안 얼마나 증가 또는 감소했는지를 나타내는 지표입니다. 값이 양수이면 수익성이 개선, 음수이면 악화되고 있다는 것을 의미합니다.')
    
    # 추천 의견 섹션
    pdf.cell(200,10,ln=True)
    pdf.cell(200, 10, txt="4. 추천 의견", align="L", ln=True)
    company_info(pdf, target, '목표 최고가', 'targetHighPrice','$', ' - 목표 최고가는 애널리스트들이 예상하는 주식의 최고 가격으로, 주식의 상승 여력을 평가하는 데 유용합니다.')
    company_info(pdf, target, '목표 최저가', 'targetLowPrice','$', ' - 목표 최저가는 애널리스트들이 예상하는 주식의 최저 가격으로, 주식의 하락 위험을 평가하는 데 도움이 됩니다.')
    company_info(pdf, target, '목표 평균가', 'targetMeanPrice','$', ' - 목표 평균가는 애널리스트들이 예상하는 주식의 평균 목표 가격으로, 주식의 현재 가격과 비교하여 목표가가 얼마나 높은지 평가할 수 있습니다.')
    company_info(pdf, target, '추천 평균', 'recommendationMean', ' - 추천 평균은 애널리스트들이 주식에 대해 제시하는 평균 추천 점수로, 1에 가까운 값은 “매수” 추천을, 5에 가까운 값은 “매도” 추천을 의미합니다.')
    company_info(pdf, target, '투자 의견', 'recommendationKey')
    
    pdf.output(f"{directory}/Exported/{name} info.pdf")

def company_info(pdf, target,name,info,txt="", note =""):
    try:
        if note and txt:
            pdf.multi_cell(200, 10, txt= name + ": " + str(target.info[info]) + txt + note, align='L')
        elif txt:
            pdf.multi_cell(200, 10, txt= name + ": " + str(target.info[info]) + txt, align='L')
        else:
            pdf.multi_cell(200, 10, txt= name + ": " + str(target.info[info]), align='L')    
    except:
        pdf.multi_cell(200, 10, txt= name + ": " + 'N/A', align='L')