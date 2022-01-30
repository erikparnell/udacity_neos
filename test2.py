import database
import extract
import os

neos_csv = extract.load_neos(os.getcwd() + '/data/neos.csv')
cad_json = extract.load_approaches(os.getcwd() + '/data/cad.json')
database1 = database.NEODatabase(neos_csv, cad_json)
database1.print_csv()