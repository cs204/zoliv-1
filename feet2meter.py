def main():
    v2 = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v2} метров.")

def feet2meter(v2):
    dr = v2.replace("180.9ft", "55.14")
    return dr

main()