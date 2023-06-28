def main():
    g = input()
    g12 = convert(g)
    print (g12)

def convert(g):
    g12 = g.replace(":)", "\N{Slightly Smiling Face}").replace(":(", "\N{Slightly Frowning Face}")
    return g12

main()