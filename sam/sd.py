from myhdl import *  # noqa: F403

# Definição dos estados do bloco de controle
states = enum("IDLE", "LOAD", "CHECK_B", "ADD", "SUB", "DONE")  # noqa: F405


@block  # noqa: F405
def sd(Reset, ck, entA, entB, mult, pronto):
    # Sinais internos
    state = Signal(states.IDLE)  # noqa: F405
    A = Signal(intbv(0)[4:])  # noqa: F405
    B = Signal(intbv(0)[4:])  # noqa: F405
    P = Signal(intbv(0)[4:])  # noqa: F405
    temp = Signal(intbv(0)[4:])  # noqa: F405

    @always_seq(ck.posedge, reset=Reset)  # noqa: F405
    def fsm():
        # print(f"State: {state}, A: {A}, B: {B}, P: {P}, pronto: {pronto}, mult: {mult}")
        if state == states.IDLE:
            pronto.next = 0
            if Reset == 0:
                state.next = states.LOAD
        elif state == states.LOAD:
            A.next = entA
            B.next = entB
            P.next = 0
            state.next = states.CHECK_B
        elif state == states.CHECK_B:
            if B != 0:
                state.next = states.ADD
            else:
                state.next = states.DONE
        elif state == states.ADD:
            temp.next = P + B
            if A == 0:
                state.next = states.DONE
            else:
                state.next = states.SUB

        elif state == states.SUB:
            P.next = temp
            A.next = A - 1
            if A == 0:
                state.next = states.DONE
            else:
                state.next = states.ADD
        elif state == states.DONE:
            mult.next = P
            pronto.next = 1
            state.next = states.IDLE

    return fsm
