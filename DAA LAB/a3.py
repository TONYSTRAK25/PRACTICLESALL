def fractional_knapsack(value, weight, capacity):

    ratio = [(v / w, v, w) for v, w in zip(value, weight)]
    ratio.sort(reverse=True)

    total_value = 0.0 
    for r, v, w in ratio:  #6,60,10  #5 100 20
        if capacity >= w:  #50
            capacity -= w  #50-10=40   40-20=20
            total_value += v  #0+60=60 +100 =160
        else:
            total_value += r * capacity  # 4*20 = 80
            break

    return total_value

value = [60, 100, 120]   
weight = [10, 20, 30]    
capacity = 50            

max_value = fractional_knapsack(value, weight, capacity)
print("Maximum value in Knapsack =",max_value)
