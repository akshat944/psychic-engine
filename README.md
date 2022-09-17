# psychic-engine
For a password to be secure, the certain conditions must be met. The password:
    a. Must at least contain 8 characters. 
    b. Must not contain any words (length >=3) that exist in the English language as a substring, e.g “123helloxyz678” is not        a secure password. Use the module “english_words_set” from the ‘english-words’ library for this purpose. Reference 
    c. Must contain at least one lower case letter [a-z]. 
    d. Must at least contain one uppercase letter [A-Z] other than at the beginning or the end: e.g. Abc34562 and abc2345D are        not secure passwords. 
    e. Must contain at least one digit [0-9] other than at the beginning or the end. 
    f. Must contain at least one special character from the set {‘#’, ‘$’, ‘%’, ‘&amp;’, ‘!’} other than at the beginning or          the end.
