import sys
sys.path.append("/app/conclave-data/")

from conclave-data.swift import SwiftData
from conclave-data.dataverse import DataverseData

def download_swift_data(conclave_config):
    """
    Download data from Swift to local filesystem.
    """

    swift_cfg = conclave_config.system_configs['swift'].source
    data_dir = conclave_config.input_path
    container = swift_cfg['data']['container_name']
    files = swift_cfg['data']['files']

    swift_data = SwiftData(swift_cfg)

    if files is not None:
        for file in files:
            swift_data.get_data(container, file, data_dir)

    swift_data.close_connection()

def download_dataverse_data(conclave_config):
    """
    Download files from Dataverse.

    TODO: close connection?
    """

    dv_conf = conclave_config.system_configs['dataverse']
    data_dir = conclave_config.input_path

    dv_data = DataverseData(dv_conf)
    dv_data.get_data(data_dir)
