# прописал только логитку
def rectangle_part():
    rect_a = RectangleWorks.rectangle_create(100, 100)
    rect_b = RectangleWorks.rectangle_create(100, 100)

    try:
        rect_a = RectangleWorks.rectangle_create(11, -14)
    except RectangleValueError as exc:
        print(f'{exc.__class__.__name__}: {exc}')
    try:
        rect_b = RectangleWorks.rectangle_create(14, 'a')
    except RectangleValueError as exc:
        print(f'{exc.__class__.__name__}: {exc}')
    try:
        rect_e = RectangleWorks.rectangle_sum(rect_a, 10)
    except RectangleTypeError as exc:
        print(f'{exc.__class__.__name__}: {exc}')
    try:
        rect_e = RectangleWorks.rectangle_sub(rect_a, 'a')
    except RectangleTypeError as exc:
        print(f'{exc.__class__.__name__}: {exc}')
    rect_c = RectangleWorks.rectangle_sum(rect_a, rect_b)
    rect_d = RectangleWorks.rectangle_sub(rect_a, rect_b)
    print(rect_c)
    print(rect_d)