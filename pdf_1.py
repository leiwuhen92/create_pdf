#coding:utf-8

import pdfkit

url = "https://10.21.144.110:8443/#/dashboard"
options = {
                         'page-size': 'Letter',
                         'margin-top': '0.75in',
                         'margin-right': '0.75in',
                         'margin-bottom': '0.75in',
                         'margin-left': '0.75in',
                         'encoding': "UTF-8",
                         'no-outline': None
                    }

path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
confg = pdfkit.configuration(wkhtmltopdf=path_wk)


#pdfkit.from_url(url,'url.pdf',configuration=confg)
pdfkit.from_file('百度.html', '百度.pdf',configuration=confg,options=options)


html='''
        <div>
            <h1>title</h1>
            <p>content</p>
        </div>'''
#pdfkit.from_string(html,'string.pdf',configuration=confg)


