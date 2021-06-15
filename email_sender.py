import yagmail
import requests
from bs4 import BeautifulSoup
import random
import schedule
import time


def job():
    czas = str(time.strftime("%Y-%m-%d", time.localtime()) )
    
    ilosc_linii = sum(1 for line in open('zlote-mysli.txt'))

    linia = random.randint(0, ilosc_linii)

    mysli_plik = open("zlote-mysli.txt", "r", encoding="utf-8")
    mysli_plik_linie = mysli_plik.readlines()
    mysli_plik.close()

    random_mysl = mysli_plik_linie[linia]
    del mysli_plik_linie[linia]
    mysli_plik_wrt = open("zlote-mysli.txt", "w+", encoding="utf-8")
    for lin in mysli_plik_linie:
        mysli_plik_wrt.write(lin)
    mysli_plik_wrt.close()


    url1 = 'https://www.coindesk.com/price/bitcoin'
    url2 = 'https://finance.yahoo.com/quote/OTGLF/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAJaDrr-Iotdmj928Ob6Fv40VQIjNirHQlPbzWcRqbFzjqgU6Zve906qozRuGgjUC5uwlWpDd2oSP9k7T23c23NA9ukP3d9qFLL8EKa5IMMRmzAoHqgNIO68dTy6Lumv0bPy7SBdErYhU9SsbykES7GcSQpdpT5o5qcGmXqF12OiR'

    yag = yagmail.SMTP('npg.daily.motivator@gmail.com')

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

    contents = [
        
        "Witaj, \n"
        "Twoja złota myśl na dziś: \n",
        random_mysl,
        "\n"
        "Dzisiejsza wartość bitcoina to " + bitcoin,
        "A akcje Cd projekt red to $" + project_red_act_value + " czyli jest o $" + project_red_diff + " mniej od premiery Cyberpunk 2077 \n"
        "Smacznej Kawusi!"
    ]

    yagmail.SMTP('npg.daily.motivator@gmail.com').send('npg.daily.motivator@gmail.com', 'Twój daily motivator - '+ czas, contents)

    return

schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
