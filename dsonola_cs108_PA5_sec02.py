'''

#Name: Demilade Sonola
#Assignment: #5
#Due Date: 9/30/24
#Honor Code Statement: I received no assistance on this assignment that
#violates the ethical guidelines set forth by the professor and class syllabus
#Comments: N/A
 
Also, provide descriptions for each function below.
And add sufficient comments to your code.

'''

##########################
# ab_val: Returns the absolute value of a number
##########################
def ab_val(n):
    if n<0:
        return -1*n
    return n
#print(ab_val(-7))
##########################
# circ_calc: Returns a measurement of a circle
##########################
def circ_calc(radius, shape):
    if (shape=='circumference'):
        return round(2*radius*3.14159, 3)
    elif (shape=='area'):
        return round(3.14159*(radius**2), 3)
    elif (shape=='volume'):
        return round((4/3)*(3.14159*(radius**3)), 3)
    else:
        return -1
#print(circ_calc(5, 'circumference'))

##########################
# kind_of_roots: Describes the roots of a quadratic function
##########################
def kind_of_roots(a, b, c):
    answer = (b**2)-4*a*c
    if (answer>0):
        return 'two real'
    elif (answer<0):
        return 'two imaginary'
    elif (answer==0):
        return 'one real'
#print(kind_of_roots(1, 0, -9))

##########################
# stock_advice: determines whether it's best to buy, sell, or hold a stock
##########################
def stock_advice(old_price, new_price):
    if (new_price>=old_price+(old_price*.3)):
        return 'BUY'
    elif (new_price<=old_price-(old_price*.5)):
        return 'SELL'
    elif (new_price<old_price+(old_price*.3) and new_price>old_price-(old_price*.5)):
        return 'HOLD'
#print(stock_advice(250.09, 466.75))
#print(stock_advice(100.00, 50.00))
#print(stock_advice(79.35, 50.00))
##########################
# level_up: determines if a gamer has enough points to reach the next level
##########################
def level_up(pts, level):
    if (pts>level*100+99):
        return True
    else:
        return False
#print(level_up(435, 2))
#print(level_up(555, 8))
##########################
# level_up2: determines if a gamer has enough points to reach the next level based on their level of expertise
##########################
def level_up2(pts, level, status):
    if (status=='beginner' and pts>level*100+99):
        return True
    elif (status=='intermediate' and pts>level*200+199):
        return True
    elif (status=='expert' and pts>level*500+499):
        return True
    elif (status=='pro' and pts>level*1000+999):
        return True
    else:
        return False
#print(level_up2(4350, 7, 'expert'))
#print(level_up2(4350, 7, 'pro'))
#print(level_up2(16000, 1, 'pro'))
##########################
# minutes_passed: determines the number of minutes before a start time and end time
##########################
def minutes_passed(h1,m1,h2,m2):
    if (h2>=h1):
        hour_minutes = h1*60
        hour_minutes2 = h2*60
        total1 = hour_minutes+m1
        total2 = hour_minutes2+m2
        difference = total1-total2
        if (difference<0):
            return difference*-1
        else:
            return difference
    if (h1>=h2):
        hour_minutes = h1*60
        hour_minutes2 = h2*60+720
        total1 = hour_minutes+m1
        total2 = hour_minutes2+m2
        difference = total1-total2
        if (difference<0):
            return difference*-1
        else:
            return difference
#print(minutes_passed(9, 15, 11, 45))
#print(minutes_passed(10, 59, 12, 11))
#print(minutes_passed(4, 38, 2, 2))