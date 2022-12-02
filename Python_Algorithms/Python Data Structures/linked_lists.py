from dataclasses import dataclass


@dataclass
class Nodes:
    data: str
    next_data: None


@dataclass
class LinkedList:
    head = None

    # Inserting at the start of the linked list
    def insert_start(self, start_val):
        node = Nodes(start_val, self.head)
        self.head = node

    # Inserting at the end of the linked list
    def insert_end(self, end_val):
        if self.head is None:
            self.head = Nodes(end_val, None)
            return

        itr = self.head
        while itr.next_data:
            itr = itr.next_data

        itr.next_data = Nodes(end_val, None)

    def insert_values(self, data_list: list):
        self.head = None
        for data in data_list:
            self.insert_end(data)

    def display(self):
        if self.head is None:
            print('Empty')
            return

        itr = self.head
        ll_str: str = ''
        while itr:
            ll_str += f'{str(itr.data)} --> '
            itr = itr.next_data
        print(ll_str)


def primes(n):
    n_list: list[int] = [i for i in range(1, n+1)]
    factors: int = 0
    for i, ele in enumerate(n_list):
        if n % ele == 0:
            factors += 1
    if factors > 2:
        return False
    return True


if __name__ == '__main__':
    ll = LinkedList()
    sample_nums = [n for n in range(1, 100)]
    primes_to_100: list[int] = list(filter(primes, sample_nums))
    # print(sample_nums)
    print(primes_to_100)
    ll.insert_values(primes_to_100)
    ll.display()

    # for i in range(1, 4):
    #     ll.insert_start(i)
    #     print(id(ll.head))
    # ll.insert_end(12)
    # ll.insert_end(28)
    # ll.insert_end(30)
    # ll.display()
