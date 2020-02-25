#!/usr/bin/env python
# coding: utf-8

# The test imports
#  This Framework is consists of Data requests from fmppub
#The requests data's are included with  Test_Parameters_press_release






import requests
import json
import jsonpath







# The  requests


url = "https://ftc-lbcmsmdb221:3601/fmppub/FMP_Send.pl"
request_data= {
    "postData":"PUB_ID,Org_Num,Dept,Pub_Type,Report_Name_Calc,Report_Date,Actual_Analyst_Name,Actual_MD_Name,Domain,Broad_code,Specific,PF_Sector,State,File_Type,Publish_Action_Code,Acrobat_Date,Language,Translation_of,New_Broad_Peer_Number_JL,New_Specific_Code_JL,sendNotification,cDocObjectId,cTransObjectId,cRelatedObjectId,Related_To,Archive_on_MDC,Office_Location\r\n \"0024\",\"195410\",\"Corporate\",\"Analysis\",\"FMP DEMO\",\"11/1/1993\",\"Adu, Peter\",\"Eckert, Glenn B\",\"Americas                                                                                                   UNITED STATES\",\"SECURITIES\",\"EXCHANGE & CLEARING HOUSES\",\"Airport\",\"\",\"PDF\",\"PUB\",\"6/15/1995\",\"Serbian\",\"\",\"12730\",\"\",\"YES\",\"PBC_0024\",\"\",\"\",\"\",\"No\",\"\"",
    "userId":"mcintya",
    "hashData":"14"
}


# The post


headers = {'content-type': 'text/plain; charset=utf-8'}
response = requests.post(url="https://ftc-lbcmsmdb221:3601/fmppub/FMP_Send.pl", params = {'postData' :'PUB_ID,Org_Num,Dept,Pub_Type,Report_Name_Calc,Report_Date,Actual_Analyst_Name,Actual_MD_Name,Domain,Broad_code,Specific,PF_Sector,State,File_Type,Publish_Action_Code,Acrobat_Date,Language,Translation_,of,New_Broad_Peer_Number_JL,New_Specific_Code_JL,sendNotification,cDocObjectId,cTransObjectId,cRelatedObjectId,Related_To,Archive_on_MDC,Office_Location \r\n "0024","195410","Corporate","Analysis","FMP DEMO","11/1/1993","Adu, Peter","Eckert, Glenn B","Americas                                                                                                   UNITED STATES","SECURITIES","EXCHANGE & CLEARING HOUSES","Airport","","PDF","PUB","6/15/1995","Serbian","","12730","","YES","PBC_0024","","","","No",""','userId':'mcintya','hashData':'14'},  headers=headers, verify=False)


print(response.text)

response2 = requests.get(url="https://ftc-lbcmsmdb221:3601/fmppub/api/v1/jobs/3", verify=False)

print(response2)
print(response2.text)





content=response2.content





print(content)





statuscode=response.status_code





print(statuscode)





json_data=json.loads(content)

print(json_data)

assert statuscode == 200
