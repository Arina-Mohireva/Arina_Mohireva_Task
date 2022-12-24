from pprint import pprint

c = [{'bin': bin(x),
      'dec': x,
      'hex': hex(x),
      'oct': oct(x)} for x in range(16)]

pprint(c)

