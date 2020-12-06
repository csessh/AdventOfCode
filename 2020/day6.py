#!/Users/thangdo/Documents/dev/csessh/bin/python

# People seem to think one liner is cool.
# Here's one for you:
print(sum([len(set(form.replace('\n', ''))) for form in open('test.txt', 'r').read().split('\n\n')]))

# Personally, I think one liner is lame.
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

