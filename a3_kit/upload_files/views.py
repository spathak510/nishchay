import os
import time
import boto3
import tabula
import datetime
# import schedule
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection
from django.contrib import messages
# Create your views here.



def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    all_data = []
    for row in cursor.fetchall():
        data_row = dict(zip(columns, row))
        # data_row["Disbursal_date"] = data_row["Disbursal_date"].strftime('%d/%m/%Y')
        # data_row["Date_reported"] = data_row["Date_reported"].strftime('%d/%m/%Y')
        # data_row["bank_name"] = data_row["bank_name"]
        # data_row["deal_id"] = data_row["deal_id"]
        all_data.append(data_row)

    return all_data

def upload_statments(request):
    # print(request.session["lead_session"])
    
    if "lead_session" not in request.session:
        print("no")
    
    data=""
    data1=""
    if "lead_session"  in request.session:
        lead_id=request.session["lead_session"]
        print(lead_id)
        with connection.cursor() as cursor:
            sql_query = "SELECT SUM(case when type="+"'"+"bank"+"'"+ " THEN 1 ELSE 0 END) AS bank_count,name,lead_id,SUM(case when type="+ "'" +"itr"+"'"+" THEN 1 ELSE 0 END) AS itr_count FROM a3_kit.upload_file_details as tld where tld.lead_id LIKE " + "'%" + lead_id + "%'" + ";"
            cursor.execute(sql_query)
            data = dictfetchall(cursor)
            print(data)
        with connection.cursor() as cursor:
            # sql_query = "SELECT tld.lead_id,tld.name,SUM(case when type="+"'"+"bank"+"'"+ " THEN 1 ELSE 0 END) AS bank_count,SUM(case when type="+ "'" +"itr"+"'"+" THEN 1 ELSE 0 END) AS itr_count FROM a3_kit.test_leaddetails as tld Left join a3_kit.bank_statment_of_lead as bsl ON tld.lead_id=bsl.lead_id where tld.lead_id LIKE " + "'" + text + "%'" + "or" + " tld.name LIKE " + "'" + text + "%'" + ";"
            sql_query = "SELECT tld.lead_id,tld.name FROM a3_kit.los_lid_generation as tld where tld.lead_id LIKE " + "'%" + lead_id + "%'" + ";"
            cursor.execute(sql_query)
            data1 = dictfetchall(cursor)
            print(data1)

        with connection.cursor() as cursor:
            
            cursor.execute("select file_name, date from upload_file_details where lead_id = " + lead_id + ";") 
            data2 = dictfetchall(cursor)

    return render(request, 'upload_files.html',{'data' : data,'data1' : data1, 'data2':data2})

@login_required
def search_by_lead_name(request,text):
    if request.is_ajax() and request.method == "GET":
        text = text
        print(text)
        with connection.cursor() as cursor:
            # sql_query = "SELECT tld.lead_id,tld.name,SUM(case when type="+"'"+"bank"+"'"+ " THEN 1 ELSE 0 END) AS bank_count,SUM(case when type="+ "'" +"itr"+"'"+" THEN 1 ELSE 0 END) AS itr_count FROM a3_kit.test_leaddetails as tld Left join a3_kit.bank_statment_of_lead as bsl ON tld.lead_id=bsl.lead_id where tld.lead_id LIKE " + "'" + text + "%'" + "or" + " tld.name LIKE " + "'" + text + "%'" + ";"
            sql_query = "SELECT tld.lead_id,tld.name FROM a3_kit.los_lid_generation as tld where tld.lead_id LIKE " + "'" + text + "%'" + "or" + " tld.name LIKE " + "'" + text + "%'" + ";"
            cursor.execute(sql_query)
            data = dictfetchall(cursor)
            print(data)
            if not len(data):
                messages.info(request, "No results found!")
            else :
                return JsonResponse({"result":data})


@login_required
def get_count_by_lead_id_name(request):
    if request.is_ajax() and request.method == "POST":
        lead_id = request.POST.get('id')
        lead_name = request.POST.get('name')
        with connection.cursor() as cursor:
            sql_query = "SELECT SUM(case when type="+"'"+"bank"+"'"+ " THEN 1 ELSE 0 END) AS bank_count,SUM(case when type="+ "'" +"itr"+"'"+" THEN 1 ELSE 0 END) AS itr_count FROM a3_kit.upload_file_details as tld where tld.lead_id LIKE " + "'" + lead_id + "%'" + "and" + " tld.name LIKE " + "'" + lead_name + "%'" + ";"
            cursor.execute(sql_query)
            data = dictfetchall(cursor)
            data[0]["lead_id"] = lead_id
            data[0]["name"] = lead_name
            if not len(data):
                messages.info(request, "No results found!")
            else:
                return JsonResponse({"result": data})


def find_files(filename, search_path):
    file = search_path + "" + filename
    for root, dir, files in os.walk(search_path):
      if filename in files:
         os.remove(file)
      else:
          time.sleep(30)
          os.remove(file)




def cutFile(f):
    file_name = str(f.name)
    try:
        with open(file_name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        destination.close()
    except Exception as e:
        if e:
            file_name = e
    return file_name

@login_required
def uploadBankStatments(request):
    lead_id = request.POST.get('id')
    lead_name = request.POST.get('name')
    bank_count = request.POST.get('bank_count')
    print(bank_count)
    deleted_files = request.POST.get('deleted_file')
    if str(bank_count) == 'null' or str(bank_count) == 'None':
        bank_count = 0
    result = ''
    result_count = ''
    deleted_file = deleted_files.split(',')
    print(lead_id)
    if (len(request.FILES)>0):
        next_count = int(bank_count)+1
        for item in range(len(request.FILES)):
            uploaded_file = request.FILES['upload['+str(item)+']']
            print(uploaded_file)
            key = cutFile(uploaded_file)
            if key in deleted_file:
                continue;
            else:
                try:
                    s3_client = boto3.client('s3')
                    bucket = 'a3bank'
                    key = cutFile(uploaded_file)
                    s3_client.upload_file(key, bucket, lead_id + '_' + str(next_count) + '_' + key)
                    result = 'Bank File successfully uploaded.'
                    next_count += 1
                    file_name = key

                    with connection.cursor() as cursor:
                        sql_query = "INSERT INTO a3_kit.upload_file_details(lead_id, name, date, file_name,type ) VALUES("+ lead_id +",'"+ lead_name +"'" +", now() ,"+"'"+ file_name +"','"+"bank"+"'"+");"
                        cursor.execute(sql_query)
                    try:
                        file_path = "D:/prudhvi/Dev/a3-kit/a3_kit/"
                        find_files(file_name,file_path)
                    except Exception as e:
                        pass
                    with connection.cursor() as cursor:
                        sql_query = "SELECT SUM(case when type="+"'"+"bank"+"'"+ " THEN 1 ELSE 0 END) AS bank_count,SUM(case when type="+ "'" +"itr"+"'"+" THEN 1 ELSE 0 END) AS itr_count FROM a3_kit.upload_file_details as tld where tld.lead_id LIKE " + "'" + lead_id + "%'" + "and" + " tld.name LIKE " + "'" + lead_name + "%'" + ";"
                        cursor.execute(sql_query)
                        result_count = dictfetchall(cursor)
                except Exception as e:
                    result = e
                    print(result)
    return JsonResponse({"result":result,"count":result_count})


@login_required
def uploadITRStatments(request):
    lead_id = request.POST.get('id')
    lead_name = request.POST.get('name')
    itr_count = request.POST.get('itr_count')
    deleted_files = request.POST.get('deleted_file')
    print(str(itr_count))
    if str(itr_count) == 'None'  or str(itr_count) == 'null':
        itr_count = 0
    result = ''
    result_count = ''
    deleted_file = deleted_files.split(',')
    if (len(request.FILES)>0):
        next_count = int(itr_count)+1
        for item in range(len(request.FILES)):
            uploaded_file = request.FILES['upload['+str(item)+']']
            key = cutFile(uploaded_file)
            if key in deleted_file:
                continue;
            else:
                try:
                    s3_client = boto3.client('s3')
                    bucket = 'a3itr'
                    key = cutFile(uploaded_file)
                    s3_client.upload_file(key, bucket, lead_id + '_' + str(next_count) + '_' + key)
                    result = 'ITR File successfully uploaded.'
                    next_count += 1
                    file_name = key
                    with connection.cursor() as cursor:
                        sql_query = "INSERT INTO a3_kit.upload_file_details(lead_id, name, date, file_name,type ) VALUES("+ lead_id +",'"+ lead_name +"'" +", now() ,"+"'"+ file_name +"','"+"itr"+"'"+");"
                        cursor.execute(sql_query)
                    try:
                        file_path = r"D:\prudhvi\Dev\a3-kit\a3_kit\\"
                        find_files(file_name, file_path)
                    except Exception as e:
                        pass
                    with connection.cursor() as cursor:
                        sql_query = "SELECT SUM(case when type="+"'"+"bank"+"'"+ " THEN 1 ELSE 0 END) AS bank_count,SUM(case when type="+ "'" +"itr"+"'"+" THEN 1 ELSE 0 END) AS itr_count FROM a3_kit.upload_file_details as tld where tld.lead_id LIKE " + "'" + lead_id + "%'" + "and" + " tld.name LIKE " + "'" + lead_name + "%'" + ";"
                        cursor.execute(sql_query)
                        result_count = dictfetchall(cursor)
                except Exception as e:
                    result = e
                    print(result)
    return JsonResponse({"result":result,"count":result_count})



def download_statments(request):
    
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(file_name) as bank_upload , COUNT(distinct(lead_id)) as lead_id FROM upload_file_details WHERE type='bank';")
        count_bank=cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(file_name) as bank_upload , COUNT(distinct(lead_id)) as lead_id FROM upload_file_details WHERE type='itr';")
        count_itr=cursor.fetchall()
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT COUNT(file_name) as bank_upload FROM bank_statment_of_lead;")
    #     count_total=cursor.fetchall()
    count_total=int(count_bank[0][0]) + int(count_itr[0][0])
    print(count_total)
    print(count_bank[0][0])
    if( count_bank[0][1]>count_itr[0][1]):
        max1=count_bank[0][1]
    if( count_bank[0][1]<count_itr[0][1]):
        max1=count_itr[0][1]
    if( count_bank[0][1]==count_itr[0][1]):
        max1=count_itr[0][1]
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(file_name) as download,count(distinct(lead_id))   FROM downloaded_file_details where substring(file_name,-5,1)='b' ;")
        count_bank1=cursor.fetchall()
        print(count_bank1)
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(file_name) as download,count(distinct(lead_id))   FROM downloaded_file_details where substring(file_name,-5,1)='i' ;")
        count_itr1=cursor.fetchall()
    if( count_bank1[0][1]>count_itr1[0][1]):
        max2=count_bank1[0][1]
    if( count_bank1[0][1]<count_itr1[0][1]):
        max2=count_itr1[0][1]
    if( count_bank1[0][1]==count_itr1[0][1]):
        max2=count_itr1[0][1]
    
    count_total1=int(count_bank1[0][0]) + int(count_itr1[0][0])
    if "lead_session"  in request.session:
        lead_id=request.session["lead_session"]
        print(lead_id)
        print("xxx")
        with connection.cursor() as cursor:
            sql_query = "SELECT distinct(customer_id) ,lead_id,deal_id, name,bank,account_number FROM a3_kit.los_did_cid_generation  where lead_id=" + lead_id + ";"
            cursor.execute(sql_query)
            data = dictfetchall(cursor)
            print((data))
        with connection.cursor() as cursor:
            cursor.execute("SELECT distinct(cid),lid,did,name FROM a3_kit.customer_allocation where lid = " + lead_id + ";")
            customer_detail1=dictfetchall(cursor)
            print(customer_detail1)
            
            if not len(data):
                messages.info(request, "No results found!")
            else:
                with connection.cursor() as cursor:
                    sql_query = "SELECT COUNT(lead_id) AS count FROM a3_kit.downloaded_file_details  where lead_id=" + "'" + lead_id + "'" + ";"
                    cursor.execute(sql_query)
                    result_count = dictfetchall(cursor)
                    print(result_count)
               
                    return render(request, 'download_file.html', {'count_bank': count_bank,'count_itr' : count_itr,'max1' : max1, 'count_total' : count_total,'count_bank1' : count_bank1 ,'count_itr1' : count_itr1,'max2' : max2,'count_total1':count_total1,"result":data,"count":result_count,'data' : customer_detail1})

                 
    
 
    
               
    return render(request, 'download_file.html', {'count_bank': count_bank,'count_itr' : count_itr,'max1' : max1, 'count_total' : count_total,'count_bank1' : count_bank1 ,'count_itr1' : count_itr1,'max2' : max2,'count_total1':count_total1})



@login_required
def search_by_lead_name_for_download(request,text):
    if request.is_ajax() and request.method == "GET":
        text = text
        with connection.cursor() as cursor:
            sql_query = "SELECT tld.lead_id,tld.name FROM a3_kit.los_did_cid_generation as tld where tld.lead_id LIKE " + "'" + text + "%'" + "or" + " tld.name LIKE " + "'" + text + "%'" + ";"
            cursor.execute(sql_query)
            data = dictfetchall(cursor)
            if not len(data):
                messages.info(request, "No results found!")
            else :
                return JsonResponse({"result":data})


@login_required
def get_about_lead_id(request):
    if request.is_ajax() and request.method == "POST":
        lead_id = request.POST.get('id')
        print(lead_id)
        print("YYY")
        request.session["lead_session"] = lead_id
        # lead_name = request.POST.get('name')
        with connection.cursor() as cursor:
            sql_query = "SELECT distinct(customer_id) ,lead_id,deal_id, name,bank,account_number FROM a3_kit.los_did_cid_generation  where lead_id=" + lead_id + ";"
            cursor.execute(sql_query)
            data = dictfetchall(cursor)
            if not len(data):
                messages.info(request, "No results found!")
            else:
                with connection.cursor() as cursor:
                    sql_query = "SELECT COUNT(lead_id) AS count FROM a3_kit.downloaded_file_details  where lead_id=" + "'" + lead_id + "'" + ";"
                    cursor.execute(sql_query)
                    result_count = dictfetchall(cursor)

                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT dbs.lead_id, dbs.name,dbs.customer_id FROM a3_kit.los_did_cid_generation as dbs where dbs.lead_id=" + lead_id + ";")
                    cust_details = dictfetchall(cursor)

                with connection.cursor() as cursor:
                        cursor.execute("SELECT bank_name as sub_type,account_name as name,account_number as identifier from a3_kit.bank_bank as bk where deal_id=" + lead_id + " group by account_number;")
                        bank_updated_result = dictfetchall(cursor)

                with connection.cursor() as cursor:
                            cursor.execute("SELECT name,pan as identifier FROM a3_kit.itrv_itrv  where deal_id=" + lead_id + " group by pan ;")
                            itr_updated_result = dictfetchall(cursor)
                            print(itr_updated_result)


                list1=[]
                if len(bank_updated_result)>0:
                    for obj in bank_updated_result:
                        obj["doc_type"] = "BANK"
                        list1.append(obj)
                if len(itr_updated_result)>0:
                    for obj in itr_updated_result:
                        obj["doc_type"] = "ITR"
                        obj["sub_type"] = "ITR V"
                        list1.append(obj)
            # if len(form16_challans_updated_result)>0:
            #     for obj in form16_challans_updated_result:
            #         list1.append(obj)
                print(list1)
                
                return_data = list1

    

                return JsonResponse({"result":data,"count":result_count,"afterdownload":return_data,"cust_details":cust_details})





@login_required
def download_files_by_lead(request):
    if request.is_ajax() and request.method == "POST":
        lead_id = request.POST.get('id')
        print(lead_id)
        bucket = 'digitizedfiles'
        s3 = boto3.resource('s3')
        objects_bank = s3.Bucket(bucket).objects.filter(Prefix=lead_id)
        result = ''
        for obj in objects_bank:
            try:
                # file = r'd:\bank\{}'.format(obj.key)
                file_name = obj.key
                s3.Bucket(bucket).download_file(obj.key, r'D:\digitizedfiles\{}'.format(obj.key))  ###download file to bank folder
                # s3.Bucket(bucket).download_file(obj.key, '/home/ubuntu/digitizedfiles/{}'.format(obj.key))
                s3.Object(bucket, obj.key).delete()  ### delete downloaded file from AWS
                result = 'Successfuly download files!'
                with connection.cursor() as cursor:
                    sql_query = "INSERT INTO a3_kit.downloaded_file_details(lead_id, file_name, date) VALUES("+ lead_id +",'"+ file_name +"'" +", now() "+");"
                    cursor.execute(sql_query)
            except Exception as e:
                result = e
             
        # else:
        #     result = 'No Found, Please try again!'
        with connection.cursor() as cursor:
            sql_query = "SELECT COUNT(lead_id) AS count FROM a3_kit.downloaded_file_details  where lead_id=" + "'" + lead_id + "'" + ";"
            cursor.execute(sql_query)
            result_count = dictfetchall(cursor)
            
        return_data = addindatabasefromcsv(request)
        
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT dbs.lead_id, dbs.name,dbs.customer_id FROM a3_kit.los_did_cid_generation as dbs where dbs.lead_id=" + lead_id + ";")
            cust_details = dictfetchall(cursor)
          
    return JsonResponse({"result": result,"count":result_count,"afterdownload":return_data,"cust_details":cust_details})


import pandas as pd
import glob
import numpy as np


def addindatabasefromcsv(request):
    lid = request.POST.get('id')
    
    files = glob.glob(r'D:\digitizedfiles\\*')
    list1 = []
    bank_updated_result = ''
    itr_updated_result = ''
    form16_challans_updated_result = ''
    # print(files)
    for file in files:
        file2 = str(file).split('_')
        file1 = file2[len(file2) - 1][:1]

        if file1 == "b":
           
            # list = []


            reader = pd.read_csv(file)
            # list.append("BANK")
            # list.append(reader.iloc[0]['bank_name'])
            # list.append(reader.iloc[0]['Account Number'])
            # list.append(reader.iloc[0]['Account Name'])
            # list.append(reader.iloc[0]['customer_id'])


            reader['Txn Date'] = pd.to_datetime(reader['Txn Date'], format="%d/%m/%Y")
            reader['Txn Date'] = reader['Txn Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            # reader['Txn Date'] = reader['Txn Date'].astype('str')
            # reader.to_csv(r'D:\prudhvi\reader2.csv', index=False)
            reader = reader.replace(np.nan, 'NA')
            reader['creation_time'] = datetime.datetime.now()

            reader['last_modification_time'] = datetime.datetime.now()
            reader['image_name'] = "asmfbejhb"
            reader['customer_id'] = 0
            reader['created_by_id']=1

          
            for i in range(len(reader)):
                row = reader.iloc[i]
                print(row)
                print("XXXX")
              
                with connection.cursor() as cursor:
                    cursor.execute("insert into bank_bank(txn_date,description,cheque_number,debit,credit,balance,account_name,account_number,mode,entity,source_of_trans,sub_mode,transaction_type,bank_name,deal_id,creation_time,last_modification_time,image_name,customer_id,created_by_id) values(%s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s, %s,%s)", row)
            os.remove(file)

            with connection.cursor() as cursor:
                cursor.execute("SELECT bank_name as sub_type,account_name as name,account_number as identifier from a3_kit.bank_bank as bk where deal_id=" + lid + " group by account_number;")
                bank_updated_result = dictfetchall(cursor)

            # list1.append(bank_updated_result)
            continue;
        if file1 == "i":
            file3 = file2[1]
            file4 = file2[2]
            if file3 == "form16":
                if file4 == "challans":
                   
                    list = []
                    reader = pd.read_csv(file)
                    # list.append("ITR")
                    # list.append("FORM16_challans")
                    # list.append("PANno")
                    # list.append("raju")

                    reader['tax_deposited_date'] = pd.to_datetime(reader['tax_deposited_date'])
                    reader['tax_deposited_date'] = reader['tax_deposited_date'].apply(lambda x: x.strftime('%Y-%m-%d'))
                    reader['tax_deposited_date'] = reader['tax_deposited_date'].astype('str')
                    reader = reader.replace(np.nan, 'NA')
                    reader['creation_time'] = datetime.datetime.now()
                    reader['creation_time']  = reader['creation_time'].astype('str')
                    reader['last_modification_time'] = datetime.datetime.now()
                    reader['last_modification_time'] = reader['last_modification_time'].astype('str')
                    # for i in range(len(reader)):
                    #     row = reader.iloc[i]

                    #     print(i)
                    #     with connection.cursor() as cursor:
                    #         cursor.execute("insert into a3_kit.form16_challans(tax_deposited,bsr_code,tax_deposited_date,challan_serial_no,status_match_oltas,deal_id,customer_id,assessment_year,creation_time,last_modification_time) values(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)",row)
                    # list1.append(list)
                    # os.remove(file)
                    # with connection.cursor() as cursor:
                    #     cursor.execute(
                    #         "SELECT bank_name as sub_type,account_name as name,account_number as identifier from a3_kit.bank_bank where deal_id=" + lid + " group by account_number;")
                    #     form16_challans_updated_result = dictfetchall(cursor)
                    # continue;

                if file4 == "info":
                    print("info")
                if file4 == "partb":
                    print("partb")
                if file4 == "quarters":
                    print("quarters")
            if file3 == "form26as":
                if file4 == "asseseedetails":
                    print("asseseedetails")
                if file4 == "parta":
                    print("parta")
                if file4 == "partb":
                    print("partb")
                if file4 == "partc":
                    print("partc")
                if file4 == "partd":
                    print("partd")
                if file4 == "partg":
                    print("partg")
            if file3 == "itr":
                print("itr")
                # list = []
                reader = pd.read_csv(file)
                # list.append("ITR")
                # list.append("FORM V")
                # list.append("PANno")
                # list.append("raju")

                # reader['tax_deposited_date']=pd.to_datetime(reader['tax_deposited_date'])
                # reader['tax_deposited_date']=reader['tax_deposited_date'].apply(lambda x :x.strftime('%Y-%m-%d'))
                # reader['tax_deposited_date']=reader['tax_deposited_date'].astype('str')
                reader = reader.replace(np.nan, 'NA')
                reader['creation_time'] = datetime.datetime.now()
                reader['last_modification_time'] = datetime.datetime.now()

                for i in range(len(reader)):
                    row = reader.iloc[i]

            
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "insert into a3_kit.itrv_itrv(assessment_year,name,pan,town_city_district_state,pin_code,efiling_acknowledgement_number,form_no,date_of_itr_filed,gross_total_income,deductions_under_chapter_vi_a,total_income,total_income_deemed_total_income_under_amt_mat,total_income_current_year_loss,net_tax_payable,interest_and_fee_payable,total_tax_interest_and_fee_payable,taxes_paid_advance_tax,taxes_paid_tds,taxes_paid_tcs,taxes_paid_self_assessment_tax,taxes_paid_total_taxes_paid,tax_payable,refund,deal_id,customer_id,image_name,creation_time,last_modification_time) values(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s, %s, %s,%s, %s, %s,%s, %s)",
                            row)
                # list1.append(list)
                os.remove(file)
                with connection.cursor() as cursor:
                    cursor.execute("SELECT name,pan as identifier FROM a3_kit.itrv_itrv  where deal_id=" + lid + " group by pan ;")
                    itr_updated_result = dictfetchall(cursor)
                    print(itr_updated_result)
                # list1.append(itr_updated_result)
                continue;
    
    if len(bank_updated_result)>0:
        for obj in bank_updated_result:
            obj["doc_type"] = "BANK"
            list1.append(obj)
    if len(itr_updated_result)>0:
        for obj in itr_updated_result:
            obj["doc_type"] = "ITR"
            obj["sub_type"] = "ITR V"
            list1.append(obj)
    if len(form16_challans_updated_result)>0:
        for obj in form16_challans_updated_result:
            list1.append(obj)
    print(list1)
    

    return (list1)






# def addindatabasefromcsv(request):
#     print("suhiab")
#     files = glob.glob(r'D:\digitizedfiles\\*')
#     list1 = []
#     # print(files)
#     for file in files:
#         file2 = str(file).split('_')
#         file1 = file2[len(file2) - 1][:1]
#         print(file1)
#         if file1 == "b":
#             print(file)
#             list = []
#
#             reader = pd.read_csv(file)
#             list.append("BANK")
#             # list.append(reader.iloc[0]['bank'])
#             list.append(reader.iloc[0]['Account Number'])
#             list.append(reader.iloc[0]['Account Name'])
#             # list.append(reader.iloc[0]['customer_id'])
#
#             reader['Txn Date'] = pd.to_datetime(reader['Txn Date'])
#             reader['Txn Date'] = reader['Txn Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
#             reader['Txn Date'] = reader['Txn Date'].astype('str')
#             reader = reader.replace(np.nan, 'NA')
#             reader['creation_time'] = datetime.datetime.now()
#
#             reader['last_modification_time'] = datetime.datetime.now()
#             reader['image_name'] = "asmfbejhb"
#             reader['customer_id'] = 0
#             reader['created_by_id']=1
#
#             print(render)
#             for i in range(len(reader)):
#                 row = reader.iloc[i]
#                 print(i)
#                 print(row)
#                 with connection.cursor() as cursor:
#                     cursor.execute("insert into bank_bank(txn_date,description,cheque_number,debit,credit,balance,account_name,account_number,mode,entity,source_of_trans,entity_bank,sub_mode,transaction_type,bank_name,lid,creation_time,last_modification_time,image_name,customer_id,created_by_id) values(%s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s, %s,%s,%s)", row)
#             os.remove(file)
#
#             list1.append(list)
#             continue;
#         if file1 == "i":
#             file3 = file2[1]
#             file4 = file2[2]
#             if file3 == "form16":
#                 if file4 == "challans":
#                     print("challans")
#                     list = []
#                     reader = pd.read_csv(file)
#                     list.append("ITR")
#                     list.append("FORM16_challans")
#                     list.append("PANno")
#                     list.append("raju")
#
#                     reader['tax_deposited_date'] = pd.to_datetime(reader['tax_deposited_date'])
#                     reader['tax_deposited_date'] = reader['tax_deposited_date'].apply(lambda x: x.strftime('%Y-%m-%d'))
#                     reader['tax_deposited_date'] = reader['tax_deposited_date'].astype('str')
#                     reader = reader.replace(np.nan, 'NA')
#                     reader['creation_time'] = datetime.datetime.now()
#
#                     reader['last_modification_time'] = datetime.datetime.now()
#
#                     for i in range(len(reader)):
#                         row = reader.iloc[i]
#
#                         print(i)
#                         with connection.cursor() as cursor:
#                             cursor.execute(
#                                 "insert into form16_challans(tax_deposited,bsr_code,tax_deposited_date,challan_serial_no,status_match_oltas,deal_id,customer_id,assessment_year,creation_time,last_modification_time) values(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)",
#                                 row)
#                     list1.append(list)
#                     os.remove(file)
#                     continue;
#
#                 if file4 == "info":
#                     print("info")
#                 if file4 == "partb":
#                     print("partb")
#                 if file4 == "quarters":
#                     print("quarters")
#             if file3 == "form26as":
#                 if file4 == "asseseedetails":
#                     print("asseseedetails")
#                 if file4 == "parta":
#                     print("parta")
#                 if file4 == "partb":
#                     print("partb")
#                 if file4 == "partc":
#                     print("partc")
#                 if file4 == "partd":
#                     print("partd")
#                 if file4 == "partg":
#                     print("partg")
#             if file3 == "itr":
#                 print("itr")
#                 list = []
#                 reader = pd.read_csv(file)
#                 list.append("ITR")
#                 list.append("FORM V")
#                 list.append("PANno")
#                 list.append("raju")
#
#                 # reader['tax_deposited_date']=pd.to_datetime(reader['tax_deposited_date'])
#                 # reader['tax_deposited_date']=reader['tax_deposited_date'].apply(lambda x :x.strftime('%Y-%m-%d'))
#                 # reader['tax_deposited_date']=reader['tax_deposited_date'].astype('str')
#                 reader = reader.replace(np.nan, 'NA')
#                 reader['creation_time'] = datetime.datetime.now()
#                 reader['last_modification_time'] = datetime.datetime.now()
#
#                 for i in range(len(reader)):
#                     row = reader.iloc[i]
#                     print(i)
#                     with connection.cursor() as cursor:
#                         cursor.execute(
#                             "insert into itrv_itrv(assessment_year,name,pan,town_city_district_state,pin_code,efiling_acknowledgement_number,form_no,date_of_itr_filed,gross_total_income,deductions_under_chapter_vi_a,total_income,total_income_deemed_total_income_under_amt_mat,total_income_current_year_loss,net_tax_payable,interest_and_fee_payable,total_tax_interest_and_fee_payable,taxes_paid_advance_tax,taxes_paid_tds,taxes_paid_tcs,taxes_paid_self_assessment_tax,taxes_paid_total_taxes_paid,tax_payable,refund,deal_id,customer_id,image_name,creation_time,last_modification_time) values(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s, %s, %s,%s, %s, %s,%s, %s)",
#                             row)
#                 list1.append(list)
#                 os.remove(file)
#                 continue;
#
#     print(list1)
#     return render(request, "afterdownload.html", {'afterdownload': list1})


import mysql.connector
@login_required
def update_after_download(request):
    if request.is_ajax() and request.method == "POST":
        lid = request.POST.get('lid')
        cid = request.POST.get('cid')
        identifier = request.POST.get('identifier')
        
        sub_type = request.POST.get('sub_type')
        result = ''
        print(lid,cid,identifier, sub_type)
        identifier = identifier.replace("'",'')
        if sub_type == "BANK":
            with connection.cursor() as cursor:
                sql_query = ("update a3_kit.bank_bank set customer_id =" + cid + " where deal_id=" + lid + " and account_number LIKE " + "'%" + identifier + "%'" + ";")
                print(sql_query)
                cursor.execute(sql_query)
                result = "Successfuly Updated!"
        print(identifier)
        print(sub_type)

        if sub_type == "ITR":
            with connection.cursor() as cursor:
                sql_query = (
                            "update a3_kit.itrv_itrv set customer_id =" + cid + " where deal_id=" + lid + " and pan LIKE " + "'%" + identifier + "%'" + ";")
                print(sql_query)
                cursor.execute(sql_query)
                result = "Successfuly Updated!"


        with connection.cursor() as cursor: 
            cursor.execute("SELECT deal_id,name from a3_kit.los_did_cid_generation  where customer_id =" + cid + ";")
            data1= dictfetchall(cursor)
            print(data1[0]['name'])
            name1=data1[0]['name'];
            

        data_allocation_table="";
        with connection.cursor() as cursor:       
            cursor.execute("SELECT * from customer_allocation  where identifier LIKE" + "'%" + identifier + "%' and lid = " + lid + ";")
            data_allocation_table= dictfetchall(cursor)
            print(data_allocation_table)
        if len(data_allocation_table)>0:
            print("XXXX")
            with connection.cursor() as cursor: 
                sql_query = ("update a3_kit.customer_allocation set cid = " + cid + " , name = '" + name1 + "' where lid = " + lid + " and identifier LIKE " + "'%" + identifier + "%'" + ";")
                cursor.execute(sql_query)
        else:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",                        ###connect to database
            password="123456789",
            database="a3_kit"
                )

            mycursor = mydb.cursor() 
                
               
            sql = "INSERT INTO a3_kit.customer_allocation (lid,did,cid,identifier,name) VALUES (%s, %s, %s, %s, %s);"
    
            lid=lid
            did=data1[0]['deal_id']
            cid=cid
            name=data1[0]['name']
        
            identifier=identifier
        

            val = (lid,did,cid,identifier,name)

            mycursor.execute(sql, val)

            mydb.commit()
            
                


            


        return JsonResponse({"result":result})






def summaryofallfile(request):
    # customer_id=str(120)
    # mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="root",                        ###connect to database
    #     password="123456789",
    #     database="a3_kit"
    #         )

    # mycursor = mydb.cursor() 
    # mycursor.execute("SELECT COUNT(file_name) as bank_upload , COUNT(distinct(lead_id)) as lead_id FROM bank_statment_of_lead WHERE type='bank';")
    # result = dictfetchall(mycursor)
    # print(result)
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(file_name) as bank_upload , COUNT(distinct(lead_id)) as lead_id FROM upload_file_details WHERE type='bank';")
        count_bank=cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(file_name) as bank_upload , COUNT(distinct(lead_id)) as lead_id FROM upload_file_details WHERE type='itr';")
        count_itr=cursor.fetchall()
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT COUNT(file_name) as bank_upload FROM bank_statment_of_lead;")
    #     count_total=cursor.fetchall()
    count_total=int(count_bank[0][0]) + int(count_itr[0][0])
    print(count_total)
    print(count_bank[0][0])
    if( count_bank[0][1]>count_itr[0][1]):
        max1=count_bank[0][1]
    if( count_bank[0][1]<count_itr[0][1]):
        max1=count_itr[0][1]
    if( count_bank[0][1]==count_itr[0][1]):
        max1=count_itr[0][1]
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(file_name) as download,count(distinct(lead_id))   FROM downloaded_file_details where substring(file_name,-5,1)='b' ;")
        count_bank1=cursor.fetchall()
        print(count_bank1)
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(file_name) as download,count(distinct(lead_id))   FROM downloaded_file_details where substring(file_name,-5,1)='i' ;")
        count_itr1=cursor.fetchall()
    if( count_bank1[0][1]>count_itr1[0][1]):
        max2=count_bank1[0][1]
    if( count_bank1[0][1]<count_itr1[0][1]):
        max2=count_itr1[0][1]
    if( count_bank1[0][1]==count_itr1[0][1]):
        max2=count_itr1[0][1]
    
    count_total1=int(count_bank1[0][0]) + int(count_itr1[0][0])
    
 
    
                           
    return render(request,"summaryofallfile.html",{'count_bank': count_bank,'count_itr' : count_itr,'max1' : max1, 'count_total' : count_total,'count_bank1' : count_bank1 ,'count_itr1' : count_itr1,'max2' : max2,'count_total1':count_total1})




@login_required
def update_cust_id_if_c_gr_0(request):
    if request.is_ajax() and request.method == "POST":
        lead_id = request.POST.get('id')
        print(lead_id)
        
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT dbs.lead_id, dbs.name,dbs.customer_id FROM a3_kit.los_did_cid_generation as dbs where dbs.lead_id=" + lead_id + ";")
            cust_details = dictfetchall(cursor)

        with connection.cursor() as cursor:
                cursor.execute("SELECT customer_id,bank_name as sub_type,account_name as name,account_number as identifier from a3_kit.bank_bank as bk where deal_id=" + lead_id + " group by account_number;")
                bank_updated_result = dictfetchall(cursor)

        with connection.cursor() as cursor:
                    cursor.execute("SELECT customer_id,name,pan as identifier FROM a3_kit.itrv_itrv  where deal_id=" + lead_id + " group by pan ;")
                    itr_updated_result = dictfetchall(cursor)
                    print(itr_updated_result)


        list1=[]
        if len(bank_updated_result)>0:
            for obj in bank_updated_result:
                obj["doc_type"] = "BANK"
                list1.append(obj)
        if len(itr_updated_result)>0:
            for obj in itr_updated_result:
                obj["doc_type"] = "ITR"
                obj["sub_type"] = "ITR V"
                list1.append(obj)
    # if len(form16_challans_updated_result)>0:
    #     for obj in form16_challans_updated_result:
    #         list1.append(obj)
        
        
        return_data = list1
        print(return_data)

    return JsonResponse({"afterdownload":return_data,"cust_details":cust_details})
