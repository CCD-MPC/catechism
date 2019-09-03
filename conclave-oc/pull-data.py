import sys
import json
sys.path.append("/app/conclave_data/")

from conclave_data.swift import SwiftData
from conclave_data.dataverse import DataverseData


def download_swift_data(c):
    """
    Download data from Swift to local filesystem.
    """

    swift_cfg = c["source"]
    data_dir = "/data/"
    container = swift_cfg['data']['container_name']
    file = swift_cfg['data']['file_name']

    swift_data = SwiftData(swift_cfg)
    swift_data.get_data(container, file, data_dir)

    swift_data.close_connection()


def download_dataverse_data(c):
    """
    Download files from Dataverse.

    TODO: close connection?
    """

    dv_conf = c["source"]
    data_dir = "/data/"

    dv_data = DataverseData(dv_conf)
    dv_data.get_data(data_dir)


def download_data(c):

    if c["source"]["name"] == "dataverse":
        download_dataverse_data(c)
    elif c["source"]["name"] == "swift":
        download_swift_data(c)
    else:
        print("Backend not recognized: {} \n".format(c["source"]["name"]))


if __name__ == "__main__":

    conf = open("/app/in-conf.json", 'r').read()
    auth_url = open("/etc/swift-auth/auth_url").read()
    username = open("/etc/swift-auth/username").read()
    password = open("/etc/swift-auth/password").read()

    cfg_json = json.loads(conf)
    cfg_json["source"]["auth"]["osAuthUrl"] = auth_url
    cfg_json["source"]["auth"]["username"] = username
    cfg_json["source"]["auth"]["password"] = password
    download_data(cfg_json)
