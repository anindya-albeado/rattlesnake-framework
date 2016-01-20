# Table of Contents #


# Introduction #
Thank you for your interest.
In this section it's explained how to become an active developer, helping us to improve the Rattlesnake Project.
If you need help contact the project manager at _mola89@gmail.com_ or other developers.
I suggest you to read some help manuals and guides. You can find them in the help section.

Remember that it is and it will always be **open source** and **free**.
# How to develop #
## Release schedule ##
How is the typical release schedule?
A release of Rattlesnake is identified by:
`version.core_majrel.contrib_rel`

When all features described on the [Roadmap](Roadmap.md) of a release are implemented a `core_majrel` is released.<br />
After ten `core_majrel` a new `version` is released.<br />
If an extension is included in the contrib part of the framework, a `contrib_rel` is released.

## The most important thing ##
A project has to be well organized. You can develop your ideas without discussing it in the [Issue Tracker](https://code.google.com/p/rattlesnake-framework/issues/list), but it's very very important that every ideas are discussed by a lot of developers, possibly in the [Issue Tracker](https://code.google.com/p/rattlesnake-framework/issues/list).
The _brainstorming phase_ of the development of a feature is the most important, because a project organized well is that it has been analyzed in each of its parts.
So, the main features that are implemented are those discussed in the [Issue Tracker](https://code.google.com/p/rattlesnake-framework/issues/list) posts tagged as a Enhancement.
## Core and Contrib ##
You can decide to develop the Core of the framework or the Contrib part. What's the difference? `*`

It's Simple:
  * **Core**
> What is the Core of Rattlesnake? It's like a kernel for a computer. What does it mean?
> The core it's the necessary part of the framework. If you want to use Rattlesnake, you have to use the Core. In the core there're the main features of the framework, like the _Jobs Scheduler_, the _Memory Management System_, the _Exception Handlers_, the _Input Manager_, the _Parameters Manager_, etc.. (For a complete list of the Core features, read the Reference).
  * **Contrib**
> What is the Contrib part of Rattlesnake? Why does it exist?
> The Contrib part of the framework can be called the <em>Extension part</em>. Everything that it isn't in the core it's an extension.
> An extension depends from the core and it should be independent from other extensions.
> So, I want to develop a new feature. Do I have to develop it in the Core or in Contrib?
> It depends. If it's a library that it's used by other libraries, it should be in the Core; if it isn't, it should be in Contrib. If it's something that it's used by users and not by other libraries it has to be in Contrib, if it isn't it has to be in the Core.
> Remember that contrib features have to be tested and so, if they're stable and usable, they're included in the Contrib part of the official framework.
## Core development ##
A diagram would be more explanatory than a paragraph:

![http://lh3.ggpht.com/_YFrKaQj9Z88/SxlHDG5VPHI/AAAAAAAAAJk/vjhYIGwnJYU/core_dev_cycle.png](http://lh3.ggpht.com/_YFrKaQj9Z88/SxlHDG5VPHI/AAAAAAAAAJk/vjhYIGwnJYU/core_dev_cycle.png)
  * **Point (1)**:
> The major features ready to be developed are in the Feature Request tracker tagged as _Major_ (look at the tracking paragraph 3).
> A feature is ready when it's discussed and approved in the brainstorming page.
> After making code-changes you should post a comment in the Feature Request tracker; so the other developers are well syncronized, understanding what is already implemented and what needs to be revised.
  * **Point (2)**:
> The minor features ready to be developed are in the Feature Request tracker tagged as _Minor_. You mustn't post a comment in the Feature Request tracker, but it would be better.
## Contrib development ##
A diagram would be more explanatory than a paragraph:

![http://lh5.ggpht.com/_YFrKaQj9Z88/SxlJPkcBBpI/AAAAAAAAAJs/ltBYOkq6LaI/contrib_dev_cycle.png](http://lh5.ggpht.com/_YFrKaQj9Z88/SxlJPkcBBpI/AAAAAAAAAJs/ltBYOkq6LaI/contrib_dev_cycle.png)
  * **Point (1)**:
> There's more freedom about the Contrib development. The extensions can be developed by individual developers or by a group of them. It's recommended to be discussed in the brainstorming page.
## How to become operative ##
    1. Read the [Documentation](Documentation.md) for understanding how Rattlesnake works
    1. Check the [Issue Tracker](https://code.google.com/p/rattlesnake-framework/issues/list) to understand what should be developed or fixed.
    1. In the [Roadmap](Roadmap.md) page you can examine what has to be developed for the next release
    1. If you have some questions please contact the project admin at _mola89@gmail.com_
    1. If you need the code reference go to [Reference](Reference.md)
# Issue Tracking System #
# Tools #
There are some useful tools that can help you to perform a better job.
## Subversion ##
When you develop you should use a subversion client (for example [Rapid SVN](http://www.rapidsvn.org/index.php/Main_Page)).
After making changes to the code you can upload it using the configured client.
### Configuration of the subversion client ###
The first time you use the repository you have to checkout it.
It requires the following fields:
  * **Svn repository**: It's the following: https://rattlesnake-framework.googlecode.com/svn. When it askes you which directory in the repository you want to use write _trunk_
  * **Work directory**: The work directory has to be your local project dir.
### How to use the subversion client ###
There are 3 main commands in a subversion client:
  * **Svn add**: You add a folder (or file) to the version control, so when you execute a commit command that folder (or file) is uploaded.
  * **Commit**: You upload the files in the repository, uploading the files in the svn repository.
  * **Update**: You download the files from the repository, replacing the files in your project directory.
There are other important commands in SVN, you can check the details in the following guide: http://svnbook.red-bean.com/nightly/en/svn-book.pdf
## Development Environment ##
First of all you need [Python](http://python.org).
You can use an editor, like:
  * [Kate](http://kate-editor.org) (Linux).
  * [Notepad++](http://notepad-plus.sourceforge.net) (Win).
  * [jEdit](http://www.jedit.org) (Multiplatform).
Or you can use an Integrated Development Environment (_IDE_), like:
  * [Eclipse](http://www.eclipse.org) with [PyDev](http://pydev.org) (Multiplatform). It's the _recommended Development Environment_.
  * [Netbeans](http://www.netbeans.org) with the [Python plugin](http://download.netbeans.org/netbeans/6.7/python/ea2) (Multiplatform).
# Guidelines #
This project mainly follows:
  * **[Zen of Python](http://www.python.org/dev/peps/pep-0020)**
  * **[Style guide for the python code](http://www.python.org/dev/peps/pep-0008)**
  * **[DocString conventions](http://www.python.org/dev/peps/pep-0257)**