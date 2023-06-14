def solution(arr, delete_list):
    check = set(delete_list)
    answer = [i for i in arr if i not in check]
    return answer
