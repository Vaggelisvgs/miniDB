import time
class EfficiencyCalculate :
    meta=None
    def __init__(self):
        self.cs_start_time=None
        
    def start_calculate_time(self):
        self.cs_start_time=time.time()

    def end_calculate_time(self,method_name,table_name,timee,char):
        end_time=time.time()
        if(timee!=None):
            method_len=len(method_name)
            constant_len=28
            number_len=len("{:8.4f}".format(((end_time-timee)*1000)))
            table_len=len(table_name)
            text_len=method_len+constant_len+number_len+table_len
            space_len=70-text_len
            if(char=='a'):
                print("| "+method_name+": "+table_name+" done in ","{:8.4}".format(((end_time-timee)*1000)),"  milliseconds"," "*(space_len-2),"|")
            else:
                print("|~ "+method_name+": "+table_name+" done in ","{:8.4}".format(((end_time-timee)*1000)),"  milliseconds"," "*(space_len-4),"~|")
            print('='*70,"\n")
        else:
            method_len=len(method_name)
            constant_len=28
            number_len=len("{:8.4f}".format(((end_time-self.cs_start_time)*1000)))
            table_len=len(table_name)
            text_len=method_len+constant_len+number_len+table_len
            space_len=70-text_len
            if(char=='a'):
                print("| "+method_name+": "+table_name+" done in ","{:8.4}".format(((end_time-self.cs_start_time)*1000)),"  milliseconds"," "*(space_len-2),"|")
            else:
                print("|~ "+method_name+": "+table_name+" done in ","{:8.4}".format(((end_time-self.cs_start_time)*1000)),"  milliseconds"," "*(space_len-4),"~|")
  
    def Ask_User(self):
        global effcalc
        effcalc=True
        ask_meta=input("Do you want to enable efficiency calculate for meta tables?[Y/N]"+"\n")
        global meta
        if(ask_meta=='Y' or ask_meta=='y'):
            print("meta tables efficiency calculate on"+'\n')
            meta=True
        else:
            print("meta tables efficiency calculate off"+'\n')
            meta=False
        return meta


