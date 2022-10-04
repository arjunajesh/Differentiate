import sys;

f = sys.argv[1]
comps = []
ops = []
left, right = 0, 0
op = ""

# Differentiates a polynomial term
def differentiate(comp):
    co = ""
    exp = 0
    x = comp.find("x")
    c = comp.find("^")
    if x == -1:
        return ""
    else:
        co = comp[0:x]
    if c == -1:
        return co
    else:
        exp = int(comp[c + 1:])

    # Power Rule
    newCo = int(co) * int(exp)
    exp -= 1

    if exp == 1:
        return str(newCo) + "x"
    else:
        return str(newCo) + "x^" + str(exp)

# Breaks down the polynomial expression into terms and operators
for i in range(len(f)):
    c = f[i]
    if i==len(f) - 1:
        comps.append(f[left:right+1])
    elif (c =="+" or c =="-") and i!=0:
        comps.append(f[left:right])
        ops.append(f[right])
        right += 1 
        left = right
    else:
        right+=1
print("Terms: ")
print(comps)

print("Operators: ")
print(ops)

# Composes the output polynomial 
i = 0
for x in comps:
    c = differentiate(x)
    if c == "":
        op = op[:-1]
        if i != len(comps) - 1:
            op += ops[i]
            i += 1
        continue
    op += differentiate(x)
    if x != comps[len(comps) -1]:
        op += ops[i]
        i += 1
print("\nDifferential: " )   
print(op)     


    
    