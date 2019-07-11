import re


def main():
    with open('./a.txt') as f:
        result = set()
        for line in f:
            arr = line.replace('(', ' ').replace('\t', ' ').replace(')', ' ').replace(',', ' ').split()
            # arr = re.split('|(|, |\t|)', line
            result = result.union(set([int(i) for i in arr]))
        return list(result)


if __name__ == '__main__':
    print(main())
