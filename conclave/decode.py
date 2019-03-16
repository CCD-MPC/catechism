from base64 import b64decode


if __name__ == "__main__":

    protocol_encoded = open("/etc/config/protocol", "r").read()
    protocol_decoded = b64decode(protocol_encoded).decode()

    with open("/app/protocol.py", "w") as protocol_out:
        protocol_out.write(protocol_decoded)

    conf_encoded = open("/etc/config/conf", "r").read()
    conf_decoded = b64decode(conf_encoded).decode()

    with open("/app/conf.json", "w") as conf_out:
        conf_out.write(conf_decoded)