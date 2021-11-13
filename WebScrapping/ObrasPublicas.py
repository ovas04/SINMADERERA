# -*- coding: utf-8 -*-
"""
Created on Sat May 15 07:12:07 2021

@author: OVAS
"""
from datetime import date
from datetime import datetime
import math


Departamentos = [
    'LIMA','TUMBES',
    'CALLAO','TACNA',
    'CUSCO','SAN MARTÍN','SAN MARTIN',
    'CUZCO','PIURA',
    'ARQUIPA','PASCO',
    'PUNO','MOQUEGUA',
    'HUÁNUCO','MADRE DE DIOS',
    'ICA','LORETO',
    'AYACUCHO','LAMBAYEQUE'
    'UCAYALI', 'JUNÍN','JUNIN',
    'HUANCAVELICA','CAJAMARCA',
    'APURÍMAC','ÁNCASH',
    'AMAZONAS'
    ]


#def obtener_conexion():
 #   return pymysql.connect(host="localhost",user="root",password="",db=obtener_nombre_base_datos())


class ObraPublica:
    def __init__(self):
        self.codigo_InfoObras = ""
        self.entidad = ""
        self.etapa = ""
        self.ubicacion = ""
        self.descripcion = ""
        self.tipo_construccion = "PUBLICA"
        self.Modalidad = ""
        self.Estado_Obra = ""
        self.Presupuesto = ""
        self.Fecha_Recuperacion =""
        self.estado = ""
        self.comentario = ""
    
    def Base_Info(self,codigo_InfoObras,entidad,descripcion,Modalidad,Estado_Obra,Presupuesto):
        fecha = date.today()
        self.codigo_InfoObras = codigo_InfoObras
        self.entidad = entidad
        self.ubicacion = self.EncontrarUbicacion(descripcion)
        self.descripcion =descripcion
        self.Modalidad =Modalidad
        self.Estado_Obra = Estado_Obra
        self.Presupuesto = Presupuesto
        self.Fecha_Recuperacion = fecha 
        self.estado = self.IdentificarEstado(Estado_Obra)
        
    def IdentificarEstado(self,Estado_Obra):
        Estado_Obra = Estado_Obra.upper()    
        if(Estado_Obra == "FINALIZADA"):
            return 2
        elif(Estado_Obra == "PARALIZADA"):
            return 2
        elif(Estado_Obra == "EN EJECUCI¢N"):
            return 1
        elif(Estado_Obra == "SIN EJECUCI¢N"):
            return 1

    def EncontrarUbicacion(self,descripcion):
        ubicacion = ""
        specialChars = ".,!" 
        for specialChar in specialChars:
            descripcion = descripcion.replace(specialChar, '')
        descripcion = descripcion.upper()   
        for i in Departamentos:
            if(i in descripcion):
                ubicacion=i
                break
        if(ubicacion == ""):
            ubicacion = "No Encontrada"
        return ubicacion
    
    def mostrar(self):
        print('='*60)
        print('Codigo_Info_Obras : ......',self.codigo_InfoObras)
        print('Entidad : ......',self.entidad)
        print('Etapa : ......',self.etapa)
        print('Ubicacion : ......',self.ubicacion)
        print('Descripcion : ......',self.descripcion)
        print('Tipo_construccion : ......',self.tipo_construccion)
        print('Estado_Obra : ......',self.Estado_Obra)
        print('Presupuesto : ......',self.Presupuesto)
        print('Fecha_Recuperacion : ......',self.Fecha_Recuperacion)
        print('Estado : ......',self.estado)
        print('Comentario : ......',self.comentario)
        print('='*60)

import pandas as pd

dataset = pd.read_excel('ObrasPublicas.xlsx')
dataset=dataset.drop(0,axis=0)

def FormarObrar(codigo_InfoObras,entidad,descripcion,Modalidad,Estado_Obra,Presupuesto):  
    ConstruccionPublica = ObraPublica()
    ConstruccionPublica.Base_Info(codigo_InfoObras,entidad,descripcion,Modalidad,Estado_Obra,Presupuesto)
    return ConstruccionPublica


Lista_ObrasPublicas = []

for row in dataset.iterrows():

    Lista_ObrasPublicas.append(FormarObrar(row[1]['C¢digo'],row[1]['Entidad'],row[1]['Descripci¢n de la obra'],
                                           row[1]['Modalidad de ejecuci¢n'],row[1]['Estado de la obra'],row[1]['Monto de inversi¢n']))

'''
conexion = obtener_conexion()    
with conexion.cursor() as cur:
    for i in range(len(Lista_ObrasPublicas)):
        cur.execute("call sp_autogenerar_id_const")
        id_const = cur.fetchall()
        cur.execute("call sp_registrar_const_pub(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (id_const,Lista_ObrasPublicas[i].estado,Lista_ObrasPublicas[i].ubicacion,
            "1",Lista_ObrasPublicas[i].descripcion,"USU-100000",Lista_ObrasPublicas[i].codigo_InfoObras,
            Lista_ObrasPublicas[i].entidad,Lista_ObrasPublicas[i].Modalidad,
            Lista_ObrasPublicas[i].Presupuesto,Lista_ObrasPublicas[i].Estado_Obra,))
        conexion.commit()
conexion.close()
print("Construcciones publicas registradas correctamente!")
'''


"""for i in range(465,467):
    print(Lista_ObrasPublicas[i].codigo_InfoObras)
    print(Lista_ObrasPublicas[i].entidad)
    print(Lista_ObrasPublicas[i].etapa)
    print(Lista_ObrasPublicas[i].Modalidad)
    print(Lista_ObrasPublicas[i].descripcion)
    print(Lista_ObrasPublicas[i].ubicacion)
    print(Lista_ObrasPublicas[i].tipo_construccion)
    print(Lista_ObrasPublicas[i].Estado_Obra)
    print(Lista_ObrasPublicas[i].Presupuesto)
    print(Lista_ObrasPublicas[i].estado)
    print(Lista_ObrasPublicas[i].comentario)
    print("="*60)"""

