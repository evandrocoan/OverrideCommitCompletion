

import unittest
import textwrap

import sublime
import sublime_plugin


def wrap_text(text):
    return textwrap.dedent( text ).strip( " " ).strip( "\n" )


class BasicSublimeTextViewTestCase(unittest.TestCase, sublime_plugin.EventListener):
    is_running_unit_tests = False

    @classmethod
    def setUp(self):
        self.maxDiff = None
        self.is_running_unit_tests = True

        # Create a new Sublime Text view to perform the Unit Tests
        self.view = sublime.active_window().new_file()
        self.view.set_syntax_file( "Packages/Text/Plain text.tmLanguage" )

        # make sure we have a window to work with
        settings = sublime.load_settings("Preferences.sublime-settings")
        settings.set("close_windows_when_empty", False)

    def tearDown(self):
        self.is_running_unit_tests = False

        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def setText(self, text, start_point=0):
        self.view.run_command("append", {"characters": text })

        selections = self.view.sel()
        selections.clear()
        selections.add( sublime.Region( start_point, start_point ) )

        self.view.window().focus_view( self.view )
        self.view.run_command( 'auto_complete', {'disable_auto_insert': True, 'next_completion_if_showing': False} )

    def assertEqual(self, expected, *args, **kargs):
        super().assertEqual(expected, self.view.substr( sublime.Region( 0, self.view.size() ) ), *args, **kargs)

    def on_query_completions(self, view, prefix, locations):

        if self.is_running_unit_tests:
            return \
            (
                [
                    "commit_completion_assistant",
                    "OverwriteCommitCompletionCommand",
                ],
                sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS
             )

        return None

