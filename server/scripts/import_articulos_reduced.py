import csv
from server.models import Articles, Coleccion, Design, Ancho, Eje, DesignColeccion, LineaConfigurador, Opcion, Valor, \
    LineaOpcion
#exec(open('/Users/juanclusellas/PycharmProjects/serverconfigurator/server/scripts/import_articulos_reduced.py').read())
def import_from_csv_11(articles_path, lineas_path, values_path):
    with open(articles_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            if row[1][0] != '-' and row[5] == 'MUEBLE' and row[1][0:3] != 'DEC' and row[1][0:3] != 'CAR':
                cod = row[1].split('.')
                if cod[2] != 'CSS' and cod[2] != 'CCS':
                    print(row[1] + " fam: " + row[4])
                    design = Design.objects.get_or_create(code=cod[0][1:])
                    ancho = Ancho.objects.get_or_create(code=int(cod[1]))
                    eje = Eje.objects.get_or_create(code=cod[2])
                    coleccion = Coleccion.objects.get_or_create(code=cod[0][0])
                    designcolection = DesignColeccion.objects.get_or_create(coleccion=coleccion[0], design=design[0])

                    articulo = Articles.objects.get_or_create(
                        CodigoEmpresa=int(row[0]),
                        CodigoArticulo=row[1],
                        DescripcionArticulo=row[2],
                        CodigoFamilia=row[4],
                        CodigoSubfamilia=row[5],
                        coleccion=coleccion[0],
                        design=design[0],
                        design_coleccion=designcolection[0],
                        ancho=ancho[0],
                        eje=eje[0],
                        visible=False
                    )
                    articulo[0].save()
    with open(lineas_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            CodigoFamilia = row[0]
            CodigoSubfamilia = row[1]
            article = Articles.objects.filter(CodigoFamilia=CodigoFamilia, CodigoSubfamilia=CodigoSubfamilia).first()
            if article:
                linea_configurador = LineaConfigurador.objects.create(price=int(row[7]), standard=False,
                                                                      coleccion=article.coleccion)
                i = 0
                cont = 1
                while cont < 15:
                    if i == 4:
                        i += 1  # row[7] is price TODO MODIFY INPUT CSV
                    print("i = "+str(i))
                    print("order= "+str(cont)+" name= "+str(row[i + 3])+" value="+""+str(row[i + 4]))
                    if row[i + 3] and row[i + 3] != "":
                        opcion = Opcion.objects.get_or_create(orden=cont, name=row[i + 3])
                        print("ENTERR")
                        valor = Valor.objects.get_or_create(code=row[i + 4], description=row[i + 4])
                        opcion[0].valores.add(valor[0])
                        LineaOpcion.objects.create(linea=linea_configurador, opcion=opcion[0], valor=valor[0])
                        linea_configurador.opciones.add(opcion[0])
                    i += 2
                    cont += 1
                linea_configurador.save()
    with open(values_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            print(row[1] + " code: " + row[2])
            nombreOpcion = row[1]
            opciones = Opcion.objects.filter(name=nombreOpcion)
            for opcion in opciones:
                already_opt = opcion.valores.filter(code=row[2]).first()
                if already_opt:
                    already_opt.description = row[3]
                    already_opt.save()
                else:
                    valor = Valor.objects.get_or_create(code=row[2], description=row[3])
                    opcion.valores.add(valor[0])
    return

import_from_csv_11('/Users/juanclusellas/Documents/NOFER/CONFIGURADOR/JSON/articulos-reduced.csv', '/Users/juanclusellas/Documents/NOFER/CONFIGURADOR/JSON/ConfiguradorMobiliario.csv', '/Users/juanclusellas/Documents/NOFER/CONFIGURADOR/JSON/Colores.csv')
