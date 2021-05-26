import schedule                     #z tego jest job plus co jaki czas wysyłamy
import requests
from bs4 import BeautifulSoup       #oba do wyciągania danych ze strony


def job():

    #losowanie cytatu z pliku plus usunięcie go z listy

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


    #pobieranie wartości bitcoina i cdr ze stron

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
    project_red_17Sep_value = 109.00        #wartość z dnia przed premiery
    project_red_diff = str(project_red_17Sep_value - float(project_red_act_value))