from base64 import b64decode


if __name__ == "__main__":

	print("\n\nDecoding protocol for Policy Engine.\n\n")

	protocol_encoded = open("/etc/init-config/protocol_policy", "r").read()
	protocol_decoded = b64decode(protocol_encoded).decode()

	with open("/app/protocol_policy.py", "w") as protocol_out:
		protocol_out.write(protocol_decoded)

    # with open("/conf_vol/protocol_policy.py", "w") as policy_out:
    #     policy_out.write(protocol_decoded)
