import random
Rice = 45 
Sugar = 40 
Oil = 130 

rice_bought  = 3
sugar_bought = 2.5
oil_bought = 1.8

rice_total = rice_bought * Rice
sugar_total = sugar_bought * Sugar
oil_total = oil_bought * Oil

total_cost = rice_total + sugar_total + oil_total
print("Total cost: ", total_cost)

total_cost_int = int(total_cost)
print("Total cost (integer): ", total_cost_int)

total_cost_str = str(total_cost)
print("Total cost (string): ", total_cost_str)

delivery_charge = random.randrange(5,10)

final_bill = total_cost + delivery_charge
print("Final Bill: ", final_bill)