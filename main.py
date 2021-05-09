def main() -> None:
    print('Kúp felszín és térfogat számolás!')
    R: float = float(input('r: '))
    M: float = float(input('m: '))
    S: float = float(input('s: '))
    Felszín: float = 0
    Térfogat: float = 0
    if R <= 0 or M <= 0 or S <= 0:
        print("Nullával és annál kisebb számmal nem lehet számolni")
    else:
        Felszín = 3.14 * R * (R + S)
        Térfogat = (1 / 3) * 3.14 * R ** 2 * M
        print(f'A Kúp felszíne: {Felszín} és a térfogata: {Térfogat}')


if __name__ == "__main__":
    main()
