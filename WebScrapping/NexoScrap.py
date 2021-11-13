from sys import flags
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import pymysql
#from Maderera.ProperatiScrap import construccion
from config import obtener_nombre_base_datos

Meses = {'ENERO' : 1, 'FEBRERO' : 2,'MARZO' : 3,'ABRIL' : 4,'MAYO' : 5,'JUNIO' : 6,
          'JULIO' : 7,'AGOSTO' : 8,'SEPTIEMBRE' : 9,'OCTUBRE' : 10,'NOVIEMBRE' : 11,'DICIEMBRE' : 12  }


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
        self.tipo_edificacion = ""
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
                if(int(Day) < today.day):
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




def Data_Nexo(p_url,ObBs):
    _construcion = construccion()
    Obj = ObBs.findAll("li",{"class":"list-data-general"})
    nombre =  ObBs.find("h1",{"class":"Project-header-title"})
    nombre = nombre.get_text().upper()
    direccion = ObBs.find("p",{"class":"Project-header-address street"})
    direccion =direccion.get_text().upper()
    ubicacion = ObBs.find("p",{"class":"Project-header-address urb"})
    ubicacion =ubicacion.get_text().upper()
    ubicacion = ubicacion.split(" ")[2]
    constructora = ObBs.find("div",{"class":"Project-inmobiliaria__name"})
    constructora = constructora.select('div > h2')[0].get_text(strip=True)#.split("/n")[0].upper()
    #descripcion = ObBs.find("div",{"Project-content-description"})
    #descripcion =descripcion.get_text().upper()
    #descripcion=descripcion.lstrip().replace("/n"," ")

    _construcion.set_BaseInfo("NEXOINMOBILIARIO",p_url,nombre,direccion,ubicacion,"PRIVADA",constructora,"")
    contador = 0
    
    for i in Obj:
        if (contador == 0):
            tipo_edificacion = i.select('li > div')[1].get_text(strip=True).upper()
            _construcion.set_p_tipo_edificacion(tipo_edificacion)
        elif (contador == 1):
            area_techada = i.select('li > div')[1].get_text(strip=True).upper()
            _construcion.set_area_techada(area_techada)
        elif (contador == 2):
            area_total = i.select('li > div')[1].get_text(strip=True).upper()
            _construcion.set_area_total(area_total)
        elif (contador == 5):
            Etapa = i.select('li > div')[1].get_text(strip=True).upper()
            _construcion.set_etapa(Etapa)
        elif (contador == 6):
            fecha_culminacion = i.select('li > div')[1].get_text(strip=True)
            _construcion.set_fecha_culminacion(fecha_culminacion)
        elif (contador == 7):
            financiamiento = i.select('li > div')[1].get_text(strip=True).upper()
            _construcion.set_financiamiento(financiamiento)
        contador+=1

    return _construcion

    
    


ConstruccionesNexo = []
for i in range(1823,1850):
    _url=("https://nexoinmobiliario.pe/proyecto/venta-de-dasdepartamento-"+str(i))
    req = Request(_url, headers={'User-Agent': '  Mozilla/5.0'})
    html = urlopen(req).read()
    ObBs =  BeautifulSoup(html,"lxml")
    title = ObBs.find("title")
    if(not (title.get_text() == "Nexo Inmobiliario - Departamentos, lotes, casas y oficinas en venta")):
        ConstruccionesNexo.append(Data_Nexo(_url,ObBs))
        print(i)
    #html = urlopen("https://nexoinmobiliario.pe/proyecto/venta-de-dasdepartamento-"+str(i))


'''
print("/"*120)
print(len(ConstruccionesNexo))
'''

conexion = obtener_conexion()
with conexion.cursor() as cur:
    for i in range(len(ConstruccionesNexo)):
        cur.execute("call sp_autogenerar_id_const")
        id_const = cur.fetchall()
        cur.execute("call sp_registrar_const_priv(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (id_const,ConstruccionesNexo[i].estado,"1",ConstruccionesNexo[i].nombre,ConstruccionesNexo[i].descripcion,
            ConstruccionesNexo[i].fecha_culminacion,"USU-100000",ConstruccionesNexo[i].pagina,ConstruccionesNexo[i].url,
            ConstruccionesNexo[i].tipo_edificacion,ConstruccionesNexo[i].area_total,ConstruccionesNexo[i].Area_Techada,
            ConstruccionesNexo[i].constructora,ConstruccionesNexo[i].financiamiento,ConstruccionesNexo[i].ubicacion,
            ConstruccionesNexo[i].direccion,ConstruccionesNexo[i].etapa))
        conexion.commit()
conexion.close()
print("Construcciones privadas registradas correctamente!")


"""for i in range(len(ConstruccionesNexo)):
    print(ConstruccionesNexo[i].pagina)
    print(ConstruccionesNexo[i].url)
    print(ConstruccionesNexo[i].nombre)
    print(ConstruccionesNexo[i].direccion)
    print(ConstruccionesNexo[i].etapa)
    print(ConstruccionesNexo[i].ubicacion)
    print(ConstruccionesNexo[i].tipo_construccion)
    print(ConstruccionesNexo[i].tipo_edificacion)
    print("="*60)"""


"""for i in range(0,len(ConstruccionesNexo)):
    print('='*50)
    ConstruccionesNexo[i].mostrar()"""
