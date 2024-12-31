print('hi')
print('yo')

for i in range(4):
    print(i)
    
def greet(greeting, name):
    """Returns a greeting

    Args:
        greeting (string): a greeting word
        name (string): A name

    Returns:
        string: A greeting with a name
    """
    return f'{greeting} {name}'

print(greet('hello', 'World'))
