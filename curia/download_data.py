import sys
import json
sys.path.append("/app/curia/")

from curia.swift import SwiftData
from curia.dataverse import DataverseData


def download_swift_data(c):
    """
    Download data from Swift to local filesystem.
    """

    swift_cfg = c["swift"]["source"]
    container = swift_cfg['data']['container_name']
    file = swift_cfg['data']['file_name']

    fname = ".".join(file.split(".")[:-1])
    pname = ".".join([fname, "json"])

    swift_data = SwiftData(swift_cfg)
    swift_data.get_data(container, file, "/data/", file)
    swift_data.get_data(container, pname, "/data/", "policy.json")

    swift_data.close_connection()


def download_dataverse_data(c):
    """
    Download files from Dataverse.

    TODO: close connection?
    """

    dv_cfg = c["dataverse"]["source"]

    file = dv_cfg['data']['file_name']
    fname = ".".join(file.split(".")[:-1])
    pname = ".".join([fname, "json"])

    dv_data = DataverseData(dv_cfg)
    dv_data.get_data(file, "/data/", file)
    dv_data.get_data(pname, "/data/", "policy.json")


if __name__ == "__main__":

    conf = open("/data/conf.json", 'r').read()
    cfg_json = json.loads(conf)

    if cfg_json["backends"]["data"] == "dataverse":

        dv_host = open("/etc/dataverse-auth/dv_host").read()
        dv_token = open("/etc/dataverse-auth/dv_token").read()
        cfg_json["dataverse"]["source"]["auth"]["host"] = dv_host
        cfg_json["dataverse"]["source"]["auth"]["token"] = dv_token

        download_dataverse_data(cfg_json)

    elif cfg_json["backends"]["data"] == "swift":
        auth_url = open("/etc/swift-auth/auth_url").read()
        username = open("/etc/swift-auth/username").read()
        password = open("/etc/swift-auth/password").read()
        cfg_json["swift"]["source"]["auth"]["osAuthUrl"] = auth_url
        cfg_json["swift"]["source"]["auth"]["username"] = username
        cfg_json["swift"]["source"]["auth"]["password"] = password

        download_swift_data(cfg_json)

    else:
        raise Exception("Backend not recognized: {} \n".format(c["backends"]["data"]))