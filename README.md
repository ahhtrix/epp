Acme.Buffy Python
=================

Port of Perl module [Acme::Buffy](https://metacpan.org/pod/Acme::Buffy) in Python


A simple test
-------------

1. Run essai.py script :

```
    $ python3 essai.py
    Ceci est un test !
```

2. The new encoded file essai_buffy.py appears. Show it, run it :

```
    $ more essai_buffy.py
    import Acme.Buffy

    'buFfy bUFfy buFfy bUFFy buFfy buFfY buFfy bUfFy buFfy Buffy buffY bUFFY buffY bUFFy bufFy BuffY buFfy buffY bufFY BUffy buFfy buFfY buffY buFFY buFfy buffY buFfy bUFFY buFfy Buffy buffY buF
FY buFfy BuffY buFfy bUfFy buffY buFFY buFfy Buffy buFfy buffY buFfy bUFFY buFfy Buffy buffY buFFY buffY bUffy buffY bUFFy buffY Buffy '

    $ python3 essai_buffy.py
    Ceci est un test !
```

License
-------

This program is distributed under GPLv3 license (see [here](LICENSE.md)).
