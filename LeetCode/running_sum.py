"""
Escribe una funcion que reciba un array de números enteros y devuelva un array con la suma acumulada de los elementos.

Ejemplo: 
- Input: [1,2,3,4]
- Output: [1,3,6,10]
"""

input = [1,2,3,4]


count = 0
output = []
for i in range(0, len(input)):
    count += input[i]
    output.append(count)

print(output)

def running_sum(nums):
    run_sum = 0 
    output = []
    for i in range(0, len(nums)):
        run_sum += nums[i]
        output.append(run_sum)
    return output

print(running_sum([1,2,3,4]))