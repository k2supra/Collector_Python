try:
    print("Enter  problem")
    problem = input("->")

    print(f"Result is {eval(problem)}")
except Exception as ex:
    print(f"Error : {ex}")