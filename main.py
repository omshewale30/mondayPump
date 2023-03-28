import smtplib
import datetime as dt


quotes_list=list(open("quotes.txt","r"))
cur=dt.datetime.now()
print(cur.weekday())
if cur.weekday()==0:
    my_email = "omhridha@gmail.com"
    password = "kwbfxlymkcqhdvkq"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="omshewale030@gmail.com",
                        msg=f"Subject:Monday Motivation \n\n {quotes_list[1]}"
    )
    connection.close()




