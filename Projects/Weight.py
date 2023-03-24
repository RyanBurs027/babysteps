
while True:
    
    "           Weight CHECK            "
    
    check_weight =(float(input("What is your weight?  ")))
    
    kg_or_lbs = (input("Is that a (K)g or in (L)bs: "))

    if kg_or_lbs == "L" or kg_or_lbs == "l":
            total_kg = 0
            total_kg = total_kg + float(check_weight)
            kg_total = total_kg * 0.45
            print("Your weight in Kg is :" + str(kg_total) + "Kilograms!" )
            break
    
    elif kg_or_lbs == "K" or kg_or_lbs == "k":
            total_lb = 0
            total_lb = total_lb + float(check_weight)
            lb_total = total_lb * 2.2
            print("Your weight in lbs is :" + str(lb_total) + "pounds!" )
            break
    
    else:
            print("You need to respond in 'K' or 'k'(in kilograms) or in 'L' or 'l' in LBS")
            