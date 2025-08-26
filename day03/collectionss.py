print("\n=================== LISTS =====================\n")

print("\n Intialize List ")
lists = ["mouse", "laptop", "android"]
print(lists)

print("original",lists)

print("\n ADD ")
lists.append("notebook")
lists.extend(["toothpick", "pencil"])
print("new list:", lists)

print("\n DELETE ")
removed = lists.pop(1)
print("Now:", lists)

print("\n LOOP ")
for i in lists:
    print("List: ", lists)

print("\n ENUMERATE ")
for i, lis in enumerate(lists):
    print(i, lis)



print("\n========== DICTS =============\n")
print("\n INITIALIZE ")
timing = {"tues":"2hrs", "wed":"5hrs"}
print("timing", timing)
print("wednesday:", timing["wed"])

print("\n ADD/ UPDATE/ ACCESS ")
timing["mon"] = "6hrs"
print(timing)

print("\n LOOP ")
for h  in timing:
    print(h, ":", timing[h])
print("\n ENUMERATE")
for i, (day, hours) in enumerate(timing.items()):
    print(i, day, hours)
print(type(timing))

print("\n CONEVERT TO TUPLE")
pairs = list(timing.items())
print("as list of tuples:", pairs)

print("\n SHOPPING LIST PROGRAM!!")
items_n_p = []

while True:
    choice = input(" \nChoice: \n1. to add to list \n2. view list \n pick : ")
    if choice == "1":

        items_name = input("Enter item name : ")
        items_price = int(input("Enter item price : "))
        items_n_p.append({"name": items_name, "price": items_price})
    elif choice == "2":
        for item in items_n_p:
            print(item)
    else:
        print("invalid input! restart program!!")
        break

print("\n ================= LIST AND DICT COMBINATION ==================\n")
tasks =[
{"task": "Homework", "time": "2 hrs"},
{"task": "Exercise", "time": "1 hr"},
]
tasks.append({"task":"Read", "time": "30 min"})
for t in tasks:
    print(f"Task: {t['task']}, Time: {t['time']}")
print("total tasks:", len(tasks))
