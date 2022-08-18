from flask import Flask,render_template,request
from textblob import TextBlob
from datetime import datetime
#import emailAnalytics as Email
import nltk
import imaplib
import email
import pandas as pd
from bs4 import BeautifulSoup
app = Flask(__name__,template_folder='template')
@app.route('/')
def index():
return render_template('Home.html')
@app.route('/login',methods = ['POST'])
def login():
if request.method == 'POST':
user = request.form['username']
if user == "User":
return render_template('EmailAnalytics.html')
else:
return failure
@app.route('/analytics',methods = ['POST'])
def analytics():
if request.method == 'POST':
dat = request.get_json(force=True)
print(dat)
username = dat['email']
password = dat['pwd']
dmsrc = dat['dmsrc']
if dmsrc == "Gmail":
server='smtp.gmail.com'
port = 993

elif dmsrc == "Outlook":
port = 993
server='outlook.office365.com'
elif dmsrc == "Yahoo":
port = 993
server='imap.mail.yahoo.com'
#pwd = 'imbdwojdvhidpqcu'
elif dmsrc == "Zoho":
port = 993
server = 'imap.zoho.com'
elif dmsrc == "Aol":
port = 993
server = 'imap.aol.com'
#pwd = 'kyonvhqrsmkdgtge'
directory_from='Inbox'
df = download_email(server,port,directory_from,username,password)
if type(df) is str:
print(df)
return df
return df.to_json(orient='records')
else:
resp = {}
resp["data"] = "unsuccessful"
return resp

def download_email(server,port,directory_from,username,password):
print(server,port)
try:
mail = imaplib.IMAP4_SSL(server,port)
mail.login(username,password)
mail.select(directory_from)

email_arr=[]
domains =["@gmail.com","@outlook.com","@yahoo.com","@aol.com","@zoho.com"]
for i in domains:
print(i)
typ, msgs = mail.search(None, 'FROM '+i)
print(msgs)
msgs = msgs[0].split()
for item in msgs:
resp, data = mail.fetch(item, "(RFC822)")
email_body = data[0][1].decode("utf-8")
m = email.message_from_string(email_body)
frm=m['From']
date=m['date']
subject=m['Subject']
text=''
modified_text=''
if m.is_multipart():
for part in m.get_payload():
if part.get_content_maintype()=='text':
html=part.get_payload(decode=True)
soup=BeautifulSoup(html,'html.parser')
text=soup.get_text()

else:

          htmltext=m.get_payload()
          soup=BeautifulSoup(htmltext,'html.parser')
          text=soup.get_text()

new_text=nltk.sent_tokenize(text)
sent_seen=set()
for sent in new_text:

if sent not in sent_seen:
modified_text+=sent
sent_seen.add(sent)
datetime_obj = date.split(" ")
datetime_obj = datetime_obj[0 : 5]
datetime_obj = " ".join(datetime_obj)
print(datetime_obj)
datestr=datetime_obj.split(',')
day=datestr[0]
datetime_obj=datetime.strptime(datestr[1],' %d %b %Y %H:%M:%S')
date=datetime.date(datetime_obj)
time=datetime.time(datetime_obj)
#modified_text=modified_text[37:]
blob=TextBlob(modified_text)
sentiment=blob.sentiment
email_sentiment=''
if sentiment.polarity > 0:
email_sentiment='Positive'
elif sentiment.polarity < 0:
email_sentiment='Negative'
else:
email_sentiment='Satisfactory'

email_row=[frm,day,str(date),str(time),subject,modified_text,email_sentiment]
email_arr.append(email_row)
except Exception as e:
print("Download Email returned error..("+str(e)+")")
return str(e)

EmailDF=pd.DataFrame(email_arr,columns=['From','Day','Date','Time','Subject','Content'
,'Sentiments'])
writer=pd.ExcelWriter('GmailEmail.xlsx')

EmailDF.to_excel(writer,sheet_name='Sheet1')
writer.save()
return EmailDF
if __name__ == '__main__':
app.run()
