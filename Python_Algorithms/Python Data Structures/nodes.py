from dataclasses import dataclass


class DayNames:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


@dataclass()
class LinkedList:
    node: str
    next_node = None

    def __repr__(self):
        return self.node


if __name__ == '__main__':
    # e1 = DayNames('Mon')
    # e2 = DayNames('Tue')
    # e3 = DayNames('Wed')
    # e4 = DayNames('Thu')
    # e5 = DayNames('Fri')
    #
    # e1.next_val = e2
    # e2.next_val = e3
    # e3.next_val = e4
    # e4.next_val = e5


    def traversal(current_val) -> list[str]:
        links: list[str] = []
        while current_val:
            print(f'memory adrress: {id(current_val.node)}, {current_val}')
            links.append(current_val)
            current_val = current_val.next_node
        return links

    no_1 = LinkedList('One')
    no_2 = LinkedList('Two')
    no_3 = LinkedList('Three')
    no_4 = LinkedList('Four')

    no_1.next_node = no_2
    no_2.next_node = no_3
    no_3.next_node = no_4

    curr_val = no_1

    data: list[str] = traversal(curr_val)
    print(data)
    data_addr = [id(i) for i in data]
    print(data_addr)

    # this_val = e1

    # while this_val:
    #     print(f'memory address: {id(this_val.data_val)} value: {this_val.data_val}')
    #     this_val = this_val.next_val
