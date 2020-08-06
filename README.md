# muse_finder
Like a '90's-era website, it returns something based on something else.


muse_finder_example.py provides an example usage. Based on someone's birthday, you are able to find their "muses."

Who are someone's muses? Well, they're the two leading actors, of the top grossing movie, of the box-office week they were born. *Obviously!*

Some functions will also allow you to return the name of the movie or the box office week, if you so choose.

**Important usage note:** A full call to determine someone's muses requires 3 HTTP get requests to boxofficemojo.com. It would be unwise to run this too many times, as it wastes bandwidth. If you want a full-featured application, it would be better to just scrape all the box office weekly leaders a single time, then build a database of them plus the two lead actors and perform a lookup when you want to reveal someone's muses.
