import re
import sys
import pathlib
import itertools
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No input file specified")
        exit(1)
    
    input_s = sys.argv[1]

    tree = ET.parse(input_s)
    root = tree.getroot()

    root.findall(".//{*}Placemark")

    with open(pathlib.Path(input_s).with_suffix(".txt"), "w") as output_f:
        for placemark in root.findall(".//{*}Placemark"):
            coordtext = placemark.findtext(".//{*}coordinates")
            coordout = "|".join(itertools.chain.from_iterable(
                l.split(",") for l in re.findall(r"(?m)^\s*?(\S*?,\S*?)[,\s]", coordtext)))
            output_f.write(coordout + "   " + placemark.findtext("{*}name") + "\n")
