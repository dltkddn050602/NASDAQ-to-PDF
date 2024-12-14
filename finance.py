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

    pdf.cell(200, 10, txt="1. 기본 정보", align="L", border=1, ln=True)
    company_info(pdf, target, '주소', 'address1')
    company_info(pdf, target, '전화번호', 'phone')
    company_info(pdf, target, '웹사이트', 'website')
    company_info(pdf, target, '산업', 'industry')
    company_info(pdf, target, '섹터', 'sector')
    
    # 재무 정보 섹션
    pdf.cell(200, 10, txt="2. 재무 정보", align="L", border=1, ln=True)
    company_info(pdf, target, '시가총액', 'marketCap','$')
    company_info(pdf, target, '총 수익', 'totalRevenue','$')
    company_info(pdf, target, '순이익', 'netIncomeToCommon','$')
    company_info(pdf, target, '주당 수익 (Trailing EPS)', 'trailingEps')
    company_info(pdf, target, '배당률', 'dividendRate')
    company_info(pdf, target, '배당 수익률', 'dividendYield')
    company_info(pdf, target, '최근 배당 금액', 'lastDividendValue')
    
    # 주식 데이터 섹션
    pdf.cell(200, 10, txt="3. 주식 데이터", align="L", border=1, ln=True)
    company_info(pdf, target, '현재 주가', 'currentPrice','$')
    company_info(pdf, target, '52주 최고가', 'fiftyTwoWeekHigh','$')
    company_info(pdf, target, '52주 최저가', 'fiftyTwoWeekLow','$')
    company_info(pdf, target, '거래량', 'regularMarketVolume','$')
    
    # 추천 의견 섹션
    pdf.cell(200, 10, txt="4. 추천 의견", align="L", border=1, ln=True)
    company_info(pdf, target, '목표 최고가', 'targetHighPrice','$')
    company_info(pdf, target, '목표 최저가', 'targetLowPrice','$')
    company_info(pdf, target, '투자 의견', 'recommendationKey')
    pdf.output(f"{directory}/Exported/{name} info.pdf")

def company_info(pdf, target,name,info,txt=""):
    try:
        if txt:
            pdf.multi_cell(200, 10, txt= name + ": " + str(target.info[info]) + txt, align='L')
        else:
            pdf.multi_cell(200, 10, txt= name + ": " + str(target.info[info]), align='L')    
    except:
        pdf.multi_cell(200, 10, txt= name + ": " + 'N/A', align='L')