class Sll_node:
    def __init__(self, data, next=None):
        self.data_ = data
        self.next_ = next
    
    def has_data(self, data):
        return self.data_ is data

class Sll_iterator:
    def __init__(self, sll_root):
        self.node_ = sll_root
    
    def has_next(self):
        if self.node_ is not None:
            return True
        else:
            return False
    
    def next(self):
        data = self.node_.data_
        self.node_ = self.node_.next_
        return data


class Linked_list:
    def __init__(self, root=None):
        self.root_ = root
        self.length = 0
    
    def get_iterator(self):
        return Sll_iterator(self.root_)

    def append(self, data):
        r = self.root_
        if r is None:
            self.root_ = Sll_node(data)
        else:
            while r.next_:
                r = r.next_
            r.next_ = Sll_node(data)
        self.length += 1
    
    def prepend(self, data):
        n = Sll_node(data)
        n.next_ = self.root_
        self.root_ = n
        self.length += 1
    
    def pop_tail(self):
        r = self.root_
        q = None
        while r.next_:
            q = r
            r = r.next_
        q.next_ = None
        self.length -= 1
        return r.data_
    
    def pop_head(self):
        r = self.root_
        self.root_ = r.next_
        self.length -= 1
        return r.data_

    def find(self, data):
        r = self.root_
        while r.next_:
            if r.has_data(data):
                return r
            else:
                r = r.next_
    
    def insert(self, data, after):
        n = self.find(after)
        m = None
        if n.next_ is None:
            n.next_ = Sll_node(data)
        else:
            m = Sll_node(data, n.next_)
            n.next_ = m
        self.length += 1
    
    def __str__(self):
        string = ""
        i = self.get_iterator()
        while i.has_next():
            string += str(i.next())
            string += " --> "
        string += "*"
        return string
