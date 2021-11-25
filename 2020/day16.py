from typing import List


class Ticket:
    criteria = []

    def __init__(self, values: List[int]):
        self._values = values
        self._is_valid = True

    def get_error_rate(self) -> int:
        rate = 0
        for _, value in enumerate(self._values):
            if any(a <= value <= b or c <= value <= d for _, (a, b, c, d) in Ticket.criteria):
                continue

            self._is_valid = False
            rate += value
        return rate

    @property
    def is_valid(self) -> bool:
        return self._is_valid

    @property
    def values(self) -> List[int]:
        return self._values


if __name__ == '__main__':
    my_ticket = None
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
                    """
                    We're parsing ticket criteria here. For example:
                        departure location: 29-458 or 484-956 --> ("departure location", [29, 458, 484, 956])
                    """
                    header = line[:line.index(':')]
                    values = line[line.index(':')+1:].strip().replace(' or ', '-').split('-')
                    values = list(map(int, values))
                    Ticket.criteria.append((header, values))
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
    product = 1
    columns = set(range(len(Ticket.criteria)))
    for _ in range(len(Ticket.criteria)):
        for index, field in enumerate(Ticket.criteria):
            header, [a, b, c, d] = field

            candidates = []
            for col in columns:
                if all(a <= ticket.values[col] <= b or c <= ticket.values[col] <= d for ticket in valid_nearby_tickets):
                    candidates.append(col)

            if len(candidates) == 1:
                columns.remove(candidates[0])
                Ticket.criteria.pop(index)
                if header.startswith('departure'):
                    product *= my_ticket.values[candidates[0]]
                break
    print(f'Part 2: Departure product = {product}')