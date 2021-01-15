#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:37:11 2021

Class to read IceCube simulations generated by ARTS
Can read in either one file or a list of files

@author: inderpreet
"""


import scipy.io
import numpy as np
import matplotlib.pyplot as plt



class IceCube():
      
    
    def __init__(self, filenames):
        """
        Class to read IceCube simulations generated by ARTS
        ----------
        filenames : string/list of strings containing the filename(s)

        Returns
        -------
        None.

        """
        
        if np.isscalar(filenames):
            print ('doing only one file')
            filenames = [filenames]
        self.mat = []
        for file in filenames:
            self.mat.append(scipy.io.loadmat(file))
            m = scipy.io.loadmat(file)
            
            if m["Tb"].shape[1] != m["iwp"].shape[0]:
                raise Exception("dimensions of TB, lat, iwp not consistent ")
            
        
    def get_data(self, parameter):    
        """
        method to read in the data from *.mat file   
    
            Parameters
        ----------
        parameter : string containing name of the parameter to be extracted

        Returns
        -------
        data : np.array of requested data

        """
        
        if parameter not in ["Tb", "iwp", "lat"]:
            raise Exception("parameter should be one of Tb, iwp or lat")
        
        
        data = []
        for i in range(len(self.mat)):
            mat = self.mat[i]
            data.append(mat[parameter])
        return data
    
    @property
    def tb(self):
        """
        brightness temperatures

        Returns
        -------
        np.array of TB values

        """
        tb = self.get_data('Tb')
        tb = np.concatenate(tb, axis = 1)
        return np.squeeze(tb)
    
    @property
    def iwp(self):
        """
        ice water path

        Returns
        -------
        np.array of IWP values

        """
        
        iwp = self.get_data('iwp')
        iwp = np.concatenate(iwp, axis = 0)
        return np.concatenate(iwp)
    

    @property
    def lat(self):
        """
        latitudes

        Returns
        -------
        np.array of lat values

        """
        
        lat = self.get_data('lat')
        lat = np.concatenate(lat, axis = 0)
        return np.concatenate(lat)
        
    @property
    def icehabit(self):
        
        return self.get_data('icehabit')        
    
    @property
    def lsampling(self):
        
        return self.get_data('lsampling')

    @property
    def polratio(self):
        
        return self.get_data('polratio')   
    
    
    def pdf(self, bins = None, plot = True):
        """
        generates pdf of Tb from IceCube simulations

        Parameters
        ----------
        bins : np.array, optional
            intervals over which PDF is to be computed. The default is None.
            When None, default bins used are np.arange(100, 300, 0.5)
        plot : boolean, optional
            if true, generates a plot of the PDF. The default is True.

        Returns
        -------
        hist[0] : np.array, The values of the histogram

        """
        
        tb = self.tb
        

        bins = np.arange(100, 300, 0.5)
        
        hist = np.histogram(tb, bins, density = True)
        
        if plot:
            
            fig, ax = plt.subplots(1,1, figsize = [8, 8])
            ax.plot(bins[:-1], hist[0])
            ax.set_yscale('log')
            ax.set_ylabel('PDF [#/K]')
            ax.set_xlabel('TB [K]')
            
        return hist[0]
    



    