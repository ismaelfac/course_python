n1 = input("Insert number One")
n2 = input("Insert number Two")
n1 = int(n1)
n2 = int(n2)
sum = n1 + n2
res = n1 - n2
mul = n1 * n2
div = n1 / n2
out_msg = f"""
 For numbers {n1} and {n2}, the result is: 
 the result for sum is: {sum}
 the result for res is: {res}
 the result for mul is: {mul}
 the result for div is: {div}
"""

print(out_msg)