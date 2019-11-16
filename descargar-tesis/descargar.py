#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  descargar.py
#  
#  Copyright 2019 Ness <ness@Baltazar>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
    import os
    import wget
    import requests
    import time
    from parsel import Selector
    from pymongo import MongoClient
    # pprint library is used to make the output look more pretty
    from pprint import pprint
    # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    client = MongoClient('localhost', 27017)
    db=client.crawlers
    # Issue the serverStatus command and print the results
    #serverStatusResult=db.command("serverStatus")
    #pprint(serverStatusResult)


    #----------------------------------------------------
    #----Esta parte ya puede encontrar un campo 

    #conteotesis = db.theses
    #salida = conteotesis.find_one()
    #print(salida) 
    #------------------------------------------------------
    #-----INTENTO PARA BAJAR EL LINK ADECUADO
    conteotesis = db.theses
    #PARA PROBAR UNO
    #x=conteotesis.find_one({},{"rawData.file":1, "_id":0})
    #PARA TODOS
    contador=1
    subcontador=0
    nb=int(input('desde que registro empezamos???'))
    f= open("logs.txt","w")
    for x in conteotesis.find({},{"rawData.file":1, "_id":0}):
     print(x)
     #------------------------------------------------------ Esta parte está chafa porque no maneja bien los diccionarios
     cadena = str(x)
     if cadena != "{'rawData': {}}":
      cadena=cadena.lstrip("{u'rawData': {u'file': u'")
      cadena=cadena.rsplit("/", 1)[0]
      if contador >=nb:   #este if es solo para poder empezar desde algun regitro en particular por si se rompe la$

       #f.write(arch)
       #----------------------------------------------------- Crawleamos un poco la diriección que ya está en mongo 
       response = requests.get(cadena)
       if response.status_code == 200:
        print('Success!')
        selector = Selector(response.text)
        # "response.txt" contain all web page content
        #print(response.content)
        href_links = selector.xpath('//frame/@src').getall()  #encuentra el link del pdf
        #------------------------------------------------------ construimos la dirección en donde debe estar guardado el
        print(cadena+'/'+href_links[1])
        # wget.download(cadena+'/'+href_links[1], '/home/ness/Tesis mate/pdfs/2019')
        subcontador=subcontador+1    #cuenta las descargas que lleva en el subciclo
        f.write("%d %d %s\n"% (contador,subcontador, cadena))  #Escribe un log de descarga
        print('\nse descargó el registro %d' % contador)
        #---------------------------------------------------------------- Esta parte sirve para darle un descanso a la con
        if subcontador == 200:
         print('Estamos en pausa')
         time.sleep(300)
         subcontador = 0
         print('Seguimos')
       elif response.status_code == 404:
        f.write("%d %s .......NO ENCONTRÓ URL..........\n" % (contador, cadena))
      else:
       f.write("%d %s ......SALTADO.......\n" % (contador, cadena))
      contador=contador+1
     elif cadena == "{'rawData': {}}":
      f.write("%d %s ......SALTADO.......\n" % (contador, cadena))
    f.close()




    #--------------------------------------- 
    #------Esta parte es la idea con el nombre pero no sirve
    #conteotesis = db.theses
    #for x in conteotesis.find({},{"rawData.file":1, "_id":0}):
     #print(x)

     #cadena = str(x)
     #longitud=len(cadena)
     #if longitud > 10:
                 #print('bien')
     #cadena=cadena.lstrip("{u'rawData': {u'file': u'")
     #cadena=cadena.rsplit('/', 1)[0]

     #base=os.path.basename(cadena)
     #cadena=cadena + '/' + base + '.pdf'
     #print(cadena)
    #print(lista)

     #wget.download(cadena, '/home/ness/Documents/Tesis mate/crawler-theses-master/pdfs')
     #print(' ')

    #print(conteotesis.find({},{"rawData.file":1, "_id":0}).count())

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))






