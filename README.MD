
# Sublime Text Overwrite Commit Completion


Overrides the remaining word when the cursor is in the middle and the completion is performed.
The original version replaces any word after:

> [Quoting taras1] It seems that if the cursor is in the middle of the word the completion does not
> override the whole word but its left part only.

> In the sample below I would expected the get_|errors to be replaced with get_saved_doc|. However
> the result is get_saved_doc|errors

> ![](https://forum.sublimetext.com/uploads/default/original/3X/5/9/593a43a91aca20e7e821325f6c9bbe3c35559723.gif)


But this one:

> I wrote a variation where it only replaces the remaining word, if it is a subword of the completed
> word. I added this because most times I am adding new words before the some word, and when I use
> the completion for this new word it was deleting my word.

> ![](http://i.imgur.com/8aCUJod.gif)



### Bibliography

1. https://forum.sublimetext.com/t/complete-whole-word/26375


## License

All files in this repository are released under GNU General Public License v3.0
or the latest version available on http://www.gnu.org/licenses/gpl.html

1. The [LICENSE](LICENSE) file for the GPL v3.0 license
1. The website https://www.gnu.org/licenses/gpl-3.0.en.html

For more information.


