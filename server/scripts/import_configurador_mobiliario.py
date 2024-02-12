import csv
from server.models import ConfiguradorMobiliario

def import_configurador_mobiliario_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            configurador = ConfiguradorMobiliario(
                CodigoFamilia=row[0],
                CodigoSubfamilia=row[1],
                NombrePantalla=row[2],
                NombreOpcion1=row[3],
                Opcion1=row[4],
                NombreOpcion2=row[5],
                Opcion2=row[6],
                ColumnaPrecio=int(row[7]),
                NombreOpcion3=row[8],
                Opcion3=row[9],
                NombreOpcion4=row[10],
                Opcion4=row[11],
                NombreOpcion5=row[12],
                Opcion5=row[13],
                NombreOpcion6=row[14],
                Opcion6=row[15],
                NombreOpcion7=row[16],
                Opcion7=row[17],
                NombreOpcion8=row[18],
                Opcion8=row[19],
                NombreOpcion9=row[20],
                Opcion9=row[21],
                NombreAncho=row[22],
                OpcionAncho=row[23],
                NombreFondo=row[24],
                OpcionFondo=row[25],
                NombreAlto=row[26],
                OpcionAlto=row[27],
                NombreInterior=row[28],
                OpcionInterior=row[29],
                NombreOpcion10=row[30],
                Opcion10=row[31]
            )
            configurador.save()

# Provide the path to your CSV file
csv_file_path = '/Users/juanclusellas/Documents/NOFER/CONFIGURADOR/JSON/ConfiguradorMobiliario.csv'
import_configurador_mobiliario_from_csv(csv_file_path)
