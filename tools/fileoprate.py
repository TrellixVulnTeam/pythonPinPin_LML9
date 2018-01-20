import xlrd

class fileoperate():

    def read_xls(path,sheetnum=0):
        workbook=xlrd.open_workbook(path)
        sheet_list=workbook.sheets()
        print (sheet_list)
        sheet=workbook.sheet_by_index(sheetnum)
        rows=sheet.nrows
        print (rows)
        cols=sheet.ncols
        print (cols)
        list=[]
        i=0

        for i in range(rows):
            line=[]
            j=0
            for j in range(cols):
                line.append(sheet.cell_value(i,j))
            list.append(line)

        return list

if __name__=="__main__":
    t=fileoperate
    t.read_xls(r"C:\Users\colli\PycharmProjects\pythonPinPin\resources\parameter.xlsx",0)
