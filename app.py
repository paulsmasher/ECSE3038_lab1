import math
def parallel(resistor_list):
    Total_Resistance=0
    for resistor in resistor_list:
        Total_Resistance= Total_Resistance + 1/resistor
        
    Total_Resistance= 1/Total_Resistance

    print(Total_Resistance, "ohms")
    return Total_Resistance



parallel([300,2000,1000])

def paralell(list):
    y= 0
    for x in list:
        y=y+ 1/y

        y = 1/y

        print(y,"ohms")
        return y 
    


    value = []
    def potential_divider(volt,list):
        total_resistance = sum(list) 
        

        for x in list: 
            output_voltage= (volt*x)/total_resistance
            value.append(output_voltage)
            return value
    
    print(potential_divider(9,[3000,1000]))
