import requests
import json

url = 'http://es.wallapop.com/rest/items?kws=sony&_p=0&catIds=&lat=41.398077&lng=2.170432&minPrice=&maxPrice=&order=&dist='

r = requests.get(url)
data = r.json()
x=len(data['items'])

'''Para la pagina 0'''

print '------------ Pagina 0 ------------'
for i in range(x):
    print 'producto->',data['items'][i]['title']
    print 'descripcion->',data['items'][i]['description']
    print 'precio->',data['items'][i]['salePrice']
    print ''
    
'''Para el resto de paginas'''

for paginaIndex in range(1,10):
    print '------------ Pagina '+str(paginaIndex)+' ------------'   
    url = url.replace('_p='+str(paginaIndex-1),'_p='+str(paginaIndex))
    r = requests.get(url)    
    data = r.json()
    x=len(data['items'])
    for i in range(x):
        print 'producto->',data['items'][i]['title']
        print 'descripcion->',data['items'][i]['description']
        print 'precio->',data['items'][i]['salePrice']
        print ''


    









