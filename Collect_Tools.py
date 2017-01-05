# -*- coding: utf-8 -*-
"""
Authors: Tim Hessels
         UNESCO-IHE 2017
Contact: t.hessels@unesco-ihe.org
Repository: https://github.com/wateraccounting/wa
Module: wa
"""
# general modules
import urllib
import os
import zipfile
import shutil

# WA+ modules
from wa import WA_Paths

def Newest():

    home_folder = WA_Paths.Paths(Type = 'Home')
    file_nametext = os.path.join(home_folder, 'wa-master.zip') 
    nameDownloadtext = r"https://github.com/wateraccounting/wa/archive/master.zip"
				
    print 'Download newest Water Accounting Plus tools'				
    urllib.urlretrieve(nameDownloadtext, file_nametext) 

    print 'Extract newest Water Accounting Plus tools'	
    zip_ref = zipfile.ZipFile(file_nametext, 'r')
    zip_ref.extractall(home_folder)
    zip_ref.close()

    print 'Install newest Water Accounting Plus tools'	
    wa_folder_General = os.path.join(home_folder, 'wa','General') 
    wa_folder_Collect = os.path.join(home_folder, 'wa','Collect') 
    wa_folder_Product = os.path.join(home_folder, 'wa','Products') 
    wa_folder_Sheets = os.path.join(home_folder, 'wa','Sheets') 

    wa_master_folder_General = os.path.join(home_folder, 'wa-master','General') 
    wa_master_folder_Collect = os.path.join(home_folder, 'wa-master','Collect') 
    wa_master_folder_Product = os.path.join(home_folder, 'wa-master','Products') 
    wa_master_folder_Sheets = os.path.join(home_folder, 'wa-master','Sheets') 
    wa_master_folder_Home = os.path.join(home_folder, 'wa-master') 

    shutil.rmtree(wa_folder_General)
    shutil.rmtree(wa_folder_Collect)
    shutil.rmtree(wa_folder_Product)
    shutil.rmtree(wa_folder_Sheets)

    shutil.copytree(wa_master_folder_General, wa_folder_General)
    shutil.copytree(wa_master_folder_Collect, wa_folder_Collect)
    shutil.copytree(wa_master_folder_Product, wa_folder_Product)
    shutil.copytree(wa_master_folder_Sheets, wa_folder_Sheets)

    shutil.rmtree(wa_master_folder_Home)				
    os.remove(file_nametext)
						
    return()				