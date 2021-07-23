import datetime

def obtener_fecha():
    fecha = datetime.date.today()
    fecha =str(fecha.year) +"-" + str(fecha.month) + "-" + str(fecha.day)
    return fecha

def altura_usuario(nombre):
    if nombre.lower() == "juan":
        return float(187)
    if nombre.lower()=="sandra":
        return float(150)

def calcular_ratio(nombre, cm_cintura):
    altura_cm = altura_usuario(nombre)
    cm_cintura = float(cm_cintura)
    ratio = float(cm_cintura/altura_cm)
    return round(ratio,3)

def obtener_todos_nombres(objeto):
    busquedas_completas = objeto.query.all()
    nombres = [busqueda_completa.nombre.lower() for busqueda_completa in busquedas_completas]
    return list(set(nombres))
