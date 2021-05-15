def solution(a, b):
    import math
    """
    1... xy -2x -2y +4 = b
    2... xy = (a + b) -> y = (a+b)/x
    -> a + b - 2x -2(a+b)/x + 4 = b y 대입
    -> ax + bx -2x^2 - 2(a+b) + 4x = bx 정리
    ->  - 2x^2 - 2(a+b) + (4+a)x = 0 정리
    -> 2x^2 - (4+a)x + 2(a+b) = 0
    [ x = (-b + sqrt(b^2 - 4ac))/2a ]
    x = ((4+a) + math.sqrt((4+a) ** 2 -4 * 2 * 2 * (a+b)) / 4
    """
    x = ((4+a) + math.sqrt((4+a) ** 2 - 4 * 2 * 2 * (a+b))) // 4
    y = (a+b) // x
    horizon = x if x >= y else y
    vertical = y if x == horizon else x
    return [horizon, vertical]