#!/Users/thangdo/Documents/dev/csessh/bin/python


from typing import List, Dict


class Ticket:
    criteria = {}

    def __init__(self, details: List[int]):
        self._info = details
        self._headers = {
            'departure location': None,
            'departure station': None,
            'departure platform': None,
            'departure track': None,
            'departure date': None,
            'departure time': None,
            'arrival location': None,
            'arrival station': None,
            'arrival platform': None,
            'arrival track': None,
            'class': None,
            'duration': None,
            'price': None,
            'route': None,
            'row': None,
            'seat': None,
            'train': None,
            'type': None,
            'wagon': None,
            'zone': None
        }
        self._is_valid = None


    @property
    def departure_product(self) -> int:
        return 0

    def get_error_rate(self) -> int:
        rate = 0

        for index, value in enumerate(self._info):
            is_valid = False
            for header, check in Ticket.criteria.items():
                if check[0] <= value <= check[1] or check[2] <= value <= check[3]:
                    is_valid = True
                    break

            if is_valid:
                continue

            self._is_valid = False
            rate += value
        return rate

    @property
    def is_valid(self) -> bool:
        if self._is_valid is None:
            self.get_error_rate()

        return self._is_valid

    @property
    def headers(self) -> Dict[str, int]:
        return self._headers


if __name__ == '__main__':
    my_ticket = []
    nearby_tickets = []

    with open('test.txt', 'r') as f:
        is_my_ticket_section = False
        is_nearby_tickets_section = False

        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                continue

            if line.startswith('your ticket:'):
                is_my_ticket_section = True
                is_nearby_tickets_section = False
            elif line.startswith('nearby tickets:'):
                is_my_ticket_section = False
                is_nearby_tickets_section = True
            else:
                try:
                    starting_index = line.index(':')
                    values = line[starting_index+1:].strip().split(' or ')
                    header = line[:starting_index]

                    Ticket.criteria[header] = []
                    for value in values:
                        start, end = value.split('-')
                        Ticket.criteria[header] += [int(start), int(end)]
                except ValueError:
                    pass

                if is_my_ticket_section:
                    my_ticket = Ticket([int(x) for x in line.split(',')])
                elif is_nearby_tickets_section:
                    nearby_tickets += [Ticket([int(x) for x in line.split(',')])]


    # Part 1
    error_rate = 0
    valid_nearby_tickets = []
    for ticket in nearby_tickets:
        error_rate += ticket.get_error_rate()
        if ticket.is_valid:
            valid_nearby_tickets.append(ticket)

    print(f'Part 1: Scanning Error Rate = {error_rate}')

    # Part 2