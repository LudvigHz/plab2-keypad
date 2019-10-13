"""Module contains class for the finite state machine"""

from keypad.finite_state_machine.rule import (STATES, Rule, signal_is_anything,
                                              signal_is_asterisk,
                                              signal_is_digit,
                                              signal_is_override)
from keypad.kpc_agent import KPCAgent


class FiniteStateMachine:
    """Rule-based finite state machine that asks agent for input, applies rules and reacts
    accordingly """

    _current_state = STATES.INIT
    _current_signal = None
    _rule_list: [Rule] = []
    _agent: KPCAgent = None

    def __init__(self, agent):
        """Add the correct rules to the rule list"""
        self._agent = agent
        self._rule_list = rules(agent)

    def add_rule(self, rule: Rule):
        """Appends a new rule to the end of the FSM’s rule list"""
        self._rule_list.append(rule)

    def _get_next_signal(self):
        """Query the agent for the next signal"""
        self._current_signal = self._agent.get_next_signal()

    def _run_rules(self):
        """Go through the rule set, in order, applying each rule until one of the rules is fired.
        Raises an exception if no rule is fired"""
        for rule in self._rule_list:
            if self._apply_rule(rule):
                self._fire_rule(rule)
                return
        raise Exception("NO RULE WAS FIRED")

    def _apply_rule(self, rule: Rule) -> bool:
        """Check whether the conditions of a rule are met"""
        if rule.match(self._current_state, self._current_signal):
            return True
        return False

    def _fire_rule(self, rule: Rule):
        """use the consequent of a rule to set the next state of the FSM AND call the appropriate
        agent action method"""
        self._current_state = rule.new_state
        rule.action(self._current_signal)

    def main_loop(self):
        """begin in the FSM’s default initial state and then repeatedly call get next signal and
        run rules until the FSM enters its default final state"""
        while self._current_state != STATES.END:
            self._get_next_signal()
            self._run_rules()
        self._agent.exit_action()


def rules(agent):
    """ List of the rules for the fsm """
    RULES = [
        Rule(STATES.INIT, signal_is_anything, STATES.READ, agent.init_passcode_entry),
        Rule(STATES.READ, signal_is_digit, STATES.READ, agent.append_password),
        Rule(STATES.READ, signal_is_asterisk, STATES.VERIFY, agent.verify_login),
        Rule(STATES.READ, signal_is_anything, STATES.INIT, agent.reset_agent),
        Rule(
            STATES.VERIFY, signal_is_override, STATES.ACTIVE, agent.fully_activate_agent
        ),
        Rule(STATES.VERIFY, signal_is_anything, STATES.INIT, agent.reset_agent),
        Rule(
            STATES.ACTIVE, signal_is_asterisk, STATES.READ2, agent.init_passcode_entry
        ),
        Rule(STATES.READ2, signal_is_digit, STATES.READ2, agent.append_password),
        Rule(
            STATES.READ2, signal_is_asterisk, STATES.READ3, agent.cache_first_password
        ),
        Rule(STATES.READ2, signal_is_anything, STATES.ACTIVE, agent.reset_agent),
        Rule(STATES.READ3, signal_is_digit, STATES.READ3, agent.append_password),
        Rule(
            STATES.READ3, signal_is_asterisk, STATES.ACTIVE, agent.compare_new_passwords
        ),
        Rule(STATES.READ3, signal_is_anything, STATES.ACTIVE, agent.reset_agent),
    ]
    return RULES
