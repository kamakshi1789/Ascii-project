import os
import msvcrt as msv
import time
import sys

# ------------------------- NEON COLORS -------------------------
RESET = "\033[0m"
NEON_PINK = "\033[95;1m"
NEON_BLUE = "\033[96;1m"
NEON_GREEN = "\033[92;1m"
NEON_YELLOW = "\033[93;1m"
NEON_RED = "\033[91;1m"
BOLD = "\033[1m"

# ------------------------- ANIMATION HELPERS -------------------------
def type_text(text, delay=0.001):
    """Typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar():
    """Sexy neon loading animation"""
    bar = "▰▰▰▰▰▰▰▰▰▰"
    type_text(NEON_BLUE + "\nLoading UI..." + RESET)
    for i in range(10):
        sys.stdout.write(NEON_GREEN + bar[:i] + RESET + "\r")
        sys.stdout.flush()
        time.sleep(0.07)
    print()

def neon_banner(text):
    print(NEON_PINK + BOLD + "═" * 80 + RESET)
    print(NEON_BLUE + BOLD + text.center(80) + RESET)
    print(NEON_PINK + BOLD + "═" * 80 + RESET)

def menu_option(num, text):
    print(f"{NEON_YELLOW} ➤ [{num}] {NEON_GREEN}{text}{RESET}")

# ------------------------- ASCII DATA -------------------------
data = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]

# ------------------------- CHAR INDEX -------------------------
def get_char_index(ch):
    if ch.isdigit(): return (ord(ch) - 17) * 6
    if ch == " ": return 26 * 6
    if ch == "@": return 27 * 6
    if ch == "_": return 28 * 6
    if ch == "-": return 29 * 6
    if ch == ".": return 30 * 6
    return (ord(ch) - 65) * 6

# ------------------------- PRINT ASCII -------------------------
def print_ascii(text):
    print()
    for row in data:
        line = ""
        for ch in text.upper():
            idx = get_char_index(ch)
            line += NEON_GREEN + row[idx:idx+6] + RESET
        print(line)
    print()

# ------------------------- MODULES -------------------------
def one_character():
    os.system("cls")
    neon_banner("🔥 ASCII ART - SINGLE CHARACTER 🔥")
    ch = input(NEON_YELLOW + " Enter ONE character: " + RESET).upper()

    if len(ch) != 1:
        print(NEON_RED + "❌ Please enter exactly ONE character!" + RESET)
        return

    loading_bar()
    print_ascii(ch)

def alpha_num_words():
    os.system("cls")
    neon_banner("✨ ASCII ART - WORDS ✨")
    text = input(NEON_YELLOW + " Enter up to 15 characters: " + RESET).upper()

    if not (1 <= len(text) <= 15):
        print(NEON_RED + "❌ Invalid length!" + RESET)
        return

    loading_bar()
    print_ascii(text)

def alpha_range():
    os.system("cls")
    neon_banner(" ASCII ART - RANGE A-D ")
    text = input(NEON_YELLOW + " Enter range like A-D: " + RESET).upper()

    if len(text) != 3 or text[1] != "-":
        print(NEON_RED + "❌ Invalid format!" + RESET)
        return

    start = ord(text[0]) - 64
    end = ord(text[2]) - 64

    if start > end or (end - start) >= 15:
        print(NEON_RED + "❌ Invalid range!" + RESET)
        return

    letters = "".join(chr(i + 64) for i in range(start, end + 1))
    loading_bar()
    print_ascii(letters)

def only_alpha():
    os.system("cls")
    neon_banner("🔤 ASCII ART - ONLY ALPHABETS 🔤")
    text = input(NEON_YELLOW + " Enter letters only (max 15): " + RESET).upper()

    if not text.isalpha():
        print(NEON_RED + "❌ Only alphabets allowed!" + RESET)
        return
    if not (1 <= len(text) <= 15):
        print(NEON_RED + "❌ Invalid length!" + RESET)
        return

    loading_bar()
    print_ascii(text)

def only_num():
    os.system("cls")
    neon_banner("🔢 ASCII ART - ONLY NUMBERS 🔢")
    text = input(NEON_YELLOW + " Enter digits only (max 15): " + RESET).upper()

    if not text.isdigit():
        print(NEON_RED + "❌ Only numbers allowed!" + RESET)
        return
    if not (1 <= len(text) <= 15):
        print(NEON_RED + "❌ Invalid length!" + RESET)
        return

    loading_bar()
    print_ascii(text)

# ------------------------- MAIN MENU -------------------------
def main_ui():
    while True:
        os.system("cls")
        neon_banner("🌟 ASCII ART PROJECT 🌟")

        menu_option("1", "One Character")
        menu_option("2", "Words (Max 15 Letters)")
        menu_option("3", "Range (A-D style)")
        menu_option("4", "Alphabet Only")
        menu_option("5", "Numbers Only")
        menu_option("6", "Exit")

        print("\n" + NEON_BLUE + BOLD + " ▶ Enter your choice: " + RESET, end="")
        ch = msv.getch().decode()

        if ch == "1":
            one_character()
        elif ch == "2":
            alpha_num_words()
        elif ch == "3":
            alpha_range()
        elif ch == "4":
            only_alpha()
        elif ch == "5":
            only_num()
        elif ch == "6":
            break

        print(NEON_YELLOW + "\n Press Y to continue, any other key to exit..." + RESET)
        again = msv.getch().decode()
        if again.lower() != "y":
            break

# Run
main_ui()
