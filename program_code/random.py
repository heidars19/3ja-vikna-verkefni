class something:
    
    def __init__(self):
        pass
    
    
new = something()


if isinstance(new, something):
    print('Error!')
else:
    print('success!')