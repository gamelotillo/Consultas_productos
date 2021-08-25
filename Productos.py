import csv
'''Este modulo lee el reporte de los productos provisto por el Supermercado'''
row_file= []

with open('Productos.csv') as csvfile:
    for row in csvfile:
       row_file.append(row.split(','))
        




