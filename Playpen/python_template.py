
build_template = """
py_binary(
    name = 'main',
    srcs = [
        'Main.py'
    ]
)
"""

file_content = """
def main():
    return 0

if __name__ == '__main__':
    print('### START ###')
    main()
    print('### END ###')

"""