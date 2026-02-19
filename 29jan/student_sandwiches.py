from collections import deque


def countStudents(students, sandwiches):
    queue = deque(students)
    stack = sandwiches

    while(sandwiches and sandwiches[0] in queue):
        print("Top sandwich: ", sandwiches[0])
        print("Front student: ", queue[0])
        if queue[0] == sandwiches[0]:
            print("Student ate the sandwich")
            queue.popleft()
            stack.pop(0)
        else:
            print("Student moved to the end of line")
            var = queue.popleft()
            queue.append(var)
        print("Line: ", queue)
        print("Stack: ", stack)
    return len(queue)

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

countStudents(students, sandwiches)