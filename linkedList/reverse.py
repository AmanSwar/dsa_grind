# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):


  before = None
  present = head

  after = present.next

  while(after):
    present.next = before
    before = present
    present = after
    after = after.next

  return present








