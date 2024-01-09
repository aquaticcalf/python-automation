import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime

def read_markdown_input(file_path):
    entries = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_entry = None

    for line in lines:
        line = line.strip()

        if line.startswith("#"):
            if current_entry:
                entries.append(current_entry)
            current_entry = {'url': line[1:].strip()}
        elif line.startswith("-"):
            parts = line[1:].split(":", 1)
            if len(parts) == 2:
                key = parts[0].strip().lower()
                value = parts[1].strip()
                current_entry[key] = value
            elif len(parts) == 1 and current_entry:
                current_entry[key] += " " + parts[0].strip()

    if current_entry:
        entries.append(current_entry)

    return entries


def generate_xml(entries):
    root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for entry in entries:
        url_element = ET.SubElement(root, "url")
        ET.SubElement(url_element, "loc").text = entry['url']
        if entry['lastmod']:
            ET.SubElement(url_element, "lastmod").text = entry['lastmod']
        if entry['changefreq']:
            ET.SubElement(url_element, "changefreq").text = entry['changefreq']
        if entry['priority']:
            ET.SubElement(url_element, "priority").text = entry['priority']

    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")

    with open("sitemap.xml", "w", encoding="utf-8") as xml_file:
        xml_file.write(xml_str)

def main():
    file_path = input("gimme path to the markdown file: ")
    entries = read_markdown_input(file_path)
    generate_xml(entries)
    print("sitemap generated successfully.")

if __name__ == "__main__":
    main()
