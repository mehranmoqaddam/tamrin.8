def sum(t1 , t2):
    result = {}
    result["h"] = t1["h"] + t2["h"]
    result["m"] = t1["m"] + t2["m"]
    result["s"] = t1["s"] + t2["s"]
    if result["s"] >= 60:
        result["s"] -= 60
        result["m"] += 1
    if result["m"] >= 60:
        result["m"] -= 60
        result["h"] += 1
    if result["h"] > 23:
        result["h"] -= 24
    return result

def minus(t1 , t2):
    result = {}
    result["h"] = t1["h"] - t2["h"]
    result["m"] = t1["m"] - t2["m"]
    result["s"] = t1["s"] - t2["s"]
    if result["s"] >= 60:
        result["s"] -= 60
        result["m"] += 1
    if result["s"] < 0:
        result["s"] += 60
        result["m"] -= 1
    if result["m"] >= 60:
        result["m"] -= 60
        result["h"] += 1
    if result["m"] < 0:
        result["m"] += 60
        result["h"] -= 1
    if result["h"] > 23:
        result["h"] -= 24
    if result["h"] < 23:
        result["h"] += 24
    return result

def show(time):
    print(time["h"],":",time["m"],":",time["s"])
time1 = {"h":4,"m":30,"s":20}
time2 = {"h":20,"m":45,"s":40}
result_sum = sum(time1,time2)
result_minus = minus(time1,time2)
print("jam e saatha")
show(result_sum)
print("tafrighe saatha")
show(result_minus)