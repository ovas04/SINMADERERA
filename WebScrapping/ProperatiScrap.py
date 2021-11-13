
from os import link
from sys import flags
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import urllib3
import pymysql
from config import obtener_nombre_base_datos


Meses = {'ENERO' : 1, 'FEBRERO' : 2,'MARZO' : 3,'ABRIL' : 4,'MAYO' : 5,'JUNIO' : 6,
          'JULIO' : 7,'AGOSTO' : 8,'SETIEMBRE' : 9,'OCTUBRE' : 10,'NOVIEMBRE' : 11,'DICIEMBRE' : 12  }


def obtener_conexion():
    return pymysql.connect(host="localhost",user="root",password="",db=obtener_nombre_base_datos())


class construccion:
    def __init__(self):
        self.pagina=""
        self.url = ""
        self.nombre = ""
        self.direccion = ""
        self.etapa = ""
        self.ubicacion = ""
        self.tipo_construccion = ""
        self.tipo_edificacion = "3"
        self.Area_Techada = ""
        self.Area_total = ""
        self.culminacion =""
        self.fecha_culminacion = ""
        self.estado = ""
        self.constructora = ""
        self.financiamiento = ""
        self.descripcion = ""
        self.comentario = ""

    def set_BaseInfo(self,p_pagina,p_url,p_nombre,p_direccion,p_ubicacion,p_tipo_construccion,p_constructora, p_descripcion):
        self.pagina = p_pagina
        self.url = p_url
        self.direccion = p_direccion
        self.nombre = p_nombre
        self.ubicacion = p_ubicacion
        self.tipo_construccion = p_tipo_construccion
        self.constructora = p_constructora
        self.descripcion = p_descripcion
        return

    def set_p_tipo_edificacion(self,p_tipo_edificacion):
        self.tipo_edificacion = p_tipo_edificacion    

    def set_area_techada(self,p_area_techada):
        self.Area_Techada = p_area_techada

    def set_area_total(self,p_area_total):
        self.Area_total = p_area_total

    def set_etapa(self,p_etapa):
        self.etapa = p_etapa
        
    def set_fecha_culminacion(self,p_culminacion):
        Year = p_culminacion.split(" ")[3]
        Month = p_culminacion.split(" ")[2].replace(",","").upper()
        Day = p_culminacion.split(" ")[0]
        today = date.today()
        flag=True
        if(int(Year)< today.year):
            flag =False
        elif(int(Year) == today.year):
            if(Meses[Month]<today.month):
                flag=False
            elif(Meses[Month]==today.month):
                if(Day < today.day):
                        flag=False
        if(flag):
            self.estado = 1 #Activa
        else:
            self.estado = 3 #Vencida
        self.fecha_culminacion = date(int(Year),Meses[Month],int(Day))
        self.culminacion = p_culminacion


    def fecha_culminacionProperati(self,Year,Month):
        if(Year != '' and Month != ''):
            today = date.today()
            flag=True
            if(int(Year)< today.year):
                flag =False
            elif(int(Year) == today.year):
                if(Meses[Month]<today.month):
                    flag=False
            if(flag):
                self.estado = 1 #Activa
            else:
                self.estado = 3 #Vencida
            self.fecha_culminacion = date(int(Year),Meses[Month],28)
            self.culminacion = Month + " , " + Year
        else:
            self.culminacion = "NO ENCONTRADA VERIFICAR EN ETAPA"
            self.fecha_culminacion = None
            self.estado = 4 #Duda
            if(self.etapa == "ENTREGA INMEDIATA"):
                self.estado = 3 #Vencida
        
    def set_financiamiento(self,p_financiamiento):
        self.financiamiento = p_financiamiento

    def get_pagina(self):
        return self.pagina
    def get_url(self):
        return self.url
    def get_nombre(self):
        return self.nombre
    def get_direccion(self):
        return self.direccion
    def get_etapa(self):
        return self.etapa
    def get_ubicacion(self):
        return self.ubicacion
    def get_tipo_construccion(self):
        return self.tipo_construccion
    def get_tipo_edificacion(self):
        return self.tipo_edificacion
    def get_Area_Techada(self):
        return self.Area_Techada
    def get_Area_total(self):
        return self.Area_total
    def get_culminacion(self):
        return self.culminacion
    def get_fecha_culminacion(self):
        return self.fecha_culminacion
    def get_estado(self):
        return self.estado
    def get_constructora(self):
        return self.constructora
    def get_financiamiento(self):
        return self.financiamiento
    def get_descripcion(self):
        return self.descripcion
    def get_comentario(self):
        return self.comentario



    def mostrar(self):
        print("Pagina : "+str(self.pagina))
        print("Url : "+str(self.url))
        print("Nombre : "+str(self.nombre))
        print("direccion : "+str(self.direccion))
        print("etapa : "+str(self.etapa))
        print("ubicacion : "+str(self.ubicacion))
        print("tipo_construccion : "+str(self.tipo_construccion))
        print("tipo_edificacion : "+str(self.tipo_edificacion))
        print("Area_Techada : "+str(self.Area_Techada))
        print("Area_total : "+str(self.Area_total))
        print("culminacion : "+str(self.culminacion))
        print("fecha_culminacion : "+str(self.fecha_culminacion))
        print("estado : "+str(self.estado))
        print("constructora : "+str(self.constructora))
        print("financiamiento : "+str(self.financiamiento))
        print("descripcion : "+str(self.descripcion))




#!https://stackoverflow.com/questions/36516183/what-should-i-use-to-open-a-url-instead-of-urlopen-in-urllib3
def DataProperati(_link):
    http = urllib3.PoolManager()
    _url = 'https://www.properati.com.pe'+str(_link)
    #html = urlopen(_url)
    response = http.request('GET', _url)
    ObBs = BeautifulSoup(response.data,'lxml') #html,"lxml"
    ConstruccionProperati = construccion()
    try:
        #-------------------------------------------------
        Oracion = ObBs.find('h1',{'class':"sc-fujyAs bTSNFO"}).get_text()
        Oracion = Oracion.split('·')
        v_nombre = Oracion[0].upper()
        try:
            v_direccion = Oracion[1].upper()
        except IndexError as e:
            v_direccion = "NO ENCONTRADO"
        #-------------------------------------------------------
        Encabezado = ObBs.find_all('span',{'class':'sc-bqGGPW eeFzyh'})
        v_ubicacion = Encabezado[2].get_text().upper()
        v_etapa =  Encabezado[1].get_text().upper()
        #--------------------------------------------------------
        try:
            Encabezado = ObBs.find('div',{'class':'StyledContentSeller-sc-1yzimq1-2 fDqWgA'})
            v_constructora= Encabezado.select('div > h2')[0].get_text(strip=True).upper()
        except AttributeError as e:
            v_constructora = "NO ENCONTRADA"
        #-------------------------------------------------------------------------------
        Encabezado = ObBs.find('div',{'class':'child-wrapper'})
        v_descripcion = Encabezado.get_text().upper()
    
        ConstruccionProperati.set_BaseInfo("PROPERATI",_url,v_nombre,v_direccion,
                                    v_ubicacion,"PRIVADA",v_constructora,
                                     v_descripcion)
        ConstruccionProperati.set_etapa(v_etapa)
        #--------------------------------------------------------------
        Encabezado = ObBs.find('div',{'class':'child-wrapper'})
        Encabezado = Encabezado.select('div > p')[0].get_text().split(" ")
        year=""
        month = ""
        for i in Encabezado:
            if(i in Meses):
                month = i
            if(i.isdigit() and int(i)>2000):
                year = i
        ConstruccionProperati.fecha_culminacionProperati(year,month)
        print("Exito")
    except:
        print("ERROR INTERNO")
    return ConstruccionProperati



ConstruccionProperati = []

url= 'https://www.properati.com.pe/proyectos-inmobiliarios/q/?page=1'
for i in range(1,7):
    _url = 'https://www.properati.com.pe/proyectos-inmobiliarios/q?page='+str(i)
    html = urlopen(_url)
    ObBs = BeautifulSoup(html,"lxml")
    Obj = ObBs.findAll("div",{"class":"StyledCard-n9541a-1 czKiDg"})
    for j in Obj:
       j=(j.select ('div > a ')[0])
       ConstruccionProperati.append(DataProperati(str(j.attrs['href'])))


conexion = obtener_conexion()
with conexion.cursor() as cur:
    for i in range(len(ConstruccionProperati)):
        cur.execute("call sp_autogenerar_id_const")
        id_const = cur.fetchall()
        cur.execute("call sp_registrar_const_priv(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (id_const,ConstruccionProperati[i].estado,'1',ConstruccionProperati[i].nombre,ConstruccionProperati[i].descripcion,
            ConstruccionProperati[i].fecha_culminacion,"USU-100000",ConstruccionProperati[i].pagina,ConstruccionProperati[i].url,
            ConstruccionProperati[i].tipo_edificacion,ConstruccionProperati[i].Area_total,ConstruccionProperati[i].Area_Techada,
            ConstruccionProperati[i].constructora,ConstruccionProperati[i].financiamiento,ConstruccionProperati[i].ubicacion,
            ConstruccionProperati[i].direccion,ConstruccionProperati[i].etapa))
        conexion.commit()
conexion.close()
print("Construcciones privadas registradas correctamente!")


"""for i in range(0,len(ConstruccionProperati)):
    print('='*50)
    ConstruccionProperati[i].mostrar()"""

