import xlrd
from utils.general import General
from config.config import ConfigData

class Excel():

    # Get path of test data
    def get_test_data_path(self):
        self.general = General()
        self.config_data = ConfigData()
        path = str(self.general.get_directory_path())
        # full_path = path + self.config_data.TEST_DATA_PATH
        full_path = path + self.get_os_based_excel_path()
        return full_path

    # Get sheet name
    def get_sheet_name(self, sheet_name):
        path = self.get_test_data_path()
        workbook = xlrd.open_workbook(path)
        sheet = workbook.sheet_by_name(sheet_name)
        return sheet

    # get number of rows
    def get_row_count(self, sheet_name):
        row_count = sheet_name.nrows
        return row_count

    # get number of column
    def get_col_count(self, sheet_name):
        col_count = sheet_name.ncols
        return col_count

    # get excel path based on operating system
    def get_os_based_excel_path(self):
        os_name = self.general.get_operating_system_name()
        if os_name == "Windows":
            excel_path = self.config_data.TEST_DATA_PATH_WINDOWS
        elif os_name == "Mac":
            excel_path = self.config_data.TEST_DATA_PATH_MAC
        elif os_name == "Linux":
            excel_path = self.config_data.TEST_DATA_PATH_LINUX
        else:
            print("Support provided for MAc, Linux and Windows ")
        return excel_path

    # read test data from excel as a list of dictionaries
    def read_test_data(self, sheet_name):
        sheet = self.get_sheet_name(sheet_name)
        row_count = self.get_row_count(sheet)
        col_count = self.get_col_count(sheet)
        first_row = []  # The row where we stock the name of the column
        for col in range(col_count):
            first_row.append(sheet.cell_value(0, col))
        # transform the workbook to a list of dictionary
        data = []
        for row in range(1, row_count):
            elm = {}
            for col in range(col_count):
                elm[first_row[col]] = sheet.cell_value(row, col)
            data.append(elm)

        tc1 = []
        for i in range(len(data)):
            tc2 = []
            data_dict = data[i]
            for x in data_dict.values():
                tc2.append(x)
            tc1.append(tc2)

        return tc1



















