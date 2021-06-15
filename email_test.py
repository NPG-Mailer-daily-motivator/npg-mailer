import yagmail
import schedule
import time


def job():
    czas = str(time.strftime("%Y-%m-%d", time.localtime()))

    yag = yagmail.SMTP('npg.daily.motivator@gmail.com')

    contents = [

        "Witaj, \n"

        "Smacznej Kawusi!"
    ]

    yagmail.SMTP('npg.daily.motivator@gmail.com').send('npg.daily.motivator@gmail.com',
                                                       'Twój daily motivator - ' + czas, contents)

    return


schedule.every(20).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
