def story():
    print('I will tell you a story, but I need some information first.')
    name = input('What is the main character called?\n')
    job = input('What is their job?\n')
    print('Once upon a time there was,', name, 'who was a', job,'.')
    print('On the way to work,', name, 'reflected on life.')
    print('Perhaps', name, 'will not be a', job, 'Data scientist forever.')


def main():
    # write your code below this line
    story()


if __name__ == '__main__':
    main()
