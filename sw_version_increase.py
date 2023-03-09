import re
import sys

def update_minor_ver():
    swv_pattern = re.compile(r"\S\S\.\S\S\.\S\S")
    bfv_pattern = re.compile(r"BugFixVersion = 0x\S\S")

    with open("./EB_tresos/templates/Application_Can/source/stubs/SWVersion.c", "r") as f:
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

    with open("./EB_tresos/templates/Application_Can/source/stubs/SWVersion.c", "w") as f:
        f.write(content)
    print("BugFixVersion updated.")

def update_major_ver():
    swv_pattern = re.compile(r"\S\S\.\S\S\.\S\S")
    bfv_pattern = re.compile(r"BugFixVersion = 0x\S\S")
    mswv_pattern = re.compile(r"MajorSWVersion = 0x\S\S")

    with open("./EB_tresos/templates/Application_Can/source/stubs/SWVersion.c", "r") as f:
        content = f.read()

    swv_match = re.search(swv_pattern, content).group()
    bfv_match = re.search(bfv_pattern, content).group()
    mswv_match = re.search(mswv_pattern, content).group()


    swv_list = swv_match.split(".")
    swv_list[1] = f"{int(swv_list[1], 16) + 1:02x}".upper()
    swv_list[-1] = f"00"
    swv_update = ".".join(swv_list)

    bfv_version = bfv_match[:-2]
    bfv_update = bfv_version + f"00"

    mswv_version = mswv_match[:-2]
    mswv_update = mswv_version + f"{int(mswv_match[-2:], 16) + 1:02x}".upper()

    content = content.replace(swv_match, swv_update)
    content = content.replace(bfv_match, bfv_update)
    content = content.replace(mswv_match, mswv_update)

    with open("./EB_tresos/templates/Application_Can/source/stubs/SWVersion.c", "w") as f:
        f.write(content)
    print("Major Version updated.")

if __name__ == "__main__":

    if sys.argv[-1] == "-m":
        update_major_ver()
    else:
        update_minor_ver()