from twilio.rest import Client
import csv

client = Client('ACaeeb4d261f358211097773b1bfd6fbee', '9066958f8a3e49f3da71f725ae5c0401')

def my_message(address):
    return f"""Hello!
My name is Dylan. I was driving by your neighborhood and I saw a couple of houses that are exactly what I'm looking to buy. I was interested in making an all-cash offer on your house at {address}. I can close as quick as 2 weeks and you can leave the property as-is. If you're not ready to sell, please keep my contact and reach out when you are.

Do you know anyone in your neighborhood who is looking to sell their property?"""

with open('addresses.csv', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for number, address in reader:
        message = client.messages \
            .create(
            body=my_message(address),
            from_='+17193725128',
            to=f'+{number}'
            )
