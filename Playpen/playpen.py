import python_template

def main():
    f = open('/tmp/BUILD', 'w')
    f.write(python_template.template)
    f.close()
    return 0
    


if __name__ == '__main__':
    print('start')
    main()
    