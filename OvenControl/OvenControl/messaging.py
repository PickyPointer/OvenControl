#This file is used to send emails and/or texts to the group members. Alterations to who is emailed/texted will need to be made here. 
#Call the send_message() function to send a subject and message from any function as needed.
import smtplib

#Shared SrI email used to text and email message to the gorup
sender = 'srgangye@hotmail.com'
password='698gang!'

#Recipients
#textRecipients = ['7205323365@vtext.com','4058247640@tmomail.net','6509067150@tmomail.net'] #Sarah, Toby, Shimon
#emailRecipients = ['tobias.bothwell@colorado.edu', 'shimon.kolkowitz@colorado.edu','sarah.l.bromley@colorado.edu']

textRecipients = '4058247640@tmomail.net'
emailRecipients = 'tobias.bothwell@colorado.edu'


#Function to send emails and texts
def send_message(sendEmail, sendText, subject, message):
    
    #Open server
    server = smtplib.SMTP( "smtp.live.com", 587 )
    server.starttls()
    server.login(sender, password ) 

    #Construct message with header for subject
    message = 'Subject: %s\n\n%s' % (subject, message)   

    #Send email if sendEmail is true
    if sendEmail == True:
        server.sendmail( sender, emailRecipients, message )

    #Send texts if sendText is true
    if sendText == True:
        server.sendmail( sender, textRecipients, message )