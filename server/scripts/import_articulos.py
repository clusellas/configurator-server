import csv
from server.models import Articles


def import_articulos_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            articulo = Articles(
                CodigoEmpresa=int(row[0]),
                CodigoArticulo=row[1],
                DescripcionArticulo=row[2],
                Descripcion2Articulo=row[3],
                DescripcionLinea=row[4],
                ComentarioArticulo=row[5],
                MarcaProducto=row[6],
                CodigoAlternativo=row[7],
                CodigoAlternativo2=row[8],
                CodigoArticuloOferta=row[9],
                CodigoArancelario=row[10],
                CodigoProveedor=row[11],
                ReferenciaEdi=row[12],
                PublicarInternet=int(row[13]),
                TipoArticulo=row[14],
                Utilizado=int(row[15]),
                Temporada=row[16],
                CodigoFamilia=row[17],
                CodigoSubfamilia=row[18],
                CodigoProyecto=row[20],
                CodigoSeccion=row[21],
                CodigoDepartamento=row[22],
                CodigoDefinicion=row[23],
                Colores=int(row[24]) if row[24] else None,
                IvaIncluido=int(row[25]) if row[25] else None,
                PrecioCompra=float(row[26]),
                PrecioVenta=float(row[27]),
                PrecioVentaconIVA1=float(row[28]),
                PrecioVentaconIVA2=float(row[29]),
                PrecioVentaconIVA3=float(row[30]),
                PrecioVentasinIVA1=float(row[31]),
                PrecioVentasinIVA2=float(row[32]),
                PrecioVentasinIVA3=float(row[33]),
                PrecioOfertaconIVA=float(row[34]),
                PrecioOfertasinIVA=float(row[35]),
                PesoBrutoUnitario=float(row[36]),
                PesoNetoUnitario=float(row[37]),
                VolumenUnitario=float(row[38])
            )
            articulo.save()

# Provide the path to your CSV file
csv_file_path = '/Users/juanclusellas/Documents/NOFER/CONFIGURADOR/JSON/articulos.csv'
import_articulos_from_csv(csv_file_path)
