lst = []
number = 23278925

def subArraySum(arr, n, num):
    curr_sum = arr[0]
    start = 0
    for i in range(1, n+1):
        while curr_sum > num and start < i-1:
            curr_sum = curr_sum - arr[start]
            start+=1

        if curr_sum == num:
            print(sorted(arr[start:i])[0] + sorted(arr[start:i])[-1])
            return

        if i < n:
            curr_sum = curr_sum + arr[i]
    print("no subarray found")

with open("input9.txt", "r") as file:
    for line in file:
        line = line.strip()
        lst.append(int(line))

subArraySum(lst, len(lst), number)
