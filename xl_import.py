#
# Created: 20170812
# Modified:20171011-
#
#
#
#
########################################################

import sys
import xlrd


def movie_load():
    xlpath = sys.path[0] + '\Movie_Library.xlsx'
    xldata = xlrd.open_workbook(xlpath)
    movie_xlsx = xldata.sheet_by_name('Sheet1')

    movie_data = {}
    excel_title = movie_xlsx.row_values(0)

    for i in range(1, len(movie_xlsx.col_values(0))):
        row_content = movie_xlsx.row_values(i)
        print row_content
        dict_data = dict(zip(excel_title, row_content))
        movie_data[i] = dict_data

    return movie_data
