import xlrd

class fileoperate():

    def read_xls(path,sheetnum=0):
        workbook=xlrd.open_workbook(path)
        sheet_list=workbook.sheets()
        sheet=workbook.sheet_by_index(sheetnum)
        rows=sheet.nrows
        cols=sheet.ncols
        list=[]
        i=0

        for i in range(rows):
            line=[]
            j=0
            for j in range(cols):
                line.append(sheet.cell_value(i,j))
            list.append(line)

        # print(len(list))
        # i=0
        # for i in range(len(list)):
        #     print()
        #     j=0
        #     for j in range(len(list[i])):
        #         print (list[i][j],end="")

        return list

if __name__=="__main__":
    t=fileoperate
    t.read_xls(r"C:\Users\colli\PycharmProjects\pythonPinPin\resources\parameter.xlsx",0)
