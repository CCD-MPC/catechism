from base64 import b64decode


if __name__ == "__main__":

    print("\n\nDecoding protocol for Policy Engine.\n\n")

    protocol_encoded = open("/conf/workflow/protocol_policy", "r").read()
    protocol_decoded = b64decode(protocol_encoded).decode()

    with open("/app/protocol_policy.py", "w") as protocol_out:
        protocol_out.write(protocol_decoded)

    in_conf_encoded = open("/conf/workflow/conf", "r").read()
    in_conf_decoded = b64decode(in_conf_encoded).decode()

    with open("/app/in-conf.json", "w") as in_conf_out:
        in_conf_out.write(in_conf_decoded)
