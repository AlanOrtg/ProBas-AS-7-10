mora = 5000
Gasto_Mora = 3500
if mora >= 4000:
    if mora - Gasto_Mora >= 1500:
        print("tienes mucha mora")
    elif mora - Gasto_Mora <= 0:
        print("Estas en crisis")
    else: 
        print("no tienes mora suficiente")
    
    
elif mora >= 2000:
    print ("tienes mora")

else: print("no tienes mora")