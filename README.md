
Using Temporal Word Embeddings to Study Semantic Change in Neologisms
---------

As language changes and words shift in meaning, these developments are in addition re-flected in cultural change. For instance, a language—in which words move in and out of a dynamic lexicon—displays the ideas and inventions that a culture might value. In this way, examining changes in lexicon possibly reveals significant aspects about the state of our society. Hence, it may be valuable to examine neologisms (newly coined words or ex-pressions) as a certain phenomenon of language change. More specifically, analyzing the semantic developments which occur during the early existence of a neologism could provide us with further insight into cultural shifts. 

HOW TO:
---------
1. Download the [sliced corpus](https://www.dropbox.com/sh/pf8dripkoqo8wzb/AABhwGhUocRLUoacCCL_sAYua?dl=0)  into `comment_data/1-mil-comm-per-month/`. **OR** download the [raw files](https://files.pushshift.io/reddit/comments/) on your own into `comment_data/tobewrited` 
2. Run `prepare_data.py` to create an atemporal compass based on the downloaded corpus.
3. Run `TWEC_master/train_model.py` to train the model. See the [TWEC GitHub page](https://github.com/valedica/twec) for the requirements, etc.

**WIP:** Some toy data is included, with the intention that there will be toy models as well.

Data
---------
Reddit corpus:
https://www.dropbox.com/sh/pf8dripkoqo8wzb/AABhwGhUocRLUoacCCL_sAYua?dl=0

Pushshift.io: 
https://files.pushshift.io/reddit/comments/

Reference
---------

This work is based on the following paper <https://aaai.org/ojs/index.php/AAAI/article/view/4594>

+ Di Carlo, V., Bianchi, F., & Palmonari, M. (2019). **Training Temporal Word Embeddings with a Compass**. Proceedings of the AAAI Conference on Artificial Intelligence, 33(01), 6326-6334. https://doi.org/10.1609/aaai.v33i01.33016326

Git:  <https://github.com/valedica/twec>

