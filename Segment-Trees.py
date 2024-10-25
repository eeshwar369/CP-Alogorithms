class SegTree:
    def __init__(self, l):
        self.len = l
        self.t = [0] * (4 * l)

    # Build Segment Tree -- build(a, 1, 0, len-1)
    def build(self, a, v, tl, tr):
        if tl == tr:
            self.t[v] = a[tl]
            return
        tm = (tl + tr) // 2
        self.build(a, 2 * v, tl, tm)
        self.build(a, 2 * v + 1, tm + 1, tr)
        self.t[v] = self.t[2 * v] + self.t[2 * v + 1]

    # Query input question is = [l, r] included -- query(1, 0, len-1, l, r)
    def query(self, v, tl, tr, l, r):
        if tl > r or tr < l:  # no overlap
            return 0
        if l <= tl and tr <= r:  # full overlap
            return self.t[v]
        
        # Partial Overlap
        tm = (tl + tr) // 2
        leftAns = self.query(2 * v, tl, tm, l, r)
        rightAns = self.query(2 * v + 1, tm + 1, tr, l, r)
        return leftAns + rightAns

    # Update at index id of nums to a value val -- update(1, 0, len-1, id, val)
    def update(self, v, tl, tr, id, val):
        if tl == id and tr == id:  # reached leaf node
            self.t[v] = val
            return
        if id > tr or id < tl:
            return
        
        tm = (tl + tr) // 2
        self.update(2 * v, tl, tm, id, val)
        self.update(2 * v + 1, tm + 1, tr, id, val)
        self.t[v] = self.t[2 * v] + self.t[2 * v + 1]

    # Overridden build function
    def build_tree(self, a):
        self.build(a, 1, 0, self.len - 1)

    # Overridden query function
    def query_range(self, l, r):
        return self.query(1, 0, self.len - 1, l, r)

    # Overridden update function
    def update_value(self, id, val):
        self.update(1, 0, self.len - 1, id, val)


# Testing the code
if __name__ == "__main__":
    n = 8
    a = [1, 2, 1, 4, 2, 3, 1, 1]
    
    seg_tree = SegTree(n)
    seg_tree.build_tree(a)
    
    # Build - View Build Data
    for i in range(n):
        print(seg_tree.query_range(i, i), end=" ")
    print()
    
    # Query - Range Query
    sum_range = seg_tree.query_range(1, 5)
    print("Sum for range id = 1 to id = 5 is:", sum_range)
    
    # Update - Point Update
    seg_tree.update_value(2, 10)  # at id=2, make the value = 10
    sum_range = seg_tree.query_range(1, 5)
    print("New Sum for range id = 1 to id = 5 is:", sum_range)
