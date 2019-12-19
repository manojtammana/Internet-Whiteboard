import smtplib

sender = 'technocratsg4@gmail.com'
receivers = ['tammanamanoj@gmail.com']

message = """From: INTERNET WHITEBOARD<technocratsg4@gmail.com>
To: To Person <technocratsg4@gmail.com>
Subject: Welcome to INTERNET WHITEBOARD

Thank you for signing up with us


"""

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('technocratsg4@gmail.com','9000074244')
server.sendmail(sender, receivers, message)
print ("Thanks for signing up, Check your mail for details")
