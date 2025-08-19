# Create a glossary of programming terms
glossary = {
    'variable': 'A named location used to store data in memory.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A sequence of instructions that repeats until a condition is met.',
    'dictionary': 'A collection of key-value pairs used to store data.',
    'list': 'An ordered collection of items that can be changed.'
}

# Print each word and its meaning
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")
    
