# What, in your opinion, is an important part of code reviews?

'''
In my experience, the most important parts of code review is coherence, logic,
and reproducibility.  These all feed into one another in the sense that logical,
coherent, easy to understand code, allows for reproducibility.
'''


# That is, what is something you pay attention to when you review code, and
# that you appreciate when others do the same for your code?

'''
Things that stick out to me when reviewing code, is the goldi-lock commenting;
commenting enough where the code is easy to follow (following along someone
else's thorugh process is a difficult thing to perform through text), and
commenting enough to where the files do not become muddied.  The kind of
feedback I appreciate comes in the form of code minimization.  Where I do
something in 5 lines, someone else can do it in 3, I'll gladly take that
critique.
'''


# We have an awful lot of computers here, and it gets pretty confusing with
# slightly different things running on all of them. How could containers help
# us improve this situation?

'''
Containers improve situatiions such as this by simply creating an executable
package called an image. This image contains all of the information necessary
to run code for an app, including config files, the dependencies, and anything
else associated with a given app.  By doing this, in a significantly smaller
package, we bypas the necessity for so many computers with dedicated environments
for virtual machines.
'''
