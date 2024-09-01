from myhdl import *  # noqa: F403
from sd import sd

@block  # noqa: F405
def testbench():
    Reset = ResetSignal(0, active=1, isasync=True)  # noqa: F405
    ck = Signal(bool(0))  # noqa: F405
    inicio = Signal(bool(0)) # noqa: F405
    entA = Signal(intbv(0)[4:])  # noqa: F405
    entB = Signal(intbv(0)[4:])  # noqa: F405
    mult = Signal(intbv(0)[4:])  # noqa: F405
    pronto = Signal(bool(0))  # noqa: F405

    sd_inst = sd(Reset, ck, inicio, entA, entB, mult, pronto)

    @always(delay(5))  # noqa: F405
    def clkgen():
        ck.next = not ck

    @instance  # noqa: F405
    def stimulus():
        Reset.next = 1
        yield ck.negedge
        Reset.next = 0
        yield ck.negedge
        entA.next = 4
        entB.next = 3
        inicio.next = 1
        yield delay(200)  # noqa: F405
        raise StopSimulation  # noqa: F405

    @instance  # noqa: F405
    def monitor():
        print("ck inicio entA entB mult pronto")
        print("-------------------------")
        while True:
            yield ck.posedge
            print(f"{int(ck)}  {int(inicio)}  {int(entA)}   {int(entB)}   {int(mult)}   {int(pronto)}")

    return sd_inst, clkgen, stimulus, monitor

def convert():
    Reset = ResetSignal(0, active=1, isasync=True)  # noqa: F405
    ck = Signal(bool(0))  # noqa: F405
    inicio = Signal(bool(0))  # noqa: F405
    entA = Signal(intbv(0)[4:])  # noqa: F405
    entB = Signal(intbv(0)[4:])  # noqa: F405
    mult = Signal(intbv(0)[4:])  # noqa: F405
    pronto = Signal(bool(0))  # noqa: F405
    convInst = sd(Reset, ck, inicio, entA, entB, mult, pronto)
    convInst.convert(hdl="VHDL", path="sam/hdl_files")
    # convTest = testbench()
    # convTest.convert(hdl="VHDL", path="sam/hdl_files")
    
tb = testbench()
tb.config_sim(trace=False, tracebackup=False)
tb.run_sim()

convert()