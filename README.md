### 2024 Chung-ang university open-source programing final - sangwoolee, dongyunye
'''bash
    pip install pandas
    pip install yfinance
    pip install fpdf
    pip install wxpython
## SequenceDiagram
```mermaid
sequenceDiagram
    participant User
    participant GUI.py
    participant finance.py

    User->>GUI.py: Search for stock "AAPL"
    GUI.py->>finance.py: Request stock data for "AAPL"
    finance.py-->>User: Return stock data PDF for "AAPL"
    GUI.py-->>User: PDF for "AAPL" is ready
