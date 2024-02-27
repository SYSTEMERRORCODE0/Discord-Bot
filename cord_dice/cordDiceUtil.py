ERROR_ONE_INVALID_ARGUMENT = "error one invalid argument"
ERROR_TWO_INVALID_ARGUMENT = "error two invalid argument"
ERROR_HELP = "error help"
ERROR_NOT_DEFINED = "error not defined"

aliases = ['d', 'dice', 'Dice', 'D']

# argument helps
one_argument_help = f">d N : 1 ~ N 값 중 하나가 나옵니다. N 은 1 이상의 정수"
two_argument_help = f">d N M : N ~ M 값 중 하나가 나옵니다. N, M 은 정수, N <= M"

help = f"명령어 prefix : 주사위, {', '.join(aliases)}\n" \
       f"{one_argument_help}\n" \
       f"{two_argument_help}"

# error descriptions
error_one_invalid_argument = "인수가 잘못되었습니다!\n" \
                             f"{one_argument_help}"
error_two_invalid_argument = "인수가 잘못되었습니다!\n" \
                             f"{two_argument_help}"
