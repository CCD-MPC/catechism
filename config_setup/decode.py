from base64 import b64decode


if __name__ == "__main__":

    print("\n\nDecoding protocol.\n\n")

    protocol_encoded = open("/etc/workflow/protocol", "r").read()
    protocol_decoded = b64decode(protocol_encoded).decode()

    with open("/data/protocol.py", "w") as protocol_out:
        protocol_out.write(protocol_decoded)

    in_conf_encoded = open("/etc/workflow/conf", "r").read()
    in_conf_decoded = b64decode(in_conf_encoded).decode()

    with open("/data/conf.json", "w") as in_conf_out:
        in_conf_out.write(in_conf_decoded)
