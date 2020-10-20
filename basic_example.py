import bspy


def foo(bsp: bspy.BSPObject):
    # Step 1
    if bsp.pid % 2 == 1:
        # Do 4 computations
        for _ in range(4):
            _ = 1

    # Do 4 more computations
    for _ in range(4):
        _ = 1

    bsp.sync()

    # Step 2
    if bsp.pid == 0:
        for id in range(1, 5):
            bsp.send('hi', id)

    bsp.sync()

    # Step 3
    if bsp.pid - 1 >= 0:
        bsp.send('hi', bsp.pid - 1)

    if bsp.pid + 1 < bsp.cores:
        bsp.send('hi', bsp.pid + 1)

    bsp.sync()

    # Step 4
    for _ in range(8 - bsp.pid):  # Note how every processor has 8 - pid computations.
        _ = 1

    bsp.sync()

    # Step 5
    if bsp.pid != 0:
        bsp.send('hi', 0)

    bsp.sync()


if __name__ == "__main__":
    bspy.run(foo, 5)
