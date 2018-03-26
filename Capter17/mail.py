from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp-mail.outlook.com'
POP3SVR = 'pop-mail.outlook.com'

origHdrs = ['From: chenpei47@outlook.com', 'To: chenpei47@outlook.com', 'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
sendSvr.login('chenpei47@outlook.com', 'zaqwsx123')
errs = sendSvr.sendmail('chenpei47@outlook.com', ('chenpei47@outlook.com',), origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('chenpei47@outlook.com')
recvSvr.pass_('zaqwsx123')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody

