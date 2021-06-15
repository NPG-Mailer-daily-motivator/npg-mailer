import requests
from bs4 import BeautifulSoup
import schedule
import time


def job():
    czas = str(time.strftime("%Y-%m-%d", time.localtime()) )
    
    url1 = 'https://www.coindesk.com/price/bitcoin'
    url2 = 'https://finance.yahoo.com/quote/OTGLF/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAJaDrr-Iotdmj928Ob6Fv40VQIjNirHQlPbzWcRqbFzjqgU6Zve906qozRuGgjUC5uwlWpDd2oSP9k7T23c23NA9ukP3d9qFLL8EKa5IMMRmzAoHqgNIO68dTy6Lumv0bPy7SBdErYhU9SsbykES7GcSQpdpT5o5qcGmXqF12OiR'

    r1 = requests.get(url1, headers={'user-agent': 'npg.daily.motivator.pl'})
    soup1 = BeautifulSoup(r1.text, "lxml")
    body1 = soup1.body
    div1 = body1.find('div', {'class': 'price-large'})

    bitcoin = div1.get_text()

    r2 = requests.get(url2, headers={'user-agent': 'npg.daily.motivator.pl'})
    soup2 = BeautifulSoup(r2.text, "lxml")
    body2 = soup2.body
    div2 = body2.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})

    project_red_act_value = div2.get_text()
    project_red_17Sep_value = 109.00
    project_red_diff = str(project_red_17Sep_value - float(project_red_act_value))

    s = "Dzisiejsza wartość bitcoina to " + bitcoin + "\nA akcje Cd projekt red to $" + project_red_act_value + " czyli jest o $" + project_red_diff + " mniej od premiery Cyberpunk 2077 \n"
    print (s)

   
    return

schedule.every(20).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
