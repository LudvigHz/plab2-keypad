"""Module contains class for the finite state machine"""
from keypad.finite_state_machine.rule import Rule


class FiniteStateMachine:
    """Rule-based finite state machine that asks agent for input, applies rules and reacts
    accordingly """

    _current_state = None
    _current_signal = ''
    _rule_list: list[Rule] = []

    def __init__(self):
        # TODO implement
        return

    def _add_rule(self, rule: Rule):
        """Add a new rule to the end of the FSM’s rule list"""
        self._rule_list.add(rule)

    def _get_next_signal(self) -> str:
        """Query the agent for the next signal"""

    def _run_rules(self):
        """Go through the rule set, in order, applying each rule until one of the rules is fired.
        Raises an exception if no rule is fired"""
        for rule in self._rule_list:
            if self._apply_rule(rule):
                self._fire_rule(rule)
                return
        raise Exception('NO RULE WAS FIRED')

    def _apply_rule(self, rule: Rule) -> bool:
        """Check whether the conditions of a rule are met"""
        if rule.match(self._current_state, self._current_signal):
            return True
        return False

    def _fire_rule(self, rule: Rule):
        """use the consequent of a rule to set the next state of the FSM AND call the appropriate
        agent action method"""
        self._current_state = rule.get_new_state()
        # TODO call agent.do_action(rule.get_action)

    def _main_loop(self):
        """begin in the FSM’s default initial state and then repeatedly call get next signal and
        run rules until the FSM enters its default final state"""
        while self._current_state != 'END':
            self._current_signal = self._get_next_signal()
            self._run_rules()
