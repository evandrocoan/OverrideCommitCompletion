


import os

import sublime
import sublime_plugin


words_to_do_function_callback = []
functions_to_do_callback = []


def add_function_word_callback(word_trigger, function_callback):
    functions_to_do_callback.append( function_callback )
    words_to_do_function_callback.append( word_trigger )


def do_function_callback(full_completed_word, view, edit):
    word_index = words_to_do_function_callback.index( full_completed_word )
    return functions_to_do_callback[word_index]( view, edit )


def find_word_end(view, completion_end_point):
    """
        This function is not used yet, but should be useful when dealing with completions which
        contain word boundary characters.
    """
    word_separators = view.settings().get("word_separators")
    maximum_attempts = 0
    current_end_point = completion_end_point

    while maximum_attempts < 10:
        maximum_attempts += 1
        next_characters = view.substr( sublime.Region( completion_end_point, completion_end_point + 50 ) )

        for characther in next_characters:
            current_end_point += 1

            if characther in word_separators:
                return current_end_point

    return completion_end_point


class OverwriteCommitCompletionCommand(sublime_plugin.TextCommand):
    """
        Complete whole word
        https://forum.sublimetext.com/t/complete-whole-word/26375

        It is possible to pass an array to a command without **kargs?
        https://forum.sublimetext.com/t/it-is-possible-to-pass-an-array-to-a-command-without-kargs/28969
    """

    def run(self, edit):
        view = self.view
        window = view.window()
        old_selections = []

        for selection in view.sel():
            old_selections.append( selection.end() )

        window.run_command( "commit_completion" )

        if old_selections:
            window.run_command( "overwrite_commit_completion_assistant", { "old_selections" : old_selections } )


class OverwriteCommitCompletionAssistantCommand(sublime_plugin.TextCommand):
    """
        Save the edit when running a Sublime Text 3 plugin
        https://stackoverflow.com/questions/20466014/save-the-edit-when-running-a-sublime-text-3-plugin
    """

    def run(self, edit, old_selections):
        """
            Since Sublime Text build ~3134, we need to wait until Sublime Text insert the completion.
        """
        view              = self.view
        selection_index   = 0
        completion_offset = 0

        for selection in view.sel():
            completion_end_point   = selection.end()
            duplicated_word_region = sublime.Region( completion_end_point, view.word( completion_end_point ).end() )
            duplicated_word        = view.substr( duplicated_word_region )
            part_completed_region  = sublime.Region( old_selections[ selection_index ] + completion_offset, completion_end_point )

            full_completed_region  = view.word( completion_end_point )
            full_completed_word    = view.substr( full_completed_region )

            # print( "selection:             " + str( selection ) )
            # print( "selection_word:        " + str( view.substr( selection ) ) )
            # print( "inserted_word:         " + view.substr( sublime.Region( view.word( completion_end_point ).begin(), completion_end_point ) ) )
            # print( "full_completed_region: " + str( full_completed_region ) )
            # print( "full_completed_word:   " + full_completed_word )
            # print( "duplicated_word:       " + duplicated_word )
            # print( "part_completed_word:   " + view.substr( part_completed_region ) )

            # inserted_word:       OverwriteCommitCompletionCommand
            # full_completed_word: OverwriteCommitCompletionCommandCommand
            # duplicated_word:     Command
            # part_completed_word: ompletionCommand
            if duplicated_word in view.substr( part_completed_region ):

                # print( "Erasing duplication: " + duplicated_word )
                view.erase( edit, duplicated_word_region )

                # When the completion is inserted we need to save the completion_offset to be able
                # correct the outdated selection points after the auto completion for the remaining
                # selections
                completion_offset += part_completed_region.size() - duplicated_word_region.size()

            if full_completed_word in words_to_do_function_callback:
                # print( "Erasing duplication: " + full_completed_word )

                view.erase( edit, full_completed_region )
                completion_offset += do_function_callback( full_completed_word, view, edit ) - full_completed_region.size()

            selection_index += 1


"""
OverwriteCommitCompletionCommand
OverwriteCommitCompletionCommand

overwrite_commit_completion_assistant
overwrite_commit_completion_assistant
"""


