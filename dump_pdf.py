#!/usr/bin/env python
import getopt
import sys

from pdfrw import PdfReader

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def extract_form_fields(pdf_file_path):
    file_data = PdfReader(pdf_file_path)

    data = {}
    """Extracts the PDF form data into a python dictionary"""
    for page in file_data.pages:
        annotations = page[ANNOT_KEY]
        if not isinstance(annotations, type(None)):
            for annotation in annotations:
                if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                    if annotation[ANNOT_FIELD_KEY]:
                        key = annotation[ANNOT_FIELD_KEY][1:-1]
                        data[key] = ''

    return data


def write_to_file(data, filename='dump_contents.txt'):
    data_file = open(filename, 'w')
    data_file.write(str(format_dictionary(data)))
    data_file.close()


def format_dictionary(dict):
    if not dict:
        return ""
    total_elements = len(dict)
    formatted = "{\n"
    for element in dict:
        formatted += f'    "{element}": ""'
        total_elements -= 1
        if total_elements > 0:
            formatted += ','
        formatted += '\n'
    formatted += '}'
    return formatted


def main(argv):
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('dump_pdf.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('dump_pdf.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is ', inputfile)
    print('Output file is ', outputfile)

    if inputfile:
        fields = extract_form_fields(inputfile)
        if outputfile:
            # do something here
            write_to_file(fields, outputfile)
        else:
            # print(fields)
            print(format_dictionary(fields))
            write_to_file(fields)


if __name__ == "__main__":
    main(sys.argv[1:])
