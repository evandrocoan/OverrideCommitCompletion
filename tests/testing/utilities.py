

import sublime
import sublime_plugin


class OverrideCommitCompletionUnitTestsEventListener(sublime_plugin.EventListener):
    is_running_unit_tests = False

    def on_query_completions(self, view, prefix, locations):

        if self.is_running_unit_tests:
            return \
            (
                [
                    (self.completion, self.completion),
                ],
                sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS
             )

        return None

