def Solve(numheads, numlegs):
    chicken = 0
    rabbit = 0
    if (numheads>=numlegs): return "no solution"
    elif (numlegs%2!=0): return "no solution"
    else:
        rabbit = (numlegs - 2*numheads)/2
        chicken = numheads - rabbit
        return int(chicken), int(rabbit)
problem = Solve(35, 94)
print(problem)
