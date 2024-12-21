import wx
import finance
import pandas as pd
class BriefFinance(wx.Frame):
    def __init__(self):
        super().__init__(None, title="주식 정보", size=(720, 640))
        panel = wx.Panel(self)
        large_font = wx.Font(36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        label = wx.StaticText(panel,label="나스닥 주식 보고서",pos=(20,10), size=(120,-1))
        label.SetFont(large_font)
        # 텍스트 입력 상자
        self.input_name = wx.TextCtrl(panel, pos=(400, 20), size=(200, 20), style=wx.TE_PROCESS_ENTER)
        self.input_name.Bind(wx.EVT_TEXT_ENTER,self.on_search)
        
        # 검색 버튼
        search_button = wx.Button(panel, label="검색", pos=(610, 20))
        search_button.Bind(wx.EVT_BUTTON, self.on_search)

        self.ticker_list = pd.read_csv("data/NYSE_Symbol.csv", encoding="ISO-8859-1")
        self.company_list = pd.read_csv("data/NYSE_company.csv", encoding="ISO-8859-1")
        self.companies = [f"{ticker} - {name}" for ticker, name in zip(self.ticker_list["Symbol"], self.company_list["Name"])]
        self.listbox = wx.ListBox(panel, choices=self.companies, size=(720, 600), pos=(0, 50))
        self.listbox.Bind(wx.EVT_LISTBOX_DCLICK, self.selected_company)
    def on_search(self, event):
        filter_text = self.input_name.GetValue() 
        self.listbox.Clear()
        self.ticker_list["Symbol"] = self.ticker_list["Symbol"].fillna("")
        self.company_list["Name"] = self.company_list["Name"].fillna("")
        filtered_company = [
            f"{ticker} - {name}" 
            for ticker, name in zip(self.ticker_list["Symbol"], self.company_list["Name"])
            if filter_text.upper() in ticker or filter_text.upper() in name
        ]
        if filtered_company:
            self.listbox.AppendItems(filtered_company)
        else:
            wx.MessageBox("검색 결과가 없습니다.", "알림", wx.OK | wx.ICON_INFORMATION)
            self.listbox.AppendItems(self.companies)
    def selected_company(self, ticker):
        ticker = ticker.GetString()
        ticker, name = ticker.split(" - ")
        target = finance.search_target(ticker)
        finance.make_PDF(target,ticker)
        wx.MessageBox(f"요청하신 {name}의 정보가 /Exported에 저장됨", "완료", wx.OK | wx.ICON_INFORMATION)


if __name__ == "__main__":
    app = wx.App()
    app.SetAppName("나스닥 주식 보고서")
    frame = BriefFinance()
    frame.SetBackgroundColour(wx.Colour(50, 50, 50))
    frame.Show()
    app.MainLoop()