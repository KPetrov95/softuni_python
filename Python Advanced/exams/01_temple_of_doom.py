from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = deque(int(x) for x in input().split())

while True:
    if (len(substances) <= 0 or len(tools) <= 0) and challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break
    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break
    current_tool = tools.popleft()
    current_substance = substances.pop()
    result = current_substance * current_tool
    if result in challenges:
        challenges.remove(result)
    else:
        current_tool += 1
        tools.append(current_tool)
        if current_substance > 1:
            substances.append(current_substance - 1)
if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")