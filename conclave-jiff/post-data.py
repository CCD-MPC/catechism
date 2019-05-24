import sys
import os
import operator
sys.path.append("/app/conclave-data/")

from conclave-data.swift import SwiftData
from conclave-data.dataverse import DataverseData

def post_swift_data(conf):
    """
    Store locally held data on Swift.
    """

    swift_cfg = conf["dest"]
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


def post_dataverse_data(conf):
    """
    Post output files to Dataverse.

    TODO: close connection?
    """

    input_dv_files = conf['source']['files']

    dv_conf = conf
    data_dir = "/data/"

    dv_data = DataverseData(dv_conf)

    for subdir, dirs, files in os.walk(data_dir):
        for file in files:
            print(file)
            if file[0] != '.':
                if file not in input_dv_files:
                    dv_data.put_data(data_dir, file)

