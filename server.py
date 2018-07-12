import random
def load_balance(server, num_request):

    # server = { "a": 30, "b": 20, "c": 150 , "d": 30}
    result = { }
    total = 0
    lst = []
    for key,value in server.items():
        lst.append({"name": key, "lower": total + 1, "upper": total + value})
        total += value
        result[key] = 0
        
    for i in range(1, num_request):
        rand = random.randint(1, total)
        
        for x in lst:
            if rand > x["lower"] and rand <= x["upper"]:
                result[x["name"]] += 1
            # elif rand <= int(server["a"]) + int(server["b"]):  hardcode solution
            #     result["b"] += 1
            # else:
            #     result["c"] += 1
    
    return result

print(load_balance({ "a": 30, "b": 20, "c": 150 , "d": 30}, 1000))
