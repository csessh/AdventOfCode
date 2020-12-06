#!/Users/thangdo/Documents/dev/csessh/bin/python

# People seem to think one-liner is cool.
# Here's one for you:
print(sum([len(set(form.replace('\n', ''))) for form in open('test.txt', 'r').read().split('\n\n')]))

