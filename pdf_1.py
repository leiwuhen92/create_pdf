#coding:utf-8

import pdfkit

url = "https://10.21.144.110:8443/#/dashboard"

confg =pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

#pdfkit.from_url(url,'url.pdf',configuration=confg)
pdfkit.from_file('百度.html', '百度.pdf',configuration=confg)


html='''
        <div>
            <h1>title</h1>
            <p>content</p>
        </div>'''
#pdfkit.from_string(html,'string.pdf',configuration=confg)


