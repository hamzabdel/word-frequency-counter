import string
import argparse

def picking_item(clothes, filename, outputname):
    matches = []

    with open(filename, 'r') as f:
        content = f.read()

    items = content.splitlines()

    for item in items:
        if clothes.lower() in item.lower():
            matches.append(item)

    with open(outputname, 'w') as f:
        if matches:
            f.write("Items found in search:\n" + "\n".join(matches))
        else:
            f.write("No items found in search\n")
def main():
    parser = argparse.ArgumentParser(description="Search for a item in file: ")
    parser.add_argument("clothes", type=str, help="What you are looking for in the file.")
    parser.add_argument("filename", type=str, help="The name of the file to search in.")
    parser.add_argument("outputname", type=str, help="The name of the output file to write in.")
    args = parser.parse_args()

    result = picking_item(args.clothes, args.filename, args.outputname)
    print("Items listed in file for output!")

if __name__ == "__main__":
    main()

