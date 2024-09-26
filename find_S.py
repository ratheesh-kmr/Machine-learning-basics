def find_s(data):
    
    hypothesis = None
    for instance in data:
        if instance[-1] == 'yes':  
            hypothesis = instance[:-1]
            break
        
    print("Most Specific hypothesis: ['0','0','0','0','0','0']")
    
    if hypothesis is None:
        raise ValueError("No positive instances found in the data.")
    
    num_attributes = len(hypothesis)

    for instance in data:
        if instance[-1] == 'yes':  # Only update hypothesis for positive instances
            for i in range(num_attributes):
                if instance[i] != hypothesis[i]:
                    hypothesis[i] = '?'
            print("Current hypothesis:", hypothesis)  # Print hypothesis state for each positive instance

    return hypothesis

# Example usage:
data = [
    ['circle', 'triangle', 'circle', 'pink', 'spike', 'yes'],
    ['square', 'square', 'box', 'green', 'spike', 'no'],
    ['square', 'triangle', 'circle', 'yellow', 'spike', 'yes'],
    ['circle', 'triangle', 'circle', 'green', 'bald',  'no'],
    ['square', 'square', 'circle', 'yellow', 'spike',  'yes']
]
final_hypothesis = find_s(data)
print("Final hypothesis:", final_hypothesis)