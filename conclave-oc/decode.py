from base64 import b64decode, decode


if __name__ == "__main__":

    protocol_encoded = open("/etc/config/protocol", "r").read()
    protocol_decoded = b64decode(protocol_encoded).decode()

    with open("/app/protocol.py", "w") as protocol_out:
        protocol_out.write(protocol_decoded)

    conf_encoded = open("/etc/config/conf", "r").read()
    conf_decoded = b64decode(conf_encoded).decode()

    with open("/app/conf.json", "w") as conf_out:
        conf_out.write(conf_decoded)

    in_conf_encoded = open("/etc/config/in_conf", "r").read()
    in_conf_decoded = b64decode(in_conf_encoded).decode()

    with open("/app/in-conf.json", "w") as in_conf_out:
        in_conf_out.write(in_conf_decoded)

    out_conf_encoded = open("/etc/config/out_conf", "r").read()
    out_conf_decoded = b64decode(out_conf_decoded).decode()

    with open("/app/out-conf.json", "w") as out_conf_out:
        out_conf_out.write(out_conf_decoded)
