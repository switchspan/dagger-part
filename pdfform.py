from pdfrw import PdfReader

# PDF form constants
ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


class PdfForm:
    """Base class which loads and manages PDF forms
    uses the pdfrw library and notes found here: https://akdux.com/python/2020/10/31/python-fill-pdf-files.html
    """
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

    def __extract_form_data(self, file_data):
        data = {}
        """Extracts the PDF form data into a python dictionary"""
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

        return data

    def __str__(self):
        return self.metadata
