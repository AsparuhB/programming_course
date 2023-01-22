# Read input

price_sk = float(input())
price_c = float(input())
p_in_kg = float(input())
s_in_kg = float(input())
clam_kg = float(input())

# Logic
p_price = price_sk + price_sk * 0.60
s_price =  price_c + price_c * 0.80
clam_price = 7.5

palamud = p_price * p_in_kg
safrid = s_in_kg * s_price
clams = clam_price * clam_kg

total = palamud + safrid + clams

# Output

print(f"{total:.2f}")