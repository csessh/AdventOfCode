#!/Users/thangdo/Documents/dev/csessh/bin/python


my_ticket = []
nearby_tickets = []
criteria = {}


def extract_values_from_train_info(info: str):
    global criteria
    for pair in [x.strip() for x in info.split(' or ')]:
        start, end = pair.split('-')
        for x in range(int(start), int(end)+1):
            criteria[x] = True


def get_scanning_error_rate() -> int:
    global criteria
    invalid_tickets = []

    for ticket in nearby_tickets:
        if ticket not in criteria:
            invalid_tickets.append(ticket)

    print(f'Invalid tickets: {invalid_tickets}')
    return sum(invalid_tickets)


if __name__ == '__main__':
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
                    line = line[starting_index+1:].strip()
                    extract_values_from_train_info(line)
                except ValueError:
                    pass

                if is_my_ticket_section:
                    my_ticket = [int(x) for x in line.split(',')]
                elif is_nearby_tickets_section:
                    nearby_tickets += [int(x) for x in line.split(',')]

    # Part 1
    print(f'Error scanning error rate = {get_scanning_error_rate()}')