def calculate_avg_payment_column(input_data):
    print("function loaded successfully")
    pay_column = ["PAY_1", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6"]
    bill_column = ['BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6']

    input_data['Avg_pay_amt'] = input_data[pay_column].mean(axis=1)
    input_data["Avg_bill_pay"] = input_data[bill_column].mean(axis=1)
    input_data['Max_Delay']= input_data[pay_column].max(axis=1)

    return input_data
