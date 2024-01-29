with open("input_on.txt") as file:
    data = file.read().strip().split("\n\n")

monkeys = []

class Monkey():
    def __init__(self, items, operation, test, true,false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspected = 0
    def __str__(self):
        return f"Monkey(items={self.items},  inspected={self.inspected})"


for monkey in data:
    
    lines = monkey.splitlines()
    items = list(map(int,lines[1].split(": ")[1].split(", ")))
    # print(items)
    test = int(lines[3].split()[-1])
    true = int(lines[4].split()[-1])
    false = int(lines[5].split()[-1])
    #eval to process string to "code" (lambda to split for essensial info and then compile function )
    operation = eval("lambda old:" + lines[2].split("= ")[1])
    # print(test)     
    # print(true,false)   
    monkey = Monkey(items,operation,test,true,false)        
    monkeys.append(monkey)
# print(monkeys)


for _ in range(20):
   
    for monkey in monkeys:
        # print(monkey)
        for item in monkey.items:
            monkey.inspected +=1
            # print("item: ", item)
            item = monkey.operation(item)
            item //=3
            
            if item % monkey.test == 0:
                monkeys[monkey.true].items.append(item)
            else:
                monkeys[monkey.false].items.append(item)
        
        monkey.items = []

monkeys.sort(key= lambda monkey: monkey.inspected)
for monkey in monkeys:
    print(monkey)

ans = monkeys[-1].inspected * monkeys[-2].inspected
print(ans)

# print(monkeys)