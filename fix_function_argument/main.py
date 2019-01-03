def main():
    functions = []
    for i in range(10):
        functions.append(lambda i=i: i)

    for f in functions:
        print(f())


if __name__ == '__main__':
    main()
