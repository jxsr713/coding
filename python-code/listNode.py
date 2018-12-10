#!/usr/bin/python3.3
import re
import os
import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None

class ListNode_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        #add a new node pointed to previous node
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print(" ", node.val, end="-->")
            node = node.next
        print("\n")

    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:
            result = result_handle.add(i)
        return result

    def get_list(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        return list

    def get_NodeList(self, nodelist):
        list = []
        while nodelist is not None:
            list.append(nodelist)
            nodelist = nodelist.next
        return list

    def sorted(self, nodelist):
        lst = self.get_NodeList(nodelist)
        lst.sort(key=lambda ListNode: ListNode.val)
        cur = lst[0]
        for node in lst:
            cur.next = node
            cur = node
            node.next = None
        return lst[0]

def dump_list(lst):
    ListNode_1 = ListNode_handle()
    print("--------DUMP LIST-------------")
    for lst in lst:
        ListNode_1.print_ListNode(lst)


def test_MerList(argLst):
    node_list = []
    ret_lst = []
    temp = -1
    debug = 1
    ListNode_1 = ListNode_handle()
    print("=================================")
    for node in argLst:
        cur = 0
        pre = -1
        val_0 = node.val
        for nd_temp in node_list:
            val_1 = nd_temp.val
            if val_1 > val_0:
                break;
            cur = cur + 1
        node_list.insert(cur, node)

    for lst in node_list:
        ListNode_1.print_ListNode(lst)
    minVal = 0

        
    node = ListNode()
    node.val = -1
    head = node
    cnt = 0
    while len(node_list):
        cnt = cnt + 1
        nd_cur = node_list.pop(0)
        if nd_cur.next:
            nd_next = nd_cur.next

            minVal = nd_cur.val

            print("[0]:", minVal , end="==")
            

            cur = 0
            val_0 = nd_next.val

            for lst in node_list:
                val_1 = lst.val
                if val_1 > val_0:
                    break;
                cur = cur + 1
            # nd_cur = nd_next
            node_list.insert(cur, nd_next)
        
        node.next = nd_cur;
        node = nd_cur

        
        if cnt > 26:
            dump_list(node_list);
            break;
    print("\n===Finished it=====")

    dump_list(node_list);
    print("====New List=====")
    ListNode_1.print_ListNode(head)


# test main function
if __name__ == '__main__':
    argc = len(sys.argv)
    arglst = sys.argv[2:]


    lst_listNode = []
    if len(arglst) != 0:
        Nlst = [ int(i) for i in arglst ]


    ListNode_1 = ListNode_handle()
    l1_list = [12 ,3 ,31,13,18,8]
    for i in l1_list:
        l1 = ListNode_1.add(i)

    sortedlst = ListNode_1.sorted(l1)
    ListNode_1.print_ListNode(sortedlst)

    exit()
    # creat 2 linked lists
    ListNode_1 = ListNode_handle()
    l1_list = [1, 3 ,10 ,17 ,26 ,31]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    l1 = ListNode_1._reverse(l1)
    lst_listNode.append(l1)

    ListNode_1 = ListNode_handle()
    l1_list = [3 ,6 ,15,17,18,29]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    l1 = ListNode_1._reverse(l1)
    lst_listNode.append(l1)

    ListNode_1 = ListNode_handle()
    l1_list = [2 ,3 ,5, 7, 11,19]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    l1 = ListNode_1._reverse(l1)
    lst_listNode.append(l1)

    ListNode_1 = ListNode_handle()
    l1_list = [1 ,3 ,11,13,18,28]
    for i in l1_list:
        l1 = ListNode_1.add(i)

    l1 = ListNode_1._reverse(l1)
    lst_listNode.append(l1)
    for lst in lst_listNode:
        ListNode_1.print_ListNode(lst)


#    lst_listNode.pop(0)

#    print("--------#################################-----------")            
#    for lst in lst_listNode:
#        ListNode_1.print_ListNode(lst)


    test_MerList(lst_listNode)

    dump_list(lst_listNode)



