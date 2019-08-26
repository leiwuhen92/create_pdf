#coding:utf-8


import pdfkit

ACESS_PATH = '/opt/di/server/diserver/uiservice/app/report/'
HEADER_PATH =  '/opt/di/server/diserver/uiservice/app/report/header.html'
FOOTER_PATH =  '/opt/di/server/diserver/uiservice/app/report/footer.html'



triage_report_url = 'http://127.0.0.1:6543/report/triage_report.html?ticketid={ticketid}'

confg =pdfkit.configuration(wkhtmltopdf=r"/usr/local/bin/wkhtmltopdf")
options = {
    'page-size': 'A4',
    'encoding': "UTF-8",
    'header-html':HEADER_PATH,
    'footer-html':FOOTER_PATH,
    'allow':ACESS_PATH
    }
url = triage_report_url.format(ticketid="e038d4ccc48111e98e360050568eb224")
pdfkit.from_url(url,'ctdi.pdf',options=options,configuration=confg)

