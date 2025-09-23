from datetime import datetime
current_datetime = datetime.now()
current_year=current_datetime.year
validate_flag = "fail"
#date_obj=datetime.strptime(mrtg_strt_dt_str,"%Y-%m-%d")
while validate_flag == "fail":
    mrtg_strt_dt_str=input("Enter Mortgage Start Date:")
    length_check = "pass"
    year_check = "pass"
    month_check = "pass"
    day_check = "pass"
    hyphen_5_check = "pass"
    hyphen_7_check = "pass"
    year_range_check = "pass"
    month_range_check="pass"
    day_range_check="pass"
    if len(mrtg_strt_dt_str) != 10:
        print('Length Error')
        length_check = "fail"
    if mrtg_strt_dt_str[0:4].isdigit() == False:
        print("Year Error")
        year_check = "fail"
    else:
        if int(mrtg_strt_dt_str[0:4])<1987 or int(mrtg_strt_dt_str[0:4])>current_year:
            print("Invalid Year Range")
            year_range_check="fail"
    if mrtg_strt_dt_str[5:7].isdigit() == False:
        print("Month Error")
        month_check = "fail"
    else:
        if int(mrtg_strt_dt_str[5:7])<0 or int(mrtg_strt_dt_str[5:7])>13:
            print("Invalid Month Range")
            month_range_check="fail"
    if mrtg_strt_dt_str[8:10].isdigit() == False:
        print("Day Error")
        day_check = "fail"
    else:
        if month_check == "pass":
            if int(mrtg_strt_dt_str[5:7]) == 4 or int(mrtg_strt_dt_str[5:7]) == 6 or int(mrtg_strt_dt_str[5:7]) == 9 or int(mrtg_strt_dt_str[5:7]) == 11:
                if int(mrtg_strt_dt_str[8:10])<0 or int(mrtg_strt_dt_str[8:10])>30:
                    print("Invalid Day Range")
                    day_range_check="fail"
            elif int(mrtg_strt_dt_str[5:7]) == 1 or int(mrtg_strt_dt_str[5:7]) == 3 or int(mrtg_strt_dt_str[5:7]) == 5 or int(mrtg_strt_dt_str[5:7]) == 7 or int(mrtg_strt_dt_str[5:7]) == 8 or int(mrtg_strt_dt_str[5:7]) == 10 or int(mrtg_strt_dt_str[5:7]) == 12:
                if int(mrtg_strt_dt_str[8:10])<0 or int(mrtg_strt_dt_str[8:10])>31:
                    print("Invalid Day Range")
                    day_range_check="fail"
            else:
                if year_check == "pass":
                    if int(mrtg_strt_dt_str[0:4])%4 != 0:
                        if int(mrtg_strt_dt_str[8:10])<0 or int(mrtg_strt_dt_str[8:10])>28:
                            print("Invalid Day Range")
                            day_range_check="fail"
                    else:
                        if int(mrtg_strt_dt_str[8:10])<0 or int(mrtg_strt_dt_str[8:10])>29:
                            print("Invalid Day Range")
                            day_range_check="fail"
    if mrtg_strt_dt_str[4:5] != "-":
        print("5th Hyphen Error")
        hyphen_5_check="fail"
    if mrtg_strt_dt_str[7:8] != "-":
        print("7th Hyphen Error")
        hyphen_7_check="fail"
       
    if length_check == "fail" or year_check == "fail" or month_check == "fail" or day_check == "fail" or hyphen_5_check=="fail" or hyphen_7_check=="fail" or year_range_check == "fail" or month_range_check == "fail" or day_range_check == "fail" :
        validate_flag = "fail"
    else:
        validate_flag = "pass"
   
    #mrtg_strt_dy = mrtg_strt_dt_str(8:9)

print(f"Start Date: {mrtg_strt_dt_str}")
mrtg_strt_dt = datetime.strptime(mrtg_strt_dt_str,'%Y-%m-%d')
print(f"Today's Date: {current_datetime}")
validate_flag = "fail"

while validate_flag == "fail":
    mrtg_init_amnt_str=input("Enter Mortgage Initial Amount:")
   
    if not mrtg_init_amnt_str.isdigit():
        print("Amount error")
        validate_flag="fail"
    else:
        mrtg_init_amnt=int(mrtg_init_amnt_str)
        if  mrtg_init_amnt==0 :
            print("Amount error")
            validate_flag="fail"
        else:
            mrtg_init_amnt=int(mrtg_init_amnt_str)
            validate_flag = "pass"
months_diff = (current_datetime.year-mrtg_strt_dt.year)*12+(current_datetime.month-mrtg_strt_dt.month)+1
print("Total Months;",months_diff)
intrest = (mrtg_init_amnt/100)*2
print("Intrest is",intrest)
total_intrest = intrest*months_diff
print("Total intrest is",total_intrest)
total_amnt = total_intrest+mrtg_init_amnt
print("Total Amount is",total_amnt)
validate_flag = "fail"
while validate_flag == "fail":
    paid_inst=input("Enter Paid installment :")
    if not paid_inst.isdigit():
        print("Invalid Amount")
        validate_flag="fail"
    else:
       paid_inst=int(paid_inst)
       if paid_inst==0 :
           print("Invalid Amount")
           validate_flag="fail"
       else:
           paid_inst=int(paid_inst)
           final_amnt=total_amnt-int(paid_inst)
           print("Final Amount is:",final_amnt)
           validate_flag = "pass"


