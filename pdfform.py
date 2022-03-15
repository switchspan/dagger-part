from pdfrw import PdfReader

from constants import *


class PdfForm:
    """Base class which loads and manages PDF forms
    uses the pdfrw library and notes found here: https://akdux.com/python/2020/10/31/python-fill-pdf-files.html
    """
    FIELD_MAPPING = {}
    metadata = {}

    def __init__(self, pdf_file_path):
        """Constructor for PdfForm"""
        self.metadata['pdf_file_path'] = pdf_file_path
        file_data = PdfReader(pdf_file_path)
        if isinstance(file_data.Info["/Author"], type(None)):
            raise Exception("Invalid PDF form file!")

        self.metadata["form_name"] = file_data.Info["/Title"][1:-1]
        self.metadata["author"] = file_data.Info["/Author"][1:-1]
        self.pdfReader = file_data
        # load in all of the fields to a dictionary
        self.data = self.__extract_form_data(file_data)
        self.__map_to_fields()

    def __extract_form_data(self, file_data):
        """Extracts the PDF form data into a python dictionary"""
        data = {}
        for page in file_data.pages:
            annotations = page[ANNOT_KEY]
            if not isinstance(annotations, type(None)):
                for annotation in annotations:
                    if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                        if annotation[ANNOT_FIELD_KEY]:
                            key = annotation[ANNOT_FIELD_KEY][1:-1]
                            val = annotation[ANNOT_VAL_KEY]
                            if val:
                                data[key] = val[1:-1]
                            else:
                                data[key] = ''

        return data

    def __map_to_fields(self):
        """Maps field data found in a dictionary from the PDF to properties on the class using the FIELD_MAPPING dictionary"""
        # print(str(self.FIELD_MAPPING))
        fields = {}
        if self.FIELD_MAPPING:
            if self.data:
                for key, val in self.FIELD_MAPPING.items():
                    if val:
                        fields[val] = self.data[key]
            self.__dict__.update(fields)

    def get_form_name(self):
        """Gets the form name from the metadata"""
        return self.metadata['form_name']

    def __str__(self):
        filepath = self.metadata['pdf_file_path']
        return f'PdfForm(\'{filepath}\')\r\n\tMetadata = {self.metadata}\r\n\tData = {self.data}'
