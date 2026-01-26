from datetime import datetime
import pandas
import random
import smtplib

#!      Automatic Birthday Email

# TODO: Update the birthdays.csv with practice email.
# TODO: Check if today matches a birthday in the 'birthdays.csv'.
# TODO: Have a way to pick a random letter txt.
# TODO: Have '[NAME]' in letter.txt swapped for persons name.
# TODO: Send the email.

#* Solution starts on line 100.





















































































# EMAIL = "Your email"
# PASSWORD_EMAIL = "Your email password"

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("python projects/Level C projects/25 project folder/birthdays.csv")
# birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthday_dict:
#     birthday_person = birthday_dict[today_tuple]
#     file_path = f"python projects/Level C projects/25 project folder/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])

#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(EMAIL, PASSWORD_EMAIL)
#         connection.sendmail(
#             from_addr=EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )