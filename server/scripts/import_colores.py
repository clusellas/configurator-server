import csv
from server.models import Colors

def import_colores_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            colores = Colors(
                CodigoEmpresa=int(row[0]),
                NombreOpcion=row[1],
                CodigoColor=row[2],
                Color=row[3],
                IdColor=row[4] if row[4] else None,
                DescripcionWeb=row[5],
                Orden=int(row[6]),
                ColorFRA=row[7],
                ColorING=row[8],
                ColorITA=row[9],
                ColorPROV=row[10],
                CodigoColorAbreviado=row[11]
            )
            colores.save()

# Replace 'your_app' with the name of your Django app and provide the path to your CSV file

csv_file_path = '/Users/juanclusellas/Documents/NOFER/CONFIGURADOR/JSON/Colores.csv'
import_colores_from_csv(csv_file_path)