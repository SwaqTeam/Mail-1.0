# Mail-1.0
Open Source Mail API For Sending Custom Mail To Users.
## How to use the API
Send a post request to this endPoint: https://mail-v1.herokuapp.com/sendMail
Your data should be in JSON format
## JSON FORMAT
your json format should be like this having the following perameters
```json
{
	"sender_email" : "sender@domain.com",
	"reciever_email" : "receiver@domain.com",
	"host_password" : "123456",
	"email_subject" : "your email subject here",
	"message" : "your email message here",
	"smtp_server" : "domain.com",
	"smtp_port" : 465
}
```
## MUST KNOW
You must understand how SMTP works before you can use it.
Mail-1.0 only allow secure connection, SSL certified domain only will work.
## RECOMMENDATIONS
We recommend that you use custom domain mail server and not public email server such as gmail, yahoo, etc. there is tendency you will to have some issues with using them for security reasons.
## RESOURCEFUL LINKS
Learn how to setup custom domain email using cpanel: https://www.namecheap.com/support/knowledgebase/article.aspx/110/31/how-to-create-an-email-account-in-cpanel
How to configure SMTP Server: https://serversmtp.com/smtp-configuration/
