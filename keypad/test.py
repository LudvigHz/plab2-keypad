from keypad.finite_state_machine.finite_state_machine import FiniteStateMachine
from keypad.kpc_agent import KPCAgent

KP = KPCAgent()
FSM = FiniteStateMachine(KP)
FSM.main_loop()
