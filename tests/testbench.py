from myhdl import *  # noqa: F403
from johnson_counter import jc2

ACTIVE, INACTIVE = bool(0), bool(1)


@block  # noqa: F405
def test():
    goLeft, goRight, stop, clk = [Signal(INACTIVE) for i in range(4)]  # noqa: F405
    q = Signal(intbv(0)[4:])  # noqa: F405

    @always(delay(10))  # noqa: F405
    def clkgen():
        clk.next = not clk

    jc2_inst = jc2(goLeft, goRight, stop, clk, q)

    @instance  # noqa: F405
    def stimulus():
        for i in range(3):
            yield clk.negedge
        for sig, nrcycles in ((goLeft, 10), (stop, 3), (goRight, 10)):
            sig.next = ACTIVE
            yield clk.negedge
            sig.next = INACTIVE
            for i in range(nrcycles - 1):
                yield clk.negedge
        raise StopSimulation  # noqa: F405

    @instance  # noqa: F405
    def monitor():
        print("goLeft goRight stop clk q")
        print("------------------------------")
        while True:
            yield clk.negedge
            yield delay(1)  # noqa: F405
            pStr = str(
                "{:^6} {:^6} {:^5} ".format(int(goLeft), int(goRight), int(stop))
            )
            yield clk.posedge
            pStr += " C "
            yield delay(1)  # noqa: F405
            pStr += " " + bin(q, 4)
            print(pStr)

    return clkgen, jc2_inst, stimulus, monitor


def convert():
    left, right, stop, clk = [Signal(INACTIVE) for i in range(4)]  # noqa: F405
    q = Signal(intbv(0)[4:])  # noqa: F405
    convInst = jc2(left, right, stop, clk, q)
    convInst.convert(hdl="VHDL", path="tests/output_files")


simInst = test()
simInst.config_sim(trace=False, tracebackup=False)
simInst.run_sim()

convert()
