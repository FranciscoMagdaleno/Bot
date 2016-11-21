
import requests
import json
import smtplib
 
fromaddr = raw_input('From: ')
toaddrs  = raw_input('To: ')

#Creando msg
url = 'http://es.wallapop.com/rest/items?kws=sony&_p=0&catIds=&lat=41.398077&lng=2.170432&minPrice=&maxPrice=&order=&dist='
limitPrice = 100
msg = ''
for paginaIndex in range(5):
    head = '------------ pagina ' +str(paginaIndex)+ ' ------------'
    url = url.replace('_p=0','_p='+str(paginaIndex))
    r = requests.get(url)    
    data = r.json()
    msg = msg + '\n' + head + '\n'
    x=len(data['items'])
    for i in range(x):
        title = data['items'][i]['title'].encode('utf8')
        auxTitle = title.lower()
        #print title
        description = data['items'][i]['description'].encode('utf8')
        #print description
        price = data['items'][i]['salePrice']
        #print price
        #print ''
        if ('sony' in auxTitle) and (price < limitPrice):
            msg = msg + '\n' + 'producto->' + str(title) + '\n' + 'descripcion->' + str(description) + '\n' + 'precio->' + str(price) + '\n' 

# Datos
username = fromaddr
password = raw_input('Contraseña: ')
 
# Enviando el correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
