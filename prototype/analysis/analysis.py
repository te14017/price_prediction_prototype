#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 12:50:31 2017

@author: tante, simon
"""
# templates for implementing transformers:
# https://github.com/scikit-learn-contrib/project-template/blob/master/skltemplate/template.py

import bestprice.utils as utils
import pandas as pd

# for further processing data
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.externals import joblib


class SparseToDenseTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_ = pd.DataFrame(data = X.toarray())
        return X_


class ScalingTransformer(BaseEstimator, TransformerMixin):
    """
    transform dataframe first by RobustScaler to lower down the influence of outliers,
    then transform it by MinMaxScaler to range (0,1)
    """
    def __init__(self, featureList, quantile_range=(25, 75)):
        # scaling continuous value features with RobustScaler
        self.quantile_range = quantile_range
        self.robust_scaler = RobustScaler(quantile_range=self.quantile_range)
        # further scaling data to range (0, 1)
        self.min_max_scaler = MinMaxScaler()
        self.featureList = featureList
            
    def fit(self, X, y=None):
        #print(X['starRating'].head())
        X_ = X.copy()
        self.robust_scaler.fit(X_[self.featureList])
        X_train_robust = self.robust_scaler.transform(X_[self.featureList])
        self.min_max_scaler.fit(X_train_robust)
        return self
        
    def transform(self, X):
        X_ = X.copy()
        X_train_robust = self.robust_scaler.transform(X_[self.featureList])
        X_[self.featureList]  = self.min_max_scaler.transform(X_train_robust)
        return X_
    

class TextFeatureTransformer(BaseEstimator, TransformerMixin):
    """
    transform 'text' feature in dataframe to either the text predicting result as a new feature, or
    to a dense matrix
    """

    def __init__(self, predictResultAsFeature=True):
        """
        @ predictResultAsFeature: whether use the prediction result of text feature as a new
        feature of original data. If it's False, transfer text into tf-idf dense matrix as a new feature
        """
        self.predictResultAsFeature = predictResultAsFeature
        # Tfidef transformer

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_ = X.copy()
        if self.predictResultAsFeature:
            text_freq = self.tfidf.transform(X_['text'])
            # use the best model to predict probability result of transformed text data
            predict = self.best_model.predict(text_freq)

            X_['text'] = predict
            print("===== text predict results transformed.")
        else:
            text_freq = self.tfidf.transform(X_['text'])
            # for i, col in enumerate(self.tfidf.get_feature_names()):
            # X_[col] = pd.SparseSeries(text_freq[:, i].toarray().ravel(), fill_value=0)
            df_dense = pd.DataFrame(data=text_freq.toarray())
            X_.drop('text', axis=1, inplace=True)
            X_ = pd.concat([X_, df_dense], axis=1)
            X_.fillna(0, inplace=True)
            print("======concat dense matrix  to dataFrame done !")
        return X_

