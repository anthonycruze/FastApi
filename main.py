from fastapi import FastAPI, Body

from pydantic import BaseModel

from typing import Optional, List

app = FastAPI()

class Clientes(BaseModel):
        id_cliente: int
        nombre_cliente: str
        mail_cliente: str
        tel_cliente: str
        dir_cliente: str

class Clientesupdate(BaseModel):
        nombre_cliente: str
        mail_cliente: str
        tel_cliente: str
        dir_cliente: str

class Usuarios(BaseModel):
        id_usuario: int
        nombre_usuario: str
        email: str
        telefono:str
        password:str
        tipo_nivel:str
        estatus:str
        registrado_por:str
class Usuariosupdate(BaseModel):
        nombre_usuario: str
        email: str
        telefono:str
        password:str
        tipo_nivel:str
        estatus:str
        registrado_por:str

class Equipos(BaseModel):
        id_equipo:int
        id_cliente:int
        tipo_equipo:str
        marca:str
        modelo:str
        num_serie:str
        fecha_ingreso:str
        observaciones:str
        estatus:str
        ultima_modificacion:str
        comentarios_tecnicos:str
        revision_tecnica_de:str
class Equiposupdate(BaseModel):
        id_cliente:int
        tipo_equipo:str
        marca:str
        modelo:str
        num_serie:str
        fecha_ingreso:str
        observaciones:str
        estatus:str
        ultima_modificacion:str
        comentarios_tecnicos:str
        revision_tecnica_de:str



clientes=[
    {
        "id_cliente": 1,
        "nombre_cliente":"trina sosa",
        "mail_cliente": "trina@ejemplo.com",
        "tel_cliente":"4587935",
        "dir_cliente":"avenida las palmas"
    },

    {
        "id_cliente": 2,
        "nombre_cliente":"trina sosa",
        "mail_cliente": "trina@ejemplo.com",
        "tel_cliente":"4587935",
        "dir_cliente":"avenida las palmas"
    }
]

usuarios=[
    {
        "id_usuario": 1,
        "nombre_usuario": "trina sosa",
        "email": "tri@gmail.com",
        "telefono": "68546211",
        "password": "123456",
        "tipo_nivel": "administrador",
        "estatus": "Activo",
        "registrado_por":"trina sosa"
    }
]

equipos=[
    {
        "id_equipo": 1,
        "id_cliente": 1,
        "tipo_equipo": "Laptop",
        "marca": "Apple",
        "modelo": "456547564",
        "num_serie": "uvd8546687",
        "fecha_ingreso":"13/05/2010",
        "observaciones":"no prende monitor",
        "estatus":"en revision",
        "ultima_modificacion":"trina sosa",
        "comentarios_tecnicos":"no prende no hay cable",
        "revision_tecnica_de":"no dejaron el cargador"

    }
]

app.title = "Mi primera aplicacion"

@app.get("/", tags=['Home'])
def home():
    return "hola mundo mi primer api"

@app.get("/clientes", tags=['cliente'])
def cliente() -> List[Clientes]:
    return clientes

@app.get("/usuarios", tags=['usuario'])
def usuario():
    return usuarios

@app.get("/equipos", tags=['equipo'])
def equipo():
    return equipos

@app.get("/clientes/{id_cliente}", tags=['Home'])
def get_cliente(id_cliente: int) -> Clientes:
    for cliente in clientes:
        if cliente["id_cliente"]== id_cliente:
            return cliente

@app.post("/clientes", tags=['cliente'])
def create_cliente(clientes: Clientes)->List[Clientes]:
    clientes.append(clientes.model_dump())
    return clientes

@app.post("/usuarios", tags=['usuario'])
def create_usuario(usuarios: Usuarios)->List[Usuarios]:
    usuarios.append(usuarios.model_dump())
    return usuarios
@app.post("/equipos", tags=['equipo'])
def create_equipo(equipos: Equipos)->List[Equipos]:
    equipos.append(equipos.model_dump())
    return equipos

@app.put("/clientes/{id_cliente}", tags=['cliente'])
def update_cliente(id_cliente:int, cliente: Clientesupdate)->List[Clientes]:
        for cli in clientes:
            if cli["id_cliente"]== id_cliente:
                
                cli["nombre_cliente"]=cliente.nombre_cliente,
                cli["mail_cliente"]=cliente.mail_cliente,
                cli["tel_cliente"]=cliente.tel_cliente,
                cli["dir_cliente"]=cliente.dir_cliente
                return cli
@app.delete("/clientes/{id_cliente}", tags=['cliente'])
def delete_cliente(id_cliente:int)->List[Clientes]:
    for cliente in clientes:
            if cliente["id_cliente"]== id_cliente:
                clientes.remove(cliente)
                return clientes

@app.put("/usuarios/{id_usuario}", tags=['usuario'])
def uptade_usuario(id_usuario: int, usuario: Usuariosupdate)->List[Usuarios]:
     for usu in usuarios:
          if usu["id_usuario"]== id_usuario:
               usu["nombre_usuario"]=usuario.nombre_usuario,
               usu["email"]=usuario.email,
               usu["telefono"]=usuario.telefono,
               usu["password"]=usuario.password,
               usu["tipo_nivel"]=usuario.tipo_nivel,
               usu["estatus"]=usuario.estatus,
               usu["registrado_por"]=usuario.registrado_por
               return usu
@app.delete("/usuarios/{id_usuario}", tags=['usuario'])
def delete_usuario(id_usuario: int)->List[Usuarios]:
     for usuario in usuarios:
          if usuario["id_usuario"]== id_usuario:
               usuarios.remove(usuario)
               return usuarios

@app.put("/equipos/{id_equipo}", tags=['equipo'])
def uptade_equipo(id_equipo:int, equipo: Equiposupdate)->List[Equipos]:
     for equi in equipos:
          if equi["id_equipo"]== id_equipo:
               equi["id_cliente"]=equipo.id_cliente,
               equi["tipo_equipo"]=equipo.tipo_equipo,
               equi["marca"]=equipo.marca,
               equi["modelo"]=equipo.modelo,
               equi["num_serie"]=equipo.num_serie,
               equi["fecha_ingreso"]=equipo.fecha_ingreso,
               equi["observaciones"]=equipo.observaciones,
               equi["estatus"]=equipo.estatus,
               equi["ultima_modificacion"]=equipo.ultima_modificacion,
               equi["comentarios_tecnicos"]=equipo.comentarios_tecnicos,
               equi["revision_tecnica_de"]=equipo.revision_tecnica_de
               return equi

@app.delete("/equipos/{id_equipo}", tags=['equipo'])
def delete_usuario(id_equipo:int)->List[Equipos]:
     for equipo in equipos:
          if equipo["id_equipo"]== id_equipo:
               equipos.remove(equipo)
               return equipos