from io import StringIO
import csv

class MySelectQuery:
    '''
    :type param_1:{String}
    :rtype: [{string=>string}]
    '''
    reader = csv.reader('')
    field_names_list = []
    field_names_dict = {}

    def __init__(self,param_1):
        # print(param_1)
        # print("-----------------------------------------")
        csv_file = StringIO(param_1)
        self.reader = csv.reader(csv_file)
        # print(type(reader))
        self.field_names_list = next(self.reader)
        print(self.field_names_list)
        self.field_names_dict = { i:self.field_names_list[i] for i in range(0,len(self.field_names_list))}

        # csv_file = StringIO(param_1)
        # dict_file = csv.DictReader(csv_file)
        # for row in dict_file:
        #     print(dict(row))

    def where(self,column_name,criteria):
        # print(column_name,criteria)
        print("-----------------------------------------")
        # for row in self.reader:
        #     print(row)
        # print(self.field_names_dict)
        for key,value in self.field_names_dict.items():
            if value == column_name:
                index_category_selected = key
        for row in self.reader:
            if row[index_category_selected] == criteria:
                answer_list = []
                separator = ','
                answer_string = separator.join(row)
                print(type(answer_string))
                print("-----------------------------------------")
                answer_list.append(answer_string)
                print(answer_list)
                return answer_list


# class MySelectQuery():
#     def __init__(self,param_1):
#         import csv
#         self.param_1 = csv.reader(param_1.split('\n'), delimiter = ',')
#
#     def where(self, column_name, criteria):
#         cs = self.param_1
#         last = []
#         for row in cs:
#             if criteria in row:
#                 roow = ",".join(row)
#                 last.append(roow)
#                 # print(type(roow))
#                 return last










param_1 = "name,year_start,year_end,position,height,weight,birth_date,college\nAlaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24 1968',Duke University\nZaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7 1946',Iowa State University\nKareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16 1947','University of California, Los Angeles\nMahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9 1969',Louisiana State University"
column_name = "name"
criteria = "Alaa Abdelnaby"
obj = MySelectQuery(param_1)
obj.where(column_name,criteria)

# Input: "name" && "Andre Brown"
# Output: [["Alaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24 1968',Duke University"]]
