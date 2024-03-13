"""
Link to Problem -> https://leetcode.com/problems/add-two-numbers/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions
"""

def getReverseNumber(l:list)-> int:
    if len(l) == 1:
        return l[0]
    num = 0
    for item in l[::-1]:
        # print(item)
        num = num*10 + item 
        # print(num)
    return num

def getReverseList(num: int)-> list:
    sumList = []
    while num!=0:
        sumList.append(num % 10)
        num = num // 10
    # print(sumList)
    if len(sumList)==0:
        sumList.append(0)
    return sumList

def AddTwoNumbers(l1: list, l2: list) -> list:
    num1 = getReverseNumber(l1)
    num2 = getReverseNumber(l2)
    sum = getReverseList(num1 + num2)
    return sum

def getListNode()->list:
    # print("Enter The first List Node: ")
    l1 = list(map(int, input().strip().split()))
    # print("Enter The second List Node: ")
    l2 = list(map(int, input().strip().split()))
    return l1,l2

def main()->None:
    l1, l2 = getListNode()
    sum = AddTwoNumbers(l1,l2)
    print(sum)
    
if __name__ == "__main__":
    main()

""""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        mem = 0
        temp = 0
        signal = 1
        while(l1 or l2):
            temp+=mem
            mem = 0
            if(l1 and l2 and signal == 1):
                temp += l1.val + l2.val
                mem = temp // 10
                temp = temp % 10
                l1.val = temp
                if(l1.next == None):
                    signal = 0
                    if(l2.next == None and mem > 0):
                        l1.next = ListNode(val = mem)
                        break
                    l2 = l2.next
                    l1.next = l2
                    l1 = l1.next
                elif(l2.next == None):
                    signal = 0
                    l1 = l1.next
                    l2.next = l1
                    l2 = l2.next
                else:
                    l1 = l1.next
                    l2 = l2.next

            elif(signal == 0 ):
                l1.val += temp
                mem = l1.val // 10
                l1.val = l1.val % 10
                if(l1.next == None and mem != 0):
                    l1.next = ListNode(val = mem)
                    break
                l1 = l1.next
                l2 = l2.next
            temp = 0



        return head
"""