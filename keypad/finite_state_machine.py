"""Module contains class for the finite state machine"""


class FiniteStateMachine:
    """Rule-based finite state machine that asks agent for input, applies rules and reacts
    accordingly """

    def _add_rule(self):
        """Add a new rule to the end of the FSM’s rule list"""

    def _get_next_signal(self):
        """Query the agent for the next signal"""

    def _run_rules(self):
        """Go through the rule set, in order, applying each rule until one of the rules is fired"""

    def _apply_rule(self):
        """Check whether the conditions of a rule are met"""

    def _fire_rule(self):
        """use the consequent of a rule to set the next state of the FSM AND call the appropriate
        agent action method"""

    def _main_loop(self):
        """begin in the FSM’s default initial state and then repeatedly call get next signal and
        run rules until the
        FSM enters its default final state"""
