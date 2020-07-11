#cs50 problem set 1 solved in py (https://cs50.harvard.edu/x/2020/psets/1/cash/)

twenty_five, ten, five, one = 25, 10, 5, 1

def make_change(x):
    if x > 0:
        change = int(round(x*100))
        quarter = int(change / twenty_five)
        quarter_rest = change % twenty_five
        print(quarter, 'times 25 cent coins')
        #print(quarter_rest)
        tenner = int(quarter_rest / ten)
        tenner_rest = quarter_rest % ten
        print(tenner, 'times 10 cent coins')
        #print(tenner_rest)
        fiver = int(tenner_rest / five)
        fiver_rest = tenner_rest % five
        print(fiver, 'times 5 cent coins')
        #print(fiver_rest)
        onner = int(fiver_rest / one)
        #onner_rest = fiver_rest % one
        print(onner, 'times 1 cent coins')
        #print(onner_rest)
        print(quarter, 'x 25 cent coins |', tenner, 'x 10 cent coins |', fiver, 'x 5 cent coins |', onner, 'x 1 cent coins')
    else:
        print('Please enter a valid amount, without a dollar sign!')

def input_change():    
    change_owed = input('What is the change owned?\n')
    #print('Your change is %s' % change_owed, type(change_owed))    
    try:
        val = float(change_owed)
        #print("Input is a float  number. Number = ", val, type(val))        
        make_change(val)
    except ValueError:
        try:
            val = int(change_owed)
            #print("Input is an integer number. Number = ", val, type(val))            
            val = float(val)
            make_change(val)
        except ValueError:
            print('Please enter a valid amount, without a dollar sign!')
            input_change()

input_change()
