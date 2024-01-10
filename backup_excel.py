from azure.storage.filedatalake import DataLakeServiceClient
import pyodbc
import pandas as pd
import io

service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
    "https", "leapsurgebi"), credential="ar1apFEmU7ObhgDi8xwa658yyjCFjXvIxuZfBlSVjZNN627YgypuyrvCS0HyKY4+tCVG7saJGYDOXZStfEHE6Q==")
server = 'leapsurgebi.database.windows.net'
userid = 'ls'                                        
password = 'Leapsurge12#' 
key="UserID"
report_name='Sales Report Summary Recent'

fetched_values={
"lscode": "LS00000026" ,
"firm_code": "0001",
"batchId": "20230713131221",
"Tablename": "RC Sales Secondary",
"Container": "logosstaging",
"Subdirectory1":"MDMExcelDownloads",
"isprod": "0", #0-Staging, 1-Production, 2-UAT
"isSplit":"0", #0 or 1 - based on row count more than 10L rows 1 
"filter":"Custom1",
"dbName":"LS00000026_0001_Stage"
}

lscode=fetched_values['lscode']
company=fetched_values['firm_code']
tableName = fetched_values['Tablename']
dbname = fetched_values['dbName']
isProd = fetched_values['isprod']
isSplit = fetched_values['isSplit']
batchId = fetched_values['batchId']
filterColumnName=fetched_values['filter']
container=fetched_values['Container']
sub_dir=fetched_values['Subdirectory1']
colList=[]
count1 = 1

# Loading (.xlsx) file to blob code
def lsdbconn(server,userid,password,isprod):
     try:
        if isprod=="0":
            custdbcnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=LSMASTER;UID='+userid+';PWD='+password)
        else :
            custdbcnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=Leapsurgebi;UID='+userid+';PWD='+password)
     except Exception as cust:
        cust.args[0]
     finally: 
            return custdbcnxn

def upload_file_to_directory_bulk(container, directory,sub_dir,sub_dir2,table_name,file, contentdf):
    try:
        file_system_client = service_client.get_file_system_client(file_system=container)
        if file_system_client:
            file_system_client.create_directory(directory)
            directory_client = file_system_client.get_directory_client(directory)
            if directory_client:
                directory_client.create_sub_directory(sub_dir)
                subdirectory_client = directory_client.get_sub_directory_client(sub_dir)
                if subdirectory_client:
                    subdirectory_client.create_sub_directory(sub_dir2)
                    subdirectory2 = subdirectory_client.get_sub_directory_client(sub_dir2)
                    if subdirectory2:
                        subdirectory2.create_sub_directory(table_name)
                        table_Name=subdirectory2.get_sub_directory_client(table_name)
                        if table_Name:
                            file_client  = table_Name.create_file(file)
                            excel_data = contentdf.getvalue()
                            file_client.upload_data(excel_data, overwrite=True)
                            return 'Success'
                        else:
                            return table_name + ' table Not Found'
                    else:
                        return sub_dir2 + ' sub_Directory Not Found'
                else:
                    return sub_dir + ' sub_Directory Not Found'
            else:
                return directory + ' Directory Not Found'
        else:
            return container + ' Container Not Found'

    except Exception as e:
        print(e)
        return 'Something went wrong!'

# End of blob Code


def custdbconn(server,dbname1,userid,password,query):
     try:
        custdbcnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+dbname1+';UID='+userid+';PWD='+password)
     except Exception as cust:
        cust.args[0]     
     finally: 
            custcursor=custdbcnxn.cursor()
            result=(custcursor.execute(query))
            return result

colListQuery = f"Select String_Agg([Column_id],',') as colList, String_Agg([Column Name],',') as col_Name from LS_Custom_Columns where LSCode = '{lscode}' and LSFirmCode = '{company}' and [Table] = '{tableName}'"
No_Of_Rows = custdbconn(server,dbname,userid,password,colListQuery)
colList1 = No_Of_Rows.fetchone()


if isSplit == '1':
    lsDistValQuery = f"Select Distinct {filterColumnName} from LS_Additional_Values where LSCode = '{lscode}' and LSFirmCode = '{company}' and [Table] = '{tableName}'"
    filtercolumn = custdbconn(server,dbname,userid,password,lsDistValQuery)
    counting_No_of_rows=filtercolumn.fetchall()
    count1=len(counting_No_of_rows)


buffer = io.BytesIO()
for i in range(count1):
    fileName = batchId
    lsQuery =f"Select Top 10000 {colList1[0]} From LS_Additional_Values Where LSCode = '{lscode}' and LSFirmCode = '{company}' and [Table] = '{tableName}' "
    
    if isSplit == '1':
        lsQuery += f" And {filterColumnName} = '{counting_No_of_rows[i][0]}'"
        fileName += "_" + counting_No_of_rows[i][0]
      
    fileName += '.xlsx'
    tabledata = custdbconn(server,dbname,userid,password,lsQuery)
    table_data=tabledata.fetchall()

    column_name = colList1[1].split(',')
    data_list=[tuple(row) for row in table_data]
    data = pd.DataFrame(data_list ,columns=column_name)
    # buffer = io.BytesIO()
    writer = pd.ExcelWriter(buffer, engine='xlsxwriter') #path – Path where to save file.
    excel_data = data.to_excel(writer, index=False,sheet_name='sheet1') # sheet_name-->it is not manadatory whenever we have multiple pages in a single excel it requires
    writer.close()
    upload_file_to_directory_bulk(container,lscode,sub_dir,company,tableName,fileName,buffer)

lsFileName = fileName
lsPath = f"https://leapsurgebi.blob.core.windows.net/{container}/{lscode}/{sub_dir}/{company}/{tableName}/{lsFileName}"

lsTriggerQuery = f'''Update LS_Trigger Set [Message] = 'Your file is ready for downloading.', [Status] = 0,
[Button Name 1] = 'Download', [Button Value 1] = '{lsPath}' 
Where application_code = 'AP0004' And LSCode = '{lscode}' And firm_code = '{company}' And [Id] = '{batchId}' 
'''
conn=lsdbconn(server,userid,password,isProd)
crsr=conn.cursor()
crsr.execute(lsTriggerQuery)
crsr.commit()
crsr.close()
