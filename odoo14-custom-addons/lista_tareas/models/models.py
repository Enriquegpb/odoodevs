# -*- coding: utf-8 -*-

from cgi import FieldStorage
from odoo import models, fields, api
import time
from datetime import datetime, date


#Definimos el modelo de datos
class lista_tareas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'
    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
    avatar=fields.Image('Imagen tarea',max_width=50,max_heigth=50)
    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    fecha = fields.Date()
    progreso=fields.Selection(
        String="Progreso",
        selection=[
            ('undone',"Sin Hacer"),
            ('progres',"haciendo"),
            ('done',"hecho"),
        ]

    )
    
    


    #Este computo depende de la variable prioridad
    @api.depends('prioridad')
    #Funcion para calcular el valor de urgente
    def _value_urgente(self):
        #Para cada registro
        for record in self:
            #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False
    
    
    



   



