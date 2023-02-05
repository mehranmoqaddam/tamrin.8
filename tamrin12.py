def mul(f1,f2):
    result = {}
    result["s"] = f1["s"] * f2["s"]
    result["m"] = f1["m"] * f2["m"]
    return result
def sum(f1 , f2):
    result = {}
    result["s"] = (f1["s"])*f2["m"] + (f2["s"] * f1["m"])
    result["m"] = f1["m"] * f2["m"]
    return result
def minus(f1 ,f2):
    result = {}
    result["s"] = (f1["s"])*f2["m"] - (f2["s"] * f1["m"])
    result["m"] = f1["m"] * f2["m"]
    return result

def div(f1 , f2):
    result = {}
    result["s"] = f1["s"] * f2["m"]
    result["m"] = f2["s"] * f1["m"]
    return result
a = {"s":2, "m":3}
b = {"s":5, "m":4}

mul_result = mul(a ,b)
sum_result = sum(a ,b)
minus_result = minus(a ,b)
div_result = div(a ,b)
print("sum: ")
print(sum_result)
print("mul: ")
print(mul_result)
print("minus: ")
print(minus_result)
print("div: ")
print(div_result)