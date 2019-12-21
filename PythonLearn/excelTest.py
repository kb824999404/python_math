import xlrd
import xlwt


def write():
    file=xlwt.Workbook()        #新建excel文件
    table=file.add_sheet('sheet1',cell_overwrite_ok=True)
    table.write(0,0,2)      #载0行0列写入数据
    file.save('data/excelTest.xls')



def readXls():
    x=xlrd.open_workbook('data/carNum.xlsx')
    y=x.sheets()[0]
    carName=y.col_values(0)[1:]
    ID=y.col_values(1)[1:]
    money=y.col_values(2)[1:]
    num=y.col_values(3)[1:]
    data=[]
    for i in range(len(carName)):
        data.append([carName[i]]+[ID[i]]+[money[i]]+[num[i]])
    print(data)
    return data

def writeTXT(path,data):
    file=open(path,'w')
    for line in data:
        for item in line:
            file.write(str(item)+'\t')
        file.write('\n')
    file.close()


if __name__=='__main__':
    # write()
    data=readXls()
    writeTXT('data/carNum.txt',data)