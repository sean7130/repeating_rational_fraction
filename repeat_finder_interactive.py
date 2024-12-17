import keyboard

from math import gcd
# from sys import argv

DEBUG = False

_vd = [str(i) for i in range(10)]
_vd.append(".")
VALID_DIGITS = set(_vd)

INPUT = ""
PERIOD_TRACKER = []
PREVIOUS_CHAR = ""

def print_debug():
    print(f"p={PERIOD_TRACKER}, prev_char={PREVIOUS_CHAR}")

def check_period(p=PERIOD_TRACKER):
    max_period = 0
    full_input = p[0]
    for i in range(len(p)-2, len(p)//2, -1):
        test_period_str = p[i]
        test_period = len(test_period_str)
        if test_period_str == full_input[2*(-test_period):len(full_input)-test_period]:
            max_period = test_period
    return max_period


def perform_backspace():
    global INPUT
    global PREVIOUS_CHAR
    INPUT = INPUT[:-1]
    PREVIOUS_CHAR = INPUT[-1] if len(INPUT) > 0 else ""
    for i in range(len(PERIOD_TRACKER)):
        PERIOD_TRACKER[i] = PERIOD_TRACKER[i][:-1]
    if len(PERIOD_TRACKER) > 1: del(PERIOD_TRACKER[-1])

def seperate_repeats(decimals, period):
    # keep checking rtl for each period, so that it still follows the repeat pattern
    # this step is actually not needed but it will help precision on long numbers
    period_string = PERIOD_TRACKER[-(period+1)]
    i = 1
    while (period * (i+1)) <= len(decimals) and period_string == decimals[-(period * (i+1)):-(period* i)]:
        i += 1
    i -= 1
    return decimals[:-(period*(i+1))], decimals[-(period*(i+1)):]


def _produce_blunt_overall_fraction(non_repeating, non_repeating_factor, repeating, repeating_factor):
    blunt_d = (10**repeating_factor - 10**non_repeating_factor)
    blunt_overall_d = blunt_d * (10**non_repeating_factor)
    blunt_repeating_n = repeating * (10**non_repeating_factor)
    blunt_n = blunt_repeating_n + (non_repeating * blunt_d)
    return blunt_overall_d, blunt_n


def simplify_fractions(d, n):
    mutral_gcd = gcd(d, n)
    return d//mutral_gcd, n//mutral_gcd


def _produce_fraction(user_input, max_period):
    if not max_period or len(PERIOD_TRACKER) == 0:
        return "<No fraction yet>", -1, -1
    decimal_and_fraction = PERIOD_TRACKER[0].split('.')
    if len(decimal_and_fraction) != 2:
        return "<No fraction yet>", -1, -1
    non_repeating, repeating = seperate_repeats(decimal_and_fraction[1], max_period)

    # piece together the repeating and non repeating part 
    non_repeating_int = int(decimal_and_fraction[0] + non_repeating) if (decimal_and_fraction[0] + non_repeating) != "" else 0
    repeating_int = int(repeating)
    repeating_int_multiplication_factor = len(repeating) + len(non_repeating)
    blunt_denominator = (10**repeating_int_multiplication_factor-10**len(non_repeating))
    # print(f"confirmed_input={PERIOD_TRACKER[0]}, repeating={repeating_int}, non_repeating={non_repeating_int}")
    # print(f"repeating's factor={repeating_int_multiplication_factor}, non repeating's factor={len(non_repeating)}")
    # print(f"blunt-fraction: {repeating_int}/{blunt_denominator} = {repeating_int/blunt_denominator}")

    d, n = _produce_blunt_overall_fraction(non_repeating_int, len(non_repeating), repeating_int, repeating_int_multiplication_factor)
    d, n = simplify_fractions(d, n)
    # print(f"results: {n}/{d}={n/d}")
    return f"{n}/{d}={n/d}", n, d

def _clear():
    global INPUT
    global PREVIOUS_CHAR
    INPUT = ""
    PREVIOUS_CHAR = ""
    PERIOD_TRACKER.clear()
    # print(f"{argv[0]}: cleared.")
    # print_debug()

def clear():
    _clear()

def register_input(user_input):
    global INPUT
    global PREVIOUS_CHAR
    INPUT += user_input
    for i in range(len(PERIOD_TRACKER)):
        PERIOD_TRACKER[i] += PREVIOUS_CHAR
    # only use previous char because the current one may be the one with rounding errors
    PREVIOUS_CHAR = user_input
    PERIOD_TRACKER.append("")
    # print_debug()


def produce_fraction():
    if INPUT != "":
        mp = check_period()
    else:
        mp = 0

    return _produce_fraction(INPUT, mp)


if __name__ == "__main__":
    print(f"\r\033[KWelcome! Start typing a repeating decimal to determine its fraction form", end="", flush=True)
    while True:
        e = keyboard.read_event()
        if e.event_type == "down":
            if e.name == "esc" or e.name == "q":
                print("\nbye!")
                exit(0)
            elif e.name == "d":
                if DEBUG: print_debug()
            elif e.name == "enter":
                print("")
                _clear()
            elif e.name == "c":
                _clear()
                # print(f"period str = {PERIOD_TRACKER[-(mp+1)]}")
                print(f"\r\033[Kcurrent input: <cleared>", end="", flush=True)
            elif e.name == "backspace":
                perform_backspace()

            elif e.name in VALID_DIGITS:
                register_input(e.name)

            frac, n, d = produce_fraction()

            print(f"\r\033[Kcurrent input: {INPUT}, equivalent fraction form: {frac}", end="", flush=True)

