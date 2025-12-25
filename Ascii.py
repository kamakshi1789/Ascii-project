import os
import msvcrt as msv
import time
import sys

# ---------------- COLORS ----------------
RESET = "\033[0m"
NEON_GREEN = "\033[92;1m"
NEON_BLUE = "\033[96;1m"
NEON_PINK = "\033[95;1m"
NEON_YELLOW = "\033[93;1m"
NEON_RED = "\033[91;1m"
BOLD = "\033[1m"

# ---------------- EFFECTS ----------------
def type_text(text, d=0.001):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(d)
    print()

def loading():
    bar = "▰▰▰▰▰▰▰▰▰▰"
    type_text(NEON_BLUE + "\nLoading UI..." + RESET)
    for i in range(1, 11):
        sys.stdout.write(NEON_GREEN + bar[:i] + RESET + "\r")
        sys.stdout.flush()
        time.sleep(0.06)
    print()

def banner(t):
    print(NEON_PINK + BOLD + "═" * 80 + RESET)
    print(NEON_BLUE + BOLD + t.center(80) + RESET)
    print(NEON_PINK + BOLD + "═" * 80 + RESET)

def menu_option(n, t):
    print(f"{NEON_YELLOW} ➤ [{n}] {NEON_GREEN}{t}{RESET}")

# ---------------- ASCII DATA ----------------
# CAPITAL A–Z
data = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]

# lowercase (u/v broken internally)
data1 = [
    "***** *               *                   *       *       * *     *     ** **             *     ***   * **  *****   *         *   *  *   * ** ** *   * *****",
    "    * *     *****     * *****  **** ***** *               * *     *     * * * *   * ***** ***** * *   **  * *       *   *   * *   *  *   *  * *  *   *    * ",
    "* * * ***** *     ***** * * *  *  * ***** *****   *       * *  ** *     *   * * * * *   * *   * *** * *     ***** ***** *   * *   *  * * *   *   *****   *  ",
    "*   * *   * *     *   * *     ***       * *   *   *   *   * * *   *     *   * *  ** *   * *****    ** *         *   *   *   *  * *   * * *  * *      *  *   ",
    "***** ***** ***** ***** *****  *    ***** *   *   *   ***** *  ** ***** *   * *   * ***** *         * *     *****   *** *****   *    ** ** ** ** ***** *****"
]

# ---------------- INDEX ----------------
def get_index(ch):
    if ch.isupper():
        return (ord(ch) - 65) * 6
    if ch.islower():
        return (ord(ch) - 97) * 6
    if ch.isdigit():
        return (ord(ch) - 17) * 6
    if ch == " ":
        return 26 * 6
    return 0

# ---------------- PRINT ASCII (FINAL FIX) ----------------
def print_ascii(text):
    print()
    for r in range(5):
        line = ""
        for ch in text:
            idx = get_index(ch)

            if ch.islower():
                line += NEON_GREEN + data1[r][idx:idx+6] + RESET
            else:
                line += NEON_GREEN + data[r][idx:idx+6] + RESET

        print(line)
    print()


# ---------------- MODULES ----------------
def one_character():
    os.system("cls")
    banner("ASCII ART - ONE CHARACTER")
    ch = input("Enter ONE character: ")
    if len(ch) != 1:
        print(NEON_RED + "Only one character allowed!" + RESET)
        return
    loading()
    print_ascii(ch)

def words():
    os.system("cls")
    banner("ASCII ART - WORDS")
    text = input("Enter up to 15 characters: ")
    if not (1 <= len(text) <= 15):
        print(NEON_RED + "Invalid length!" + RESET)
        return
    loading()
    print_ascii(text)

def alpha_range():
    os.system("cls")
    banner("ASCII ART - RANGE (A-D)")
    text = input("Enter range like A-D: ")
    if len(text) != 3 or text[1] != "-":
        print(NEON_RED + "Invalid format!" + RESET)
        return
    letters = "".join(chr(i) for i in range(ord(text[0]), ord(text[2]) + 1))
    loading()
    print_ascii(letters)

def only_alpha():
    os.system("cls")
    banner("ASCII ART - ALPHABETS ONLY")
    text = input("Enter alphabets only: ")
    if not text.isalpha():
        print(NEON_RED + "Only alphabets allowed!" + RESET)
        return
    loading()
    print_ascii(text)

def only_num():
    os.system("cls")
    banner("ASCII ART - NUMBERS ONLY")
    text = input("Enter numbers only: ")
    if not text.isdigit():
        print(NEON_RED + "Only numbers allowed!" + RESET)
        return
    loading()
    print_ascii(text)

# ---------------- MAIN UI ----------------
def main():
    while True:
        os.system("cls")
        banner("🌟 ASCII ART PROJECT 🌟")

        menu_option("1", "One Character")
        menu_option("2", "Words")
        menu_option("3", "Range (A-D)")
        menu_option("4", "Alphabet Only")
        menu_option("5", "Numbers Only")
        menu_option("6", "Exit")

        print("\nChoice: ", end="")
        ch = msv.getch().decode()

        if ch == "1": one_character()
        elif ch == "2": words()
        elif ch == "3": alpha_range()
        elif ch == "4": only_alpha()
        elif ch == "5": only_num()
        elif ch == "6": break

        print("\nPress Y to continue...")
        if msv.getch().decode().lower() != "y":
            break

# ---------------- RUN ----------------
main()
