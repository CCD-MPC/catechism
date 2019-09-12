import sys
import os
import operator
import json

sys.path.append("/app/conclave_data/")
from curia.swift import SwiftData
from curia.dataverse import DataverseData


def post_swift_data(c):
    """
    Store locally held data on Swift.
    """

    swift_cfg = c["dest"]
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


def post_data(c):

    data_backend = c["backends"]["data"]

    if data_backend == "dataverse":
        # TODO: update this to DV code if we want to push to DV in the future.
        post_swift_data(c["swift"])
    elif data_backend == "swift":
        post_swift_data(c["swift"])
    else:
        raise Exception("Backend not recognized: {} \n".format(c["backends"]["data"]))


if __name__ == "__main__":

    conf = open("/data/conf.json", 'r').read()
    cfg_json = json.loads(conf)

    if cfg_json["user_config"]["pid"] == 1:
        post_data(cfg_json)

