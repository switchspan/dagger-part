from pdfform import PdfForm


class ICS213Form(PdfForm):
    """General Message Form (ICS 213)"""
    FIELD_MAPPING = {
        "1 Incident Name Optional": "incident_name",
        "2 To Name and Position": "to_name",
        "3 From Name and Position": "from_name",
        "4 Subject": "subject",
        "5 Date": "date",
        "6 Time": "time",
        "7 Message": "message_text",
        "8 Approved by Name": "approved_by_name",
        "Signature_19": "",
        "PositionTitle_13": "approved_by_position",
        "9 Reply": "reply_text",
        "10 Replied by Name": "replied_by_name",
        "PositionTitle_14": "replied_by_position",
        "Signature_20": "",
        "DateTime_14": "date_time"
    }

    incident_name = ''
    to_name = ''
    from_name = ''
    subject = ''
    date = ''
    time = ''
    message_text = ''
    approved_by_name = ''
    approved_by_position = ''
    reply_text = ''
    replied_by_name = ''
    replied_by_position = ''
    date_time = ''

    def __init__(self, pdf_file_path):
        super().__init__(pdf_file_path)


class NotableActivity:
    """Holds a notable activity for an ICS 214 activity log"""

    def __init__(self, datetime, activity, row):
        self.datetime = datetime
        self.activity = activity
        self.row = row


class Resource:
    """Holds a resource for an ICS 214 activity log"""

    def __init__(self, name, position, home_agency):
        self.name = name
        self.position = position
        self.home_agency = home_agency


# TODO: Keep mapping the fields below
class ICS214Form(PdfForm):
    """Activity Log (ICS 214)"""
    FIELD_MAPPING = {
        "1 Incident Name_19": "incident_name",
        "3 Name": "recorder_name",
        "4 ICS Position": "recorder_position",
        "5 Home Agency and Unit": "recorder_agency",
        "8 Prepared by Name": "prepared_by_name",
        "PositionTitle_15": "prepared_by_position",
        "Signature_21": "",
        "DateTime_15": "prepared_on_datetime",
        "1 Incident Name_20": "incident_name",
        "8 Prepared by Name_2": "prepared_by_name",
        "PositionTitle_16": "prepared_by_name2",
        "Signature_22": "",
        "DateTime_16": "prepared_on_datetime2"
    }

    # TODO: Add logic to track notable activity rows
    # TODO: Add code to update the resources assigned
    RESOURCE_FIELD_MAPPING = [
        (1, "NameRow1_3", "ICS PositionRow1", "Home Agency and UnitRow1"),
        (2, "NameRow2_3", "ICS PositionRow2", "Home Agency and UnitRow2"),
        (3, "NameRow3_3", "ICS PositionRow3", "Home Agency and UnitRow3"),
        (4, "NameRow4_3", "ICS PositionRow4", "Home Agency and UnitRow4"),
        (5, "NameRow5_3", "ICS PositionRow5", "Home Agency and UnitRow5"),
        (6, "NameRow6_3", "ICS PositionRow6", "Home Agency and UnitRow6"),
        (7, "NameRow7", "ICS PositionRow7", "Home Agency and UnitRow7"),
        (8, "NameRow8", "ICS PositionRow8", "Home Agency and UnitRow8")
    ]

    ACTIVITY_FIELD_MAPPING = [
        (1, "DateTimeRow1", "Notable ActivitiesRow1"),
        (2, "DateTimeRow2", "Notable ActivitiesRow2"),
        (3, "DateTimeRow3", "Notable ActivitiesRow3"),
        (4, "DateTimeRow4", "Notable ActivitiesRow4"),
        (5, "DateTimeRow5", "Notable ActivitiesRow5"),
        (6, "DateTimeRow6", "Notable ActivitiesRow6"),
        (7, "DateTimeRow7", "Notable ActivitiesRow7"),
        (8, "DateTimeRow8", "Notable ActivitiesRow8"),
        (9, "DateTimeRow9", "Notable ActivitiesRow9"),
        (10, "DateTimeRow10", "Notable ActivitiesRow10"),
        (11, "DateTimeRow11", "Notable ActivitiesRow11"),
        (12, "DateTimeRow12", "Notable ActivitiesRow12"),
        (13, "DateTimeRow13", "Notable ActivitiesRow13"),
        (14, "DateTimeRow14", "Notable ActivitiesRow14"),
        (15, "DateTimeRow15", "Notable ActivitiesRow15"),
        (16, "DateTimeRow16", "Notable ActivitiesRow16"),
        (17, "DateTimeRow17", "Notable ActivitiesRow17"),
        (18, "DateTimeRow18", "Notable ActivitiesRow18"),
        (19, "DateTimeRow19", "Notable ActivitiesRow19"),
        (20, "DateTimeRow20", "Notable ActivitiesRow20"),
        (21, "DateTimeRow21", "Notable ActivitiesRow21"),
        (22, "DateTimeRow22", "Notable ActivitiesRow22"),
        (23, "DateTimeRow23", "Notable ActivitiesRow23"),
        (24, "DateTimeRow24", "Notable ActivitiesRow24"),
        (25, "DateTimeRow1_2", "Notable ActivitiesRow1_2"),
        (26, "DateTimeRow2_2", "Notable ActivitiesRow2_2"),
        (27, "DateTimeRow3_2", "Notable ActivitiesRow3_2"),
        (28, "DateTimeRow4_2", "Notable ActivitiesRow4_2"),
        (29, "DateTimeRow5_2", "Notable ActivitiesRow5_2"),
        (30, "DateTimeRow6_2", "Notable ActivitiesRow6_2"),
        (31, "DateTimeRow7_2", "Notable ActivitiesRow7_2"),
        (32, "DateTimeRow8_2", "Notable ActivitiesRow8_2"),
        (33, "DateTimeRow9_2", "Notable ActivitiesRow9_2"),
        (34, "DateTimeRow10_2", "Notable ActivitiesRow10_2"),
        (35, "DateTimeRow11_2", "Notable ActivitiesRow11_2"),
        (36, "DateTimeRow12_2", "Notable ActivitiesRow12_2"),
        (37, "DateTimeRow13_2", "Notable ActivitiesRow13_2"),
        (38, "DateTimeRow14_2", "Notable ActivitiesRow14_2"),
        (39, "DateTimeRow15_2", "Notable ActivitiesRow15_2"),
        (40, "DateTimeRow16_2", "Notable ActivitiesRow16_2"),
        (41, "DateTimeRow17_2", "Notable ActivitiesRow17_2"),
        (42, "DateTimeRow18_2", "Notable ActivitiesRow18_2"),
        (43, "DateTimeRow19_2", "Notable ActivitiesRow19_2"),
        (44, "DateTimeRow20_2", "Notable ActivitiesRow20_2"),
        (45, "DateTimeRow21_2", "Notable ActivitiesRow21_2"),
        (46, "DateTimeRow22_2", "Notable ActivitiesRow22_2"),
        (47, "DateTimeRow23_2", "Notable ActivitiesRow23_2"),
        (48, "DateTimeRow24_2", "Notable ActivitiesRow24_2"),
        (49, "DateTimeRow25", "Notable ActivitiesRow25"),
        (50, "DateTimeRow26", "Notable ActivitiesRow26"),
        (51, "DateTimeRow27", "Notable ActivitiesRow27"),
        (52, "DateTimeRow28", "Notable ActivitiesRow28"),
        (53, "DateTimeRow29", "Notable ActivitiesRow29"),
        (54, "DateTimeRow30", "Notable ActivitiesRow30"),
        (55, "DateTimeRow31", "Notable ActivitiesRow31"),
        (56, "DateTimeRow32", "Notable ActivitiesRow32"),
        (57, "DateTimeRow33", "Notable ActivitiesRow33"),
        (58, "DateTimeRow34", "Notable ActivitiesRow34"),
        (59, "DateTimeRow35", "Notable ActivitiesRow35"),
        (60, "DateTimeRow36", "Notable ActivitiesRow36")
    ]

    MAX_RESOURCE_RECORDS = 8
    MAX_ACTIVITY_RECORDS = 60

    resources_assigned = []
    notable_activities = []

    def number_of_resources_assigned(self):
        return len(self.resources_assigned)

    def number_of_notable_activities(self):
        return len(self.notable_activities)
