

import sublime
import sublime_plugin

import unittest
import textwrap

import OverrideCommitCompletion.tests.testing.utilities
sublime_plugin.reload_plugin( "OverrideCommitCompletion.tests.testing.utilities" )


def wrap_text(text):
    return textwrap.dedent( text ).strip( " " ).strip( "\n" )


class OverrideCommitCompletionUnitTests(unittest.TestCase, sublime_plugin.EventListener):
    is_running_unit_tests = False

    @classmethod
    def setUp(self):
        self.maxDiff = None
        OverrideCommitCompletion.tests.testing.utilities.OverrideCommitCompletionUnitTestsEventListener.is_running_unit_tests = True

        # Create a new Sublime Text view to perform the Unit Tests
        self.view = sublime.active_window().new_file()
        self.view.set_syntax_file( "Packages/Text/Plain text.tmLanguage" )

        # make sure we have a window to work with
        settings = sublime.load_settings("Preferences.sublime-settings")
        settings.set("close_windows_when_empty", False)

    def tearDown(self):
        OverrideCommitCompletion.tests.testing.utilities.OverrideCommitCompletionUnitTestsEventListener.is_running_unit_tests = False

        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def setText(self, text, start_point, completion):
        OverrideCommitCompletion.tests.testing.utilities.OverrideCommitCompletionUnitTestsEventListener.completion = completion
        self.view.run_command("append", {"characters": text })

        selections = self.view.sel()
        selections.clear()
        selections.add( sublime.Region( start_point, start_point ) )

        self.view.window().focus_view( self.view )
        self.view.run_command( 'auto_complete', {'disable_auto_insert': True, 'next_completion_if_showing': False} )

    def assertEqual(self, expected, *args, **kargs):
        super().assertEqual(expected, self.view.substr( sublime.Region( 0, self.view.size() ) ), *args, **kargs)

    def test_camel_case_word(self):
        self.setText( "OverwriteCompletionCommand", 9, "OverwriteCommitCompletionCommand" )

        self.view.run_command( "fix_commit_completion" )
        self.assertEqual( "OverwriteCommitCompletionCommand" )

    def test_snake_case_word(self):
        self.setText( "commit__assistant", 7, "commit_completion_assistant" )

        self.view.run_command( "fix_commit_completion" )
        self.assertEqual( "commit_completion_assistant" )


