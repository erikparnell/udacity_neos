"""Extract data on near-Earth objects and close approaches from CSV and
JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of
`NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON
file, formatted as described in the project instructions, into a
collection of `CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an
`NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
    near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_collection = []
    with open(neo_csv_path) as c:
        reader = csv.reader(c)
        next(reader)
        for row in reader:
            neo_obj = NearEarthObject(
                row[3],  # designation
                row[4],  # name
                row[15],  # diameter
                row[7]  # hazardous
            )
            neo_collection.append(neo_obj)
        return neo_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about
    close approaches.
    :return: A collection of `CloseApproach`es.
    """
    ca_collection = []
    with open(cad_json_path) as cad:
        cad_json = json.load(cad)
        cad_data = cad_json.get('data')
        for ca in cad_data:
            ca_obj = CloseApproach(
                ca[3],  # time
                ca[4],  # distance
                ca[7],  # velocity
                ca[0]  # designation
            )
            ca_collection.append(ca_obj)
    return ca_collection
