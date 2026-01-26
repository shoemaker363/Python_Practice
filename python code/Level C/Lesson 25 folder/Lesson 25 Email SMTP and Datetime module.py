# import smtplib
# #! SMTP
# #! Make 2 new email accounts for this lesson.
 
# #?      smtplib module may give an error 'Connection unexpectedly closed'. 
# #?      Potential debug options:
# #*                      Make sure you have the correct smto address for you email provider.
# #//                                         Gmail: smtp.gmail.com
# #//                                         Hotmail: smtp.live.com
# #//                                         Yahoo: smtp.mail.yahoo.com
# #*                      Try changing Port to 587 if you get a 'TimeoutError'.
# #//                                         Example changing port: smtplib.SMTP("smtp.gmail.com", port=587)
# #*                      Steps to send email from Gmail address:
# #//                                         Step 1) go to https://myaccount.google.com/
# #//                                         Step 2) Select 'Security' tab, scroll dow to ' How you sign into Google.
# #//                                         Step 3) Click on 2 step verification and turn it on.
# #//                                         Step 4) Find App Passwords. (Can search for it in search bar.)
# #//                                         Step 5) Put in a name for your app.
# #//                                         Step 6) Copy the password generated.
# ##                                                      This is the only time you will ever see the password!
# #//                                         Step 7) Use copied Password in your Python code.

# email_one = "Email you are sending from."                                               ## 'email_one=': Your first practice email.
# password = "password for email you are sending email from"                              ## Try creating password here first before going throught the debugging steps.

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

#     connection.starttls()                                                               ## Secures the connection.

#     connection.login(user=email_one, password=password)

#     connection.sendmail(from_addr=email_one, to_addrs="Your email thats receiving",     ## 'to_addrs=': Your second practice email.
                        
#                         msg="Subject:Hello\n\nThe body of sent email")
#                             #* 'Subject': Puts the following part of the string into subject line of email.
#                             #* '\n\n': Put the following part of the string into the body of email.

# #! Datetime module

# import datetime as dt

# #$ Current:
# now = dt.datetime.now()                                                                     ## 'now' method: Retrieves current date and time.
# print(now)                                                                                  ## 'now": Class of datetime object.

# #$ Year:
# year = now.year                                                                             ## 'year': Retrieves year from 'now'.
# print(year)                                                                                 ## 'year': Class of integer.
# if year == 2026:
#     print("It's Dom's year to win!")

# #$ Month:
# month = now.month                                                                           ## 'month': Retrieves the month from 'now'.
# print(month)                                                                                ## 'month': Prints as integer, with JAN being 1 to DEC being 1.

# #$ Weekday:
# day_of_week = now.weekday()                                                                 ## 'weekday': Retrieves the day of week it is from 'now'.
# print(day_of_week)                                                                          ## 'weekday': Prints as integer, with Monday being 0 to Sunday being 6.

# #$ Creating a date and time:
# #?     Only required to add Year, Month, and Day.
# date_of_creation = dt.datetime(year=1900, month=2, day=5, hour=14, minute=27, second=54)
# print(date_of_creation)

# #! Motivational quotes sent on Mondays

# import smtplib
# import datetime as dt
# import random

# EMAIL = "Email you are sending from."
# PASSWORD_EMAIL = "password for email you are sending email from"

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 0:
#     with open("python code/Level C/Lesson 25 folder/motivation.txt") as file:
#         all_quotes = file.readlines()
#         quote = random.choice(all_quotes)

# #$ encoding quotes in order to send
#         clean_quote = quote.encode('ascii', 'ignore').decode('ascii')

#     print(quote)
#     print(clean_quote)
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(EMAIL, PASSWORD_EMAIL)
#         connection.sendmail(from_addr=EMAIL, 
#                             to_addrs="Your email thats receiving", 
#                             msg=f"Subject:Motivational quote\n\n{clean_quote}"
#                         )