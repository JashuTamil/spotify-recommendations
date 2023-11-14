def sol(inp, out, truth):
    if not out and truth:
        print(truth)
    
    if out and not truth:
        print(out)

sol("gm", "mha", None)
sol("gm", None, "gvm")