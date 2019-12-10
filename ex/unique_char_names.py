def has_unique_chars(name):
    return len(name) == len(set(name))


names = ['Java', 'Python', 'JavaScript', 'Ruby', 'Rust', 'C++']

for n in filter(has_unique_chars, names):
    print(n)
