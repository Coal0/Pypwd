# Pypwd
_________
[![inner-strength.jpg](https://s13.postimg.org/878e7cf13/inner-strength.jpg)](https://postimg.org/image/bqubx5hqr/)
Pypwd is a nifty password generator coded in Python
_______________________________________________________________________________

# Description:
_______________
A secure password doesn't just have to include upper and lower case characters and numbers, it also has to be unpredictable.

For example, JohnSmith82 is of medium strength at least according to most password meters, but 7/10 online dictionaries contain it, those dictionaries are available online free of charge, making it vulnerable to dictionary attacks.

So I came up with a very simple algorithm that takes care of that problem by turning weak, 5 letter lowercase passwords to 20+ characters of unpredictable gibberish. You can easily reproduce the string anytime you want, and all you need to memorize: a short password, a multiplication key (optional), a seed (a number, which is optional too), and the positions of a couple special characters (optional as well).

Those optional values make the resulting pass much stronger, but even without them the resulting string will be practically unpredictable.

For more information, read the source code and the docstrings.

Feedback is welcome and appreciated, hope you find it useful.
