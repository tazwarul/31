def Toh(n, src, aux, dest):
    if n == 1:
        print(f"Move disk - {n} from {src} To {dest}")
        return

    Toh(n - 1, src, dest, aux)
    print(f"Move disk - {n} from {src} To {dest}")
    Toh(n - 1, aux, src, dest)
