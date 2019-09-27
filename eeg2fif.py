#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 04:33:21 2019

@author: huxiaoqing
"""
import mne
import os
from mne_bids import write_raw_bids
raw_fname=('/home/huxiaoqing/hcp_EEG/RawData/eeg/') 
out_path1=('/home/xiatao/TMRBiasEEG/BIDS_raw/')
subjectlist=os.listdir(raw_fname)
for subject in subjectlist:
    montage=mne.channels.read_montage('standard_1020')
    raw_name_path=os.path.join(raw_fname,subject)
    all_block=[]
    for i in range(1,10):
        block_path=(subject +'_Moral_asso_'+str(i)+'.vhdr')
        eeg_path=os.path.join(raw_name_path,block_path)
        raw=mne.io.read_raw_brainvision(eeg_path,montage,preload=True)
        all_block.append(raw)
        
raw_fname=('/home/eeg/sub6_Moral_asso_1.vhdr') 
montage=mne.channels.read_montage('standard_1020')
raw=mne.io.read_raw_brainvision(raw_fname,montage,preload=True)