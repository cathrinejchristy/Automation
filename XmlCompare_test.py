import xml.sax
from itertools import accumulate
import logging
import os
from collections import OrderedDict

class XMLHandler(xml.sax.ContentHandler):
    
    def __init__(self):
        self.CurrentData = ""
        self.date = ""
        self.post_date = ""
        self.debit_credit_flag = ""
        self.response_code = ""
        self.description = ""
        self.txn_reference_id = ""
        self.currency = ""
        self.amount = ""
        self.source_currency = ""
        self.source_amount = ""
        self.auth_code = ""
        self.running_balance = ""
        self.transaction_code = ""
        
   # Call when an element starts
    def startElement(self, tag, attrs):
        self.CurrentData = tag
        if(tag == "ns0:transaction"):
            logging.debug("*********transaction*************")
            
            
        
   # Call when an elements ends
    def endElement(self, tag):
        if(self.CurrentData == "ns0:date"):
            logging.debug("original_date:" + self.date)
        elif(self.CurrentData == "ns0:post_date"):
            logging.debug("post_date:" + self.post_date)
        elif(self.CurrentData == "ns0:debit_credit_flag"):
            logging.debug("debit_credit_flag:" + self.debit_credit_flag)
        elif(self.CurrentData == "ns0:response_code"):
            logging.debug("response_code:" + self.response_code)
        elif(self.CurrentData == "ns0:description"):
            logging.debug("description:" + self.description)
        elif(self.CurrentData == "ns0:txn_reference_id"):
            logging.debug("txn_reference_id:" + self.txn_reference_id)
        elif(self.CurrentData == "ns0:currency"):
            logging.debug("currency_1:" + self.currency)
        elif(self.CurrentData == "ns0:amount"):
            logging.debug("amount_1:" + self.amount)
        elif(self.CurrentData == "ns0:source_currency"):
            logging.debug("source_currency:" + self.source_currency)
        elif(self.CurrentData == "ns0:source_amount"):
            logging.debug("source_amount:" + self.source_amount)
        elif(self.CurrentData == "ns0:auth_code"):
            logging.debug("auth_code:" + self.auth_code)
        elif(self.CurrentData == "ns0:running_balance"):
            logging.debug("running_balance:" + self.running_balance)
        elif(self.CurrentData == "ns0:transaction_code"):
            logging.debug("transaction_code:" + self.transaction_code)
        self.CurrentData = ""

   # Call when a character is read
    def characters(self, content):
        if(self.CurrentData == "ns0:date"):
            self.date = content
        elif(self.CurrentData == "ns0:post_date"):
            self.post_date = content
        elif(self.CurrentData == "ns0:debit_credit_flag"):
            self.debit_credit_flag = content
        elif(self.CurrentData == "ns0:response_code"):
            self.response_code = content
        elif(self.CurrentData == "ns0:description"):
            self.description = content
        elif(self.CurrentData == "ns0:txn_reference_id"):
            self.txn_reference_id = content
        elif(self.CurrentData == "ns0:currency"):
            self.currency = content
        elif(self.CurrentData == "ns0:amount"):
            self.amount = content
        elif(self.CurrentData == "ns0:source_currency"):
            self.source_currency = content
        elif(self.CurrentData == "ns0:source_amount"):
            self.source_amount = content
        elif(self.CurrentData == "ns0:auth_code"):
            self.auth_code = content
        elif(self.CurrentData == "ns0:running_balance"):
            self.running_balance = content
        elif(self.CurrentData == "ns0:transaction_code"):
            self.transaction_code = content
            
def covert_xml_to_list():
    #Read file 
    f = open(log, 'r')
    lines = f.readlines()

    final_list =[]
    create_list =[]
    final_list.clear()
    create_list.clear()

    for line in lines:
        if "xml file name:" not in str(line):
            if "***transaction**" in str(line):
                try :   
                    final_list.append(create_list)
                except:
                    pass
                create_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            else:
                if "original_date" in str(line):
                    create_list[0] = str(str(line).split("original_date:")[1].strip('\n'))
                elif "post_date" in str(line):
                    create_list[1] = str(str(line).split("post_date:")[1].strip('\n'))
                elif "debit_credit_flag:" in str(line):
                    create_list[2] = str(str(line).split("debit_credit_flag:")[1].strip('\n'))
                elif "response_code:" in str(line):
                    create_list[3] = str(str(line).split("response_code:")[1].strip('\n'))
                elif "description:" in str(line):
                    create_list[4] = str(str(line).split("description:")[1].strip('\n'))
                elif "txn_reference_id:" in str(line):
                    create_list[5] = str(str(line).split("txn_reference_id:")[1].strip('\n'))
                elif "currency_1:" in str(line):
                    create_list[6] = str(str(line).split("currency_1:")[1].strip('\n'))
                elif "amount_1" in str(line):
                    create_list[7] = str(str(line).split("amount_1:")[1].strip('\n'))
                elif "source_currency:" in str(line):
                    create_list[8] = str(str(line).split("source_currency:")[1].strip('\n'))
                elif "source_amount:" in str(line):
                    create_list[9] = str(str(line).split("source_amount:")[1].strip('\n'))
                elif "source_amount:" in str(line):
                    create_list[10] = str(str(line).split("source_amount:")[1].strip('\n'))
                elif "auth_code:" in str(line):
                    create_list[11] = str(str(line).split("auth_code:")[1].strip('\n'))
                elif "running_balance:" in str(line):
                    create_list[12] = str(str(line).split("running_balance:")[1].strip('\n'))
                elif "transaction_code:" in str(line):
                    create_list[13] = str(str(line).split("transaction_code:")[1].strip('\n'))
    final_list.append(create_list)
    return final_list

def remove_the_file_content():
    f = open(log, 'r+')
    f.truncate(0)

def find_duplicate_transactions(list_name):
    #Find the duplicate transaction in a list
    duplicate_list = []
    duplicate_list.clear()
    for e in list_name:
        if list_name.count(e)> 1:
            duplicate_list.append(e)
    return duplicate_list

def checkSubset(list1, list2):
    return (all(map(list1.__contains__, list2)))

def Remove(listname):
     res = []
     res.clear()
     check = set()
     for x in listname:
         hsh = tuple(x)
         if hsh not in check:
             res.append(x)
             check.add(hsh)
               
     return res

def non_match_elements(first, second):
    non_match = []
    non_match.clear()
    for i in first:
        if i not in second:
            non_match.append(i)
    return non_match

def identify_non_match(list_c, list_d):
    list3 = [value for value in list_c if value in list_d]
    print (list3)


# log file

log = r".\transactions.log"
logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


f = open("output.txt", "w+")
f.write("**********TEST NAME : COMPARE THE TRANSACTIONS IN TWO XML FILES**********\n")



# create an XMLReader
parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
# override the default ContextHandler
Handler = XMLHandler()
parser.setContentHandler( Handler )

transaction_list_in_file1 = []
transaction_list_in_file2 = []

xml_file_input = [str(r"C:\Users\Muthukumar\Documents\GitHub\Automation\Source_File.xml"), str(r"C:\Users\Muthukumar\Documents\GitHub\Automation\Target_File.xml")]
parser.parse(str(xml_file_input[0]))   
transaction_list_in_file1 = covert_xml_to_list()
remove_the_file_content()
parser.parse(str(xml_file_input[1]))
transaction_list_in_file2 = covert_xml_to_list()
remove_the_file_content()

transaction_list_in_file1 = [ele for ele in transaction_list_in_file1 if ele != []]
transaction_list_in_file2 = [ele for ele in transaction_list_in_file2 if ele != []]

#Identify the Duplicate Transactions
f.write ("============TEST 1 : Identify the duplicate transaction============\n")
duplicate_transactions_set1 = find_duplicate_transactions(transaction_list_in_file1)
if len(duplicate_transactions_set1) > 0:
    f.write ("\nDuplicate Transactions in Source File\n")
    for i in duplicate_transactions_set1:
        f.write ("\n")
        f.write("date :" + i[0] + "\n")
        f.write("post_date :" + i[1] + "\n")
        f.write("debit_credit_flag :" + i[2] + "\n")
        f.write("response_code :" + i[3] + "\n")
        f.write("description :" + i[4] + "\n")
        f.write("txn_reference_id :" + i[5] + "\n")
        f.write("currency :" + i[6] + "\n")
        f.write("amount :" + i[7] + "\n")
        f.write("source_currency :" + i[8] + "\n")
        f.write("source_amount :" + i[9] + "\n")
        f.write("auth_code :" + str(i[10]) + "\n")
        f.write("running_balance :" + i[11] + "\n")
        f.write("transaction_code :" + i[12] + "\n")

duplicate_transactions_set2 = find_duplicate_transactions(transaction_list_in_file2)
if len(duplicate_transactions_set2) > 0:
    f.write ("\nDuplicate Transactions in Target File\n")
    for i in duplicate_transactions_set2:
        f.write ("\n")
        f.write("date :" + i[0] + "\n")
        f.write("post_date :" + i[1] + "\n")
        f.write("debit_credit_flag :" + i[2] + "\n")
        f.write("response_code :" + i[3] + "\n")
        f.write("description :" + i[4] + "\n")
        f.write("txn_reference_id :" + i[5] + "\n")
        f.write("currency :" + i[6] + "\n")
        f.write("amount :" + i[7] + "\n")
        f.write("source_currency :" + i[8] + "\n")
        f.write("source_amount :" + i[9] + "\n")
        f.write("auth_code :" + str(i[10]) + "\n")
        f.write("running_balance :" + i[11] + "\n")
        f.write("transaction_code :" + i[12] + "\n") 

    
if len(duplicate_transactions_set1) == 0 and len(duplicate_transactions_set2) == 0 :
    f.write ("TEST RESULT : PASS  - No duplicate transactions in both the file\n")
else:
    f.write ("TEST RESULT : FAIL  - Duplicates transactions are identified\n")
    
f.write ("============TEST 1 : Completed============\n\n")


#Verify all the transactions in file1 in file2 and file2 in file1
f.write ("============TEST 2 : Verify the transactions in both the files are matching============\n")
unique_transac_list1 = Remove (transaction_list_in_file1)
unique_transac_list2 = Remove (transaction_list_in_file2)
compared = checkSubset(unique_transac_list1, unique_transac_list2)
if not compared :
    non_matched_1 = non_match_elements (unique_transac_list1, unique_transac_list2)
    
    if len(non_matched_1) > 0:
        f.write ("\nNon matched Transactions in Source File\n\n")
        for i in non_matched_1:
            f.write ("\n")
            f.write("date :" + i[0] + "\n")
            f.write("post_date :" + i[1] + "\n")
            f.write("debit_credit_flag :" + i[2] + "\n")
            f.write("response_code :" + i[3] + "\n")
            f.write("description :" + i[4] + "\n")
            f.write("txn_reference_id :" + i[5] + "\n")
            f.write("currency :" + i[6] + "\n")
            f.write("amount :" + i[7] + "\n")
            f.write("source_currency :" + i[8] + "\n")
            f.write("source_amount :" + i[9] + "\n")
            f.write("auth_code :" + str(i[10]) + "\n")
            f.write("running_balance :" + i[11] + "\n")
            f.write("transaction_code :" + i[12] + "\n")


    non_matched_2 = non_match_elements (unique_transac_list2, unique_transac_list1)
    
    if len(non_matched_2) > 0:
        f.write ("\nNon matched Transactions in Target File\n\n")
        for i in non_matched_2:
            f.write ("\n")
            f.write("date :" + i[0] + "\n")
            f.write("post_date :" + i[1] + "\n")
            f.write("debit_credit_flag :" + i[2] + "\n")
            f.write("response_code :" + i[3] + "\n")
            f.write("description :" + i[4] + "\n")
            f.write("txn_reference_id :" + i[5] + "\n")
            f.write("currency :" + i[6] + "\n")
            f.write("amount :" + i[7] + "\n")
            f.write("source_currency :" + i[8] + "\n")
            f.write("source_amount :" + i[9] + "\n")
            f.write("auth_code :" + str(i[10]) + "\n")
            f.write("running_balance :" + i[11] + "\n")
            f.write("transaction_code :" + i[12] + "\n")
            
    f.write ("\nTEST RESULT : FAIL  - The transactions in both the files are not matched\n")
else :
    f.write ("\nTEST RESULT : PASS  - The transactions in both the file are matching\n")

f.write ("============TEST 2 : Completed============\n\n")
f.close()

contents = open(r"./output.txt","r")
with open("xml_Compare.html", "w") as e:
    for lines in contents.readlines():
        e.write("<pre>" + lines + "</pre> <br>\n")
