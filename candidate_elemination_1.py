import csv

def read_dataset(file_path):
    examples = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            example = (int(row[0]), *row[1:])
            examples.append(example)
    return examples

def learn(concepts):
    specific_h = list(concepts[0][1:])
    general_h = [['?' for _ in range(len(specific_h))] for _ in range(len(specific_h))]

    print("Initial Specific_h:", specific_h)
    print("Initial General_h:", general_h)
    
    for i, h in enumerate(concepts[1:], start=1):
        if h[0] == 1:  # For positive examples
            for x in range(len(specific_h)):
                if h[x + 1] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        else:  # For negative examples
            for x in range(len(specific_h)):
                if h[x + 1] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
        
        print(f"\nAfter processing example {i} ({'Positive' if h[0] == 1 else 'Negative'}):")
        print("Specific_h:", specific_h)
        print("General_h:", general_h)

    general_h = [g for g in general_h if any(attr != '?' for attr in g)]

    return specific_h, general_h

if __name__ == '__main__':
    data = read_dataset('\DataSet\cand_1.csv')
    s_final, g_final = learn(data)

    print("\nFinal Specific_h:", s_final)
    print("Final General_h:", g_final)
    print("The hypothesis of the tested samples:",g_final)
    