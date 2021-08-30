import pandas as pd
ns = pd.read_excel('네이버_뉴스_제목_데이터.xlsx', engine='openpyxl')
ns = ns.drop_duplicates(['Field2_text'], keep='first')
ns.to_csv('sor_test.csv', encoding='utf-8-sig')