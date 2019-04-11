def find_four(data):
  secound = ''
  for i in data:
    if i == '4':
      secound += '1'
    else:
      secound += '0'
  return int(secound)


if __name__ == '__main__':
    for case in range(int(input())):
        n = int(input())
        s = find_four(str(n)) 
        print('Case #{}: {} {}'.format(case+1, s, n-s))