
# Ex.1:---------
try:
    print(10/2)
except:
    print("Your Code is failed")


# Ex.2:---------
try:
    s = 100/0
    print(s)
except:
    print("Not Executed !")


# Ex.3:---------
try:
    s = 100/0
    print(s)
except Exception as e:
    print("Error of: ", e)


# Ex.4:---------
try:
    st = 'Hi, I am Dibyendu Biswas'
    nT = 2021
    add = st + nT
    print('Add String and Integer without type casting: ', add)
except Exception as e:
    print('Your frist code is wrong method', e)
else:
    print('Content/ Statement has no error and run successfully')


# Ex.5:---------
try:
    st = 'Hi, I am Dibyendu Biswas'
    nT = 2021
    add = st + ' ' + str(nT)
    print('Add String and Integer without type casting: ', add)
    
except Exception as e:
    print('Your frist code is wrong method', e)
    
else:
    print('Content/ Statement has no error and run successfully')


# Ex.6:---------
try:
    st = 'Hi, I am Dibyendu Biswas'
    nT = 2020
    add = st + ' ' + str(nT)
    print(add)
finally:
    print('All statements are Executed')


# Ex.7:---------
try:
    st = 'Hi, I am Dibyendu Biswas'
    nT = 2020
    add = st + ' ' + nT
    print(add)
finally:
    a = 20
    b = 300
    s = a + b
    print('sum of a and b: ', s)


# Ex.8:---------
try:
    st = 'Hi, I am Dibyendu Biswas'
    nT = 2020
    add = st + ' ' + nT
    print(add)
except Exception as e:
    print("Error is: ", e)
finally:
    a = 20
    b = 300
    s = a + b
    print('sum of a and b: ', s)


# Ex.9:---------
try:
    st = 'Hi, I am Dibyendu Biswas'
    nT = 2020
    add = st + ' ' + nT
    print(add)
except Exception as e:
    print("Error is: ", e)
finally:
    a = 20
    b = 300
    s = a + b
    print('sum of a and b: ', s)
    try:
        10/0
    except Exception as e:
        print('Error is: ', e)


# Ex.10:---------
def AskInt():
    try:
        val = int(input("Enter a number: "))
    except Exception as e:
        print("Error is: ", e)
        try:
            val = int(input("Enter a number: "))
        except:
            print("Ediot handle it.")
    finally:
        print("Finally Executed !")
        try:
            print("Value is: ", val)
        except Exception as e:
            print("Error is: ", e)
AskInt()


# Ex.11:---------
def Input(a, b):
    try:
        s = a + b
        m = a / b
        print("Sum value is: ", s)
        print("Product value is: ", m)
    except Exception as e:
        print("Error is: ", e)
    finally:
        print("Finally Executed !")
        try:
            print(f"Values are {a} and {b}")
        except Exception as e:
            print("Error is: ", e)

Input(20, 10)
Input(10, 0)

