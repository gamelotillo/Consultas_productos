import Productos as product 
import random
from colorama import Fore, Back, Style
import os

'''Variable global, proviene de la lectura del archivo provisto por el supermecado'''
list_products = product.row_file

''' Funcion para iniciar la aplicacion'''
def inicio(self):
    borrarPantalla()
    cont=0
    while cont<2000000000:
        print("\n Bienvenido a consultas de precios")
        print("\n Opciones")
        print("\n Presione (1) para ingresar en la aplicación")
        select=input("\n Presione (2) Para salir de la aplicación  ")
        if select=='1':
         ingresar()
        else:
            break
        break
        cont+=1    
''' Esta funcion permite ingresar las categorias, sin importar si es mayuscula o minuscula'''
'''Ademas verifica que la categoria que ingresa el usuario existe y que no la ingreso anteriormente'''

def ingresar():
    i=0
    producto = ' '
    ask_product=[]
    validacion=show_categorias()
    cont=0
    borrarPantalla()
    print ("\nCategorias existentes:  ")
    show_categorias()
    while i<=4:
        producto = input("\nIngrese la categoria del producto Producto a consultar:  ")
        while cont<100000:
            if producto.lower() in validacion:
                if not producto.lower() in ask_product:
                    ask_product.append(producto.lower())
                    break
                else:
                    producto = input("Ingrese una categoria no ingresada anteriormente:  ")
                      
            else:
                producto = input("\nEsta categoria no es existe, vuelva a ingresar una categoria existente: ")

            cont+=1
        i+=1
    query_producto(ask_product)

'''Esta funcion permite ordenar unificar las categorias en un valor unico y ademas las ordena de forma alfabeticas'''
def show_categorias():
    no_repeat=[]
    show_categorias = []
    lower_categorias =[]
    qty_items = len(list_products)-1
    ini= 1
    category=[]

    for filas in list_products:
        if filas[2]!="Categoria":
            category.append(filas[2])

    no_repeat= set(category)
    show_categorias=sorted(no_repeat)
    
    for items in show_categorias:
        print("  ",items)
        lower_categorias.append(items.lower())

    
    return lower_categorias
                

'''Esta funcion agrupa todos los productos de una misma categoria para luego tomar de cada categoria un random'''
def query_producto(element):

    show_product = []
    qty_items = len(list_products)-1
    ini= 1
    category={}

    while ini<=qty_items:
            for items in list_products[ini]:
                 if items.lower() in element:
                     cat= category.keys()
                     if not items.lower() in cat:
                         category.setdefault(list_products[ini][2].lower(), [])
                         category[list_products[ini][2].lower()].append(list_products[ini])
                     else:
                         category[list_products[ini][2].lower()].append(list_products[ini])
                         
                    
            ini+=1
    
    for key, values in category.items():
        select_product = ''
        find_product = category[key]
        select_product = random.choice(find_product)
        show_product.append(select_product)
    
    pantalla(show_product)
   
'''Esta funcion muestra en pantalla los datos random obtenidos por categorias'''
def pantalla(show_product):
    cont=0
    borrarPantalla()
    for articulo in show_product:
        print("\nIdentificacion del producto:  ", articulo[0])
        print("Nombre del producto:  ", articulo[1])
        print("Categoria del producto:  ", articulo[2])
        print("Precio costo del producto:  ", articulo[3])
        print("Precio de Venta al publico:  ", articulo[4])
        print("Precio de Venta al mayor: ", articulo[4])
    
    
    consulta=input("\nPresione cualquier tecla para ingresar al menu principal:   ")
    inicio(consulta)

'''Esta funcion limpia la pantalla'''       
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")