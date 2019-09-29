
# Sublime Text Overwrite Commit Completion

[![Build Status](https://travis-ci.org/evandrocoan/OverrideCommitCompletion.svg?branch=master)](https://travis-ci.org/evandrocoan/OverrideCommitCompletion)
[![Build status](https://ci.appveyor.com/api/projects/status/github/evandrocoan/OverrideCommitCompletion?branch=master&svg=true)](https://ci.appveyor.com/project/evandrocoan/OverrideCommitCompletion/branch/master)
[![codecov](https://codecov.io/gh/evandrocoan/OverrideCommitCompletion/branch/master/graph/badge.svg)](https://codecov.io/gh/evandrocoan/OverrideCommitCompletion)
[![Coverage Status](https://coveralls.io/repos/github/evandrocoan/OverrideCommitCompletion/badge.svg?branch=master)](https://coveralls.io/github/evandrocoan/OverrideCommitCompletion?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/58d1b714a900461998c933e36bfc5685)](https://www.codacy.com/app/evandrocoan/OverrideCommitCompletion?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=evandrocoan/OverrideCommitCompletion&amp;utm_campaign=Badge_Grade)
[![Latest Release](https://img.shields.io/github/tag/evandrocoan/OverrideCommitCompletion.svg?label=version)](https://github.com/evandrocoan/OverrideCommitCompletion/releases)
<a href="https://packagecontrol.io/packages/OverrideCommitCompletion"><img src="https://packagecontrol.herokuapp.com/downloads/OverrideCommitCompletion.svg"></a>

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


## Installation

### By Package Control

1. Download & Install **`Sublime Text 3`** (https://www.sublimetext.com/3)
1. Go to the menu **`Tools -> Install Package Control`**, then,
   wait few seconds until the installation finishes up
1. Go to the menu **`Tools -> Command Palette...
   (Ctrl+Shift+P)`**
1. Type **`Preferences:
   Package Control Settings – User`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
   add the following setting to your **`Package Control.sublime-settings`** file, if it is not already there
   ```js
   [
       ...
       "channels":
       [
           "https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json",
           "https://packagecontrol.io/channel_v3.json",
       ],
       ...
   ]
   ```
   * Note,
     the **`https://raw...`** line must to be added before the **`https://packagecontrol...`**,
     otherwise you will not install this forked version of the package,
     but the original available on the Package Control default channel **`https://packagecontrol...`**
1. Now,
   go to the menu **`Preferences -> Package Control`**
1. Type **`Install Package`** on the opened quick panel and press <kbd>Enter</kbd>
1. Then,
search for **`OverrideCommitCompletion`** and press <kbd>Enter</kbd>

See also:
1. [ITE - Integrated Toolset Environment](https://github.com/evandrocoan/ITE)
1. [Package control docs](https://packagecontrol.io/docs/usage) for details.


## Unit Tests

To run the unit tests:

1. Install the package: https://github.com/randy3k/UnitTesting
1. Open the file `unit_testing/override_commmit_completions_unit_tests.py`
1. Open the Sublime Text command palette with `Ctrl+Shift+P`
1. And run the command: `UnitTesting: Test Current Package`


### Bibliography

1. https://forum.sublimetext.com/t/complete-whole-word/26375


## License

All files in this repository are released under GNU General Public License v3.0
or the latest version available on http://www.gnu.org/licenses/gpl.html

1. The [LICENSE](LICENSE) file for the GPL v3.0 license
1. The website https://www.gnu.org/licenses/gpl-3.0.en.html

For more information.


