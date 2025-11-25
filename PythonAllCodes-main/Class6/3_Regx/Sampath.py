input = "aaabbccdeeffdg"

def function(input):
  for i,c in enumerate(input):
    print(len(input)-1)
    if((i== 0 or input[i-1] !=c) and ((i== len(input)-1 or input[i+1]) !=c)):
      return c 

      def function(input):
    for i, c in enumerate(input):
        # Check if current char differs from both neighbors
        if ((i == 0 or input[i-1] != c) and 
            (i == len(input)-1 or input[i+1] != c)):
            return c
    return None  # Explicit return when no unique character found

function(input)