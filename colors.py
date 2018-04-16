from termcolor import colored

# print(dir(termcolor))
# help(termcolor)
print(
    colored(
        'Hello, World!',
        color='green',
        on_color='on_blue',
        attrs=['blink']))
# print(termcolor.colored('Hello, World!', 'red', 'blink'))

print(
    colored(
        'Dmitri James Wamback',
        color='red',
        on_color='on_yellow',
        attrs=[
            'blink',
            'bold',
            'underline']))
