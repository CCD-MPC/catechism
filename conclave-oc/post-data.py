import sys
import os
import operator
import json

sys.path.append("/app/conclave_data/")
from conclave_data.swift import SwiftData
from conclave_data.dataverse import DataverseData


def post_swift_data(c):
    """
    Store locally held data on Swift.
    """

    swift_cfg = c["swift"]["dest"]
    data_dir = "/data/"
    container = swift_cfg['data']['container_name']

    swift_data = SwiftData(swift_cfg)

    all_files = {}

    for subdir, dirs, files in os.walk(data_dir):
        for file in files:
            if file[0] != '.':
                all_files[file] = os.path.getmtime("{0}/{1}".format(data_dir, file))

    # this is a hack to avoid writing all intermittent files to swift
    # it grabs the most recently modified file, which should be the output file,
    # since it is written to last
    output_file = max(all_files.items(), key=operator.itemgetter(1))[0]
    swift_data.put_data(container, output_file, data_dir)

    swift_data.close_connection()


def post_dataverse_data(c):
    """
    Post output files to Dataverse.

    TODO: close connection?
    """

    input_dv_files = c['source']['files']

    dv_conf = c
    data_dir = "/data/"

    dv_data = DataverseData(dv_conf)

    for subdir, dirs, files in os.walk(data_dir):
        for file in files:
            print(file)
            if file[0] != '.':
                if file not in input_dv_files:
                    dv_data.put_data(data_dir, file)


def post_data(c):

    data_backend = c["backends"]["data"]

    if data_backend == "dataverse":
        post_dataverse_data(c)
    elif data_backend == "swift":
        post_swift_data(c)
    else:
        raise Exception("Backend not recognized: {} \n".format(c["backends"]["data"]))


if __name__ == "__main__":

    conf = open("/app/conf.json", 'r').read()
    cfg_json = json.loads(conf)

    data_backend = cfg_json["backends"]["data"]

    if cfg_json[data_backend]["dest"]["pid"] == 1:
        post_data(cfg_json)

