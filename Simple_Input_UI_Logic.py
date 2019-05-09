# In this project - it shows the important of exception and why


while True :
    try:
        number = int(input("What's your fav number boss?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure you enter a number only")
    except ZeroDivisionError:
        print("Don't pick zero!")
    except:
        break
    finally:
            print("Transaction complete")

