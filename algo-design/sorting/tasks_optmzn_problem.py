## You need to write a function, which computes the maximum number of tasks that can be completed within the given time T. 
## The function accepts as arguments the number N and T and a list of the task difficulties. It must return one integer 
## - the maximum number of tasks that can be completed within the given time limit.

## Here is an example test case.
## SAMPLE INPUT
## 5 65
## 24 23 22 10 20

## SAMPLE OUTPUT
## 3
## All five tasks cannot be completed within the allowed 65 minutes, but it is possible to accomplish three tasks, 
## for example tasks 4, 5, 3 if completed in this order.
import cProfile

@profile
def maximum_completed_tasks(n, t, task_difficulties, result_list):
    if(n > 1):
        task_difficulties.sort()
        min_item = task_difficulties[0]
        next_min_item = task_difficulties[1]
        min_item_diff = []
        min_item_sum = 0

        for each in task_difficulties:
            min_item_diff.append(abs(each - min_item))

        min_item_diff.sort()
        if(min_item not in result_list):
            result_list.append(min_item)
        if(next_min_item not in result_list):
            result_list.append(next_min_item)

        print(result_list)
        min_item_sum = sum_of_resultset(result_list)
        print(min_item_sum)
        if(t - min_item_sum > next_min_item):
            task_difficulties.remove(min_item)
            maximum_completed_tasks(n - 1, t, task_difficulties, result_list)

    return len(result_list)

@profile
def sum_of_resultset(mylist):
    sum = 0
    diff = 0
    total_sum = 0
    for index in range(0, len(mylist)):
        sum = sum + mylist[index]
        if(index < len(mylist) - 1):
            diff = diff + mylist[index] - mylist[index+1]
    
    total_sum = sum + abs(diff)
    return total_sum


print(maximum_completed_tasks(5, 65, [24,23,22,10,20], []))
