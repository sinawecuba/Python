# Expanded glossary with 10 programming terms
glossary = {
    'variable': 'A named location used to store data in memory.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A sequence of instructions that repeats until a condition is met.',
    'dictionary': 'A collection of key-value pairs used to store data.',
    'list': 'An ordered collection of items that can be changed.',
    'tuple': 'An ordered collection of items that cannot be changed.',
    'set': 'An unordered collection of unique items.',
    'class': 'A blueprint for creating objects.',
    'object': 'An instance of a class.',
    'module': 'A file containing Python code, such as functions and classes.'
}

# Loop through the glossary and print each term and its meaning
for term, definition in glossary.items():
    print(f"{term.title()}:\n\t{definition}\n")
