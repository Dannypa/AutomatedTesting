from colorama import Fore

color_test = Fore.LIGHTCYAN_EX
color_right = Fore.LIGHTGREEN_EX
color_wrong = Fore.RED
color_note = Fore.LIGHTMAGENTA_EX


def main():
    possible_colors = {Fore.RED: "Red", Fore.GREEN: "Green", Fore.YELLOW: 'Yellow', Fore.LIGHTGREEN_EX: "LightGreen",
                       Fore.LIGHTCYAN_EX: "LightCyan", Fore.LIGHTMAGENTA_EX: "LightMagenta", Fore.BLACK: "Black",
                       Fore.BLUE: "Blue", Fore.CYAN: "Cyan", Fore.LIGHTBLACK_EX: "LightBlack(?)",
                       Fore.LIGHTBLUE_EX: "LightBlue",
                       Fore.LIGHTRED_EX: "LightRed", Fore.LIGHTWHITE_EX: "LightWhite(???)",
                       Fore.LIGHTYELLOW_EX: "LightYellow",
                       Fore.MAGENTA: "Magenta", Fore.WHITE: "White"}
    print("Possible colors - and how do they look like.")
    for color in possible_colors:
        print(color + possible_colors[color])
    print(Fore.RESET + "Choose whatever you want, my friend^)")
    # if you want to change some color - just put its name next to where it should be used
    # For example:
    # color_wrong = Fore.GREEN
    # run program to see how do different colors look


if __name__ == '__main__':
    main()
