from bin.graph import Linked_list

def test_linked_list():
    counter = 0
    ll = Linked_list()
    ll.append(1)
    counter += 1
    print(str(ll))
    ll.append(2)
    counter += 1
    print(str(ll))
    ll.append(4)
    counter += 1
    print(str(ll))
    ll.prepend(0)
    counter += 1
    print(str(ll))
    ll.insert(3, 2)
    counter += 1
    print(str(ll))
    ll.pop_head()
    counter -= 1
    print(str(ll))
    ll.pop_tail()
    counter -= 1
    print(str(ll))
    assert ll.length is counter
    for j in range(10):
        ll.prepend(j)
        print(str(ll))
    #try iterator
    i = ll.get_iterator()
    while i.has_next():
        print("iterating: ", str(i.next()))


def main():
    test_linked_list()

if __name__ == "__main__":
    main()