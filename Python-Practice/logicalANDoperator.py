#Using The Logical Operators OR & The And Operator To Decide


#has_high_income = input('Do you have a high income? : ')
#has_good_credit = input('Do you have good credit? : ')


#positive_response = ['True', 'Yes']
#has_none_or_one = ['False', 'No']


#has_high_income = True
has_good_credit =  False

have_criminal_record = False



#if has_high_income or has_good_credit:
   #print('You are eligible for LOAN!')

#else:
  # print('Sorry you are ineligible to get the loan')

#if has_high_income in positive_response and has_good_credit in positive_response:
   #print('You are eligible For LOAN!')

#else:
    #print('You are not eligible')

if has_good_credit and not have_criminal_record:
    print('You are eligible!')

else:
    print('You are not eligible due to your criminal record')