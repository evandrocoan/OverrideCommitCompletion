

import sublime
import sublime_plugin

import os
import sys
import importlib

PACKAGE_ROOT_DIRECTORY = os.path.dirname( os.path.dirname( os.path.realpath( __file__ ) ) )
CURRENT_PACKAGE_NAME = os.path.basename( PACKAGE_ROOT_DIRECTORY ).rsplit('.', 1)[0]

utilities = importlib.import_module( CURRENT_PACKAGE_NAME + ".tests.utilities" )


class OverrideCommitCompletionUnitTests(utilities.BasicSublimeTextViewTestCase):

    def test_camel_case_word(self):
        self.setText( "OverwriteCompletionCommand", 9 )

        self.view.run_command( "overwrite_commit_completion" )
        self.assertEqual( "OverwriteCommitCompletionCommand", self.view.substr( sublime.Region( 0, self.view.size() ) ) )

    def test_snake_case_word(self):
        self.setText( "commit__assistant", 7 )

        self.view.run_command( "overwrite_commit_completion" )
        self.assertEqual( "commit_completion_assistant", self.view.substr( sublime.Region( 0, self.view.size() ) ) )


