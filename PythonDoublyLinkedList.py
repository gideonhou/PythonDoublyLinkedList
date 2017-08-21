'''
Python implementation of doubly linked list
'''

class DoublyLinkedList(object):

    '''
    Default constructor
    '''
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.type = None

    '''
    This method returns size of LL
    '''
    def size(self):
        return self.size;

    '''
    This method clears the LL
    '''
    def clear(self):
        curr = self.head; # delete from head to tail
        toDel = curr; # pointer to node to delete. Trails curr pointer
        while curr is not None:
            curr = curr.next_node;
            toDel.next_node = None; # remove pointers of trailing pointer
            toDel.prev_node = None;

        self.head = None;   # remove head and tail pointers
        self.tail = None;
        self.type = None;   # reset type
        self.size = 0;      # set size to 0
        return True;
    
    '''
    This method inserts at end of LL
    '''
    def insert(self, input_val):
        if(self.size is 0): # do this if LL is empty
            self.type = type(input_val);
            self.head = Node(input_val);
            self.tail = self.head;
            self.size += 1;
            return True;

        else: # do this if LL is not empty
            if(not isinstance(input_val, self.type)):
               return False; # if input_val is not the correct type, exit

            curr = self.head;

            while(curr.next_node != None): # iterate to last node of list
                curr = curr.next_node;

            toAdd = Node(input_val); # create new instance of Node to add to LL
            curr.next_node = toAdd;
            toAdd.prev_node = curr;
            self.size += 1;
            self.tail = toAdd;
            return True;

    '''
    This method gets the element at the input index
    '''
    def get(self, index):
        if((not isinstance(index, int)) and (self.size < index)):
            return False; # make sure input is integer and input is not larger than LL size
        counter = 0; # counter
        curr = self.head; # curr pointer
        while curr is not None: # iterate until counter reaches index
            if counter is index:
                return curr.data;
            else:
                counter += 1;
                curr = curr.next_node;

        return False; # code shouldn't end up here
    
    '''
    This method deletes the first occurence of inpujt
    '''
    def delete(self, input_val):
        #if(not isinstance(input_val, self.type)):
        if(type(input_val) is not self.type):

            return False; # make sure target element is of type self.type

        if self.size is 0:
            return True; # nothing to delete
        
        curr = self.head; # Curr pointer. Search from head to tail

        if self.head.data is input_val: # if the head node is the matched node
            
            self.head = curr.next_node; # change pointers pointing to first node
            #self.head.prev_node = None;

            curr.next_node = None; # remove curr's pointers
            curr.prev_node = None;
            curr = None;
            
            self.size -= 1;     # decrement size
            if self.size is 0:  # if LL is now empty, call clear to set head, tail, and type attributes to None
                self.clear();

            return True;
                
        while curr is not None:
            if curr.data is input_val: # if a match is found, delete the node curr points to
                
                curr.prev_node.next_node = curr.next_node; # set the nodes around the matched node to point to each other
                if(curr.next_node is not None):
                    curr.next_node.prev_node = curr.prev_node;
                else:
                    self.tail = curr.prev_node;
                    
                self.size -= 1;
                return True;
            else:   # else iterate to next node in LL
                curr = curr.next_node;

        return False; # input_val not found

    '''
    This method sorts the LL
    '''
    def sort(self):

        if self.size < 2:
            return; # return if the list is empty or has one element

        sort_end = self.head;           # these two pointers will be used to sort the LL. to_move trails sort_end
        to_move = sort_end.next_node;
        #print to_move.data + sort_end.data

        while to_move is not None:

            if to_move.data < self.head.data: # check if to_move is less than the head. If yes, switch these nodes
                #print to_move.data + sort_end.data
                to_move_prev = to_move.prev_node;
                to_move_next = to_move.next_node;

                if to_move_prev is not None: to_move_prev.next_node = to_move_next;
                if to_move_next is not None: to_move_next.prev_node = to_move_prev; # move pointers of nodes surrounding to_move

                self.head.prev_node = to_move;
                to_move.next_node = self.head;
                to_move.prev_node = None;

                self.head = to_move;

                to_move = sort_end.next_node;
            elif to_move.data < sort_end.data: # if to_move is less than the end of the sorted list, begin moving

                it = sort_end;
                while to_move.data < it.data and it is not None:
                    it = it.prev_node;              # iterate along the linked list

                to_move_prev = to_move.prev_node;
                to_move_next = to_move.next_node;

                if to_move_prev is not None: to_move_prev.next_node = to_move_next;
                if to_move_next is not None: to_move_next.prev_node = to_move_prev; # move pointers of nodes surrounding to_move

                new_to_move_prev = it;
                new_to_move_next = it.next_node;

                new_to_move_prev.next_node = to_move;
                new_to_move_next.prev_node = to_move;

                to_move.prev_node = new_to_move_prev;
                to_move.next_node = new_to_move_next;
                
                to_move = sort_end.next_node;
            else:
                sort_end = sort_end.next_node;
                to_move = sort_end.next_node;

        self.tail = sort_end;
        
        return;

    '''

    '''
    
    '''
    This method returns all nodes in a tuple
    '''
    def get_list(self):
        ret = list();
        curr = self.head;
        while curr is not None:
            ret.append(curr.data);
            curr = curr.next_node;

        return ret;
    
'''
Class for nodes
'''
class Node(object):

    def __init__(self, input_val):
        self.data = input_val;
        self.next_node = None;
        self.prev_node = None;

    '''
    comparison method for nodes
    '''
    def compareTo(self, arg0):
        return cmp(self.data, arg0.data);
