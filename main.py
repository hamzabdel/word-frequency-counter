import argparse
import json

def picking_item(clothes, filename, outputname):
    matches = []

    with open(filename, 'r') as f:
        data = json.load(f)

    items = data.get('items', [])

    for item in items:
        name = item.get('name', '')
        if clothes.lower() in name.lower():
            matches.append(item)

    with open(outputname, 'w') as f:
        if matches:
            json.dump(matches, f, indent=4)
        else:
            json.dump({"message": "No items found in search"}, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Search for an item in a JSON file and write results to another JSON file.")
    parser.add_argument("clothes", type=str, help="The type of clothes to search for in the file.")
    parser.add_argument("filename", type=str, help="The name of the JSON file to search in.")
    parser.add_argument("outputname", type=str, help="The name of the output JSON file to write results to.")
    args = parser.parse_args()

    picking_item(args.clothes, args.filename, args.outputname)
    print("Items listed in output file!")

if __name__ == "__main__":
    main()
