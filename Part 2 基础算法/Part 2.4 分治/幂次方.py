def power_representation(n):
    if n == 0:
        return '0'
    result = []
    power = 0
    while n > 0:
        if n % 2 == 1:
            if power == 1:
                result.append('2')
            else:
                result.append(f'2({power_representation(power)})')
        power += 1
        n //= 2
    return '+'.join(result[::-1])

n = int(input().strip())

print(power_representation(n))