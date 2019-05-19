def ngrams(input, n):
  input = input.split(' ')
  output = {}
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output

ret = ngrams('a a a a', 2) # {'a a': 3}
print(ret)

##############
def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

input_list = ['all', 'this', 'happened', 'more', 'or', 'less']
find_ngrams(input_list, 1)
#[('all',), ('this',), ('happened',), ('more',), ('or',), ('less',)]
find_ngrams(input_list, 2)
#[('all', 'this'), ('this', 'happened'), ('happened', 'more'), ('more', 'or'), ('or', 'less')]
print(find_ngrams(input_list, 3))
#[('all', 'this', 'happened'), ('this', 'happened', 'more'), ('happened', 'more', 'or'), ('more', 'or', 'less')]

