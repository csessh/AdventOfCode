#!/Users/thangdo/Documents/dev/csessh/bin/python

# People seem to think one liner is cool.
# Here's one for you:
print(sum([len(set(form.replace('\n', ''))) for form in open('test.txt', 'r').read().split('\n\n')]))

# Personally, I think one liners are lame.
with open('test.txt', 'r') as f:
    groups = f.read().split('\n\n')

    count = 0
    for group in groups:
        choices = []
        people = group.split('\n')

        for choice in people:
            choices.append(set(choice))

        common_questions = set.intersection(*choices)
        if common_questions:
            count += len(common_questions)

    print(count)

# However, a kind redditor (u/alexisloiselle97) offered theirs:
print(sum([len(set.intersection(*[set(v) for v in g.split('\n')])) for g in open('test.txt', 'r').read().split('\n\n')]))
