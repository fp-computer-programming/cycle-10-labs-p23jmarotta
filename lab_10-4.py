# Creator JM 1/23/23

def indexed_names(names):
    result = []
    for i, v in enumerate(names):
        result.append(f"{str(i)}: {v}")
    print(result)

indexed_names(['John', 'Jane', 'Bob'])
indexed_names(['Joey', 'Timmy', 'John', 'Belinda', 'Melinda'])
