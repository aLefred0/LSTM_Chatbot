# Deep Reinforcement Learning fo Dialogue Genereation
for text files please go to this link:https://drive.google.com/file/d/1mLNk5o4ea-2GH5Cj1YH7ESuXfjzlYKB3/view?usp=sharing

This repository contains code for implemetniting an LSTM SEQ2SEQ model with attention and an Encoder-decoder model which uses beam search(part of mutual information)
It mainly uses keras, tensorflow and gensim.


Probable Issues

Lack of computing power: My computer would crash during extended training so I spent a lot of time optmising my models.. So U had to break the training data into smaller chunks

Lack of computer RAM: I could not use a large vocabulary as the one-hot vectors would take up a lot of space. I tried a character level network but that was less efficient so I used a reduced vocabulary and linked similar words to expand the vocabulary using word vectors from glove using gensim’s similar().

The output would mainly consist of <pad>: This can be removed by either by removing <pad> from the output vocabulary or modifying the loss function to give more weightage to no <pad> words. BUt this function will use SGD.
  

Instructions to run

lstm_w_a.ipynb for the lstm with attention

voc_mod.ipynb is used to modify the vocabulary

beam_search_m_i.ipynb for beam search

simulation.ipynb was not finished
