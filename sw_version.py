import re

swv_pattern = re.compile(r"\S\S\.\S\S\.\S\S")
bfv_pattern = re.compile(r"BugFixVersion = 0x\S\S")

with open("./SWVersion.c", "r") as f:
    content = f.read()

swv_match = re.search(swv_pattern, content).group()
bfv_match = re.search(bfv_pattern, content).group()


swv_list = swv_match.split(".")
swv_list[-1] = f"{int(swv_list[-1], 16) + 1:02x}".upper()
swv_update = ".".join(swv_list)

bfv_version = bfv_match[:-2]
bfv_update = bfv_version + f"{int(bfv_match[-2:], 16) + 1:02x}".upper()

content = content.replace(swv_match, swv_update)
content = content.replace(bfv_match, bfv_update)

with open("./SWVersion.c", "w") as f:
    f.write(content)