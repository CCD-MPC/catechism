import sys
sys.path.append("/app/conclave-data/")

from conclave-data.swift import SwiftData
from conclave-data.dataverse import DataverseData

def download_swift_data(conf):
    """
    Download data from Swift to local filesystem.
    """

    swift_cfg = conf["source"]
    data_dir = "/data/"
    container = swift_cfg['data']['container_name']
    files = swift_cfg['data']['files']

    swift_data = SwiftData(swift_cfg)

    if files is not None:
        for file in files:
            swift_data.get_data(container, file, data_dir)

    swift_data.close_connection()

def download_dataverse_data(conf):
    """
    Download files from Dataverse.

    TODO: close connection?
    """

    dv_conf = conf["source"]
    data_dir = "/data/"

    dv_data = DataverseData(dv_conf)
    dv_data.get_data(data_dir)

def download_data(conf):

    if conf["source"]["name"] == "dataverse":
        download_dataverse_data(conf)
    elif conf["source"]["name"] == "swift":
        download_swift_data(conf)
    else:
        print("Backend not recognized: {} \n".format(conf["source"]["name"]))


if __name__ == "__main__":

    conf = open("/app/data-conf.json", 'r').read()
    download_data(conf)
