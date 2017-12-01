

import sublime
import sublime_plugin

from .overwrite_commit_completion import add_function_word_callback


starcomment_trigger = 'starcommentsnippet'

class InsertHeaderCompletionCommand(sublime_plugin.TextCommand):

    def on_query_completions(self, view, prefix, locations):
        return [(starcomment_trigger + ' \tsnippet', starcomment_trigger)]


def plugin_loaded():
    add_function_word_callback( starcomment_trigger, dynamic_character_lenght )


def dynamic_character_lenght(view, edit):
    """
        Snippet with dynamic character length
        https://forum.sublimetext.com/t/snippet-with-dynamic-character-length/33601
    """
    rulers = view.settings().get("rulers", [])
    maxlength = min(rulers) if rulers else 80
    if len(view.sel()) > 1:
        print("This doesn't work with more than one selection :(")
        return
    region = view.sel()[0]
    # If we have an empty region, assume we want to convert the whole line.
    if region.empty():
        region = view.line(region.begin())
    print('handling', view.substr(region), region)
    # -4 for '/** '
    # -1 for the space between the region and the start of the dashes.
    # Totals -5.
    dashlength = maxlength - region.size() - 5
    if dashlength < 0:
        print("Region is too large:", view.substr(region))
        return
    string = "/** {} {}\n * $0\n */".format(view.substr(region),
                                            "-" * dashlength)
    view.erase(edit, region)
    view.run_command("insert_snippet", {"contents": string})

    return len( string )


