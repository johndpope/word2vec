#/datastore/zhenyang/bin/python

import sys
import os
import gensim, logging
import numpy as np
import scipy.io as sio


def main():

    ##############
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    #pretrained_model = './vectors.bin'
    #pretrained_model = '../freebase-vectors-skipgram1000-en.bin'
    #pretrained_model = '../GoogleNews-vectors-negative300.bin'
    #model = gensim.models.Word2Vec.load_word2vec_format(pretrained_model, binary=True)
    #pretrained_model = './vectors.output'
    pretrained_model = '../yahoo_100m_words_30d.output'
    model = gensim.models.Word2Vec.load_word2vec_format(pretrained_model, binary=False)

    ##############
    classnames = open('shoes_gclasses_vps.txt', 'r').read().splitlines()

    cc = 0
    clsid = 0
    vec_size = 30
    word2vec_mat = np.zeros((len(classnames), vec_size))
    for classname in classnames:
        idc = 1
        for cls in classname.split(';'):
            wordvec = np.zeros(1, vec_size)
            for cls_word in cls.split(' '):
                try:
                    wordvec = np.add(wordvec, model[cls_word])
                    idc = 0
                
                except:
                    print cls_word
                    idc = 1
                    break
            if idc == 0:
                break

        word2vec_mat[clsid, :] = wordvec

        clsid = clsid + 1
        cc = cc + idc

    #np.savetxt('attr_word2vec_GoogleNews.txt', word2vec_mat)
    #sio.savemat('attr_word2vec_GoogleNews.mat', {'word2vec':word2vec_mat})
    np.savetxt('shoes_word2vec_yahoo_30d.txt', word2vec_mat)
    sio.savemat('shoes_word2vec_yahoo_30d.mat', {'word2vec':word2vec_mat})
    print cc

if __name__ == "__main__":
    main()