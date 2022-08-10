
template = """
py_binary(
    name = 'main',
    srcs = [
        'main.py'
    ]
)
"""

content = """
def main():
    return 0

if __name__ == '__main__':
    print('### START ###')
    main()
    print('### END ###')

"""