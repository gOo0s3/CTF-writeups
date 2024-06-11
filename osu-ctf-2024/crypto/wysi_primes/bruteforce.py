import random
from Crypto.Util.number import isPrime, bytes_to_long

def wysi_primes(num_primes):
    while True:
        prime_candidate = int(''.join(random.choices("72", k=272)))
        if isPrime(prime_candidate):
            yield prime_candidate

n = 2160489795493918825870689458820648828073650907916827108594219132976202835249425984494778310568338106260399032800745421512005980632641226298431130513637640125399673697368934008374907832728004469350033174207285393191694692228748281256956917290437627249889472471749973975591415828107248775449619403563269856991145789325659736854030396401772371148983463743700921913930643887223704115714270634525795771407138067936125866995910432010323584269926871467482064993332990516534083898654487467161183876470821163254662352951613205371404232685831299594035879
for prime in wysi_primes(n):
    print(f"attempting p={str(prime)[:40]}...", end="\r")
    if n % prime == 0:
        print(f"Found q&p: p={prime}, q={n//prime}")
        break
