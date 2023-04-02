def read_excel_parameters(year,category,sheet,max_column):

    n_columns=max_column-1
#2021
    names_en_17=['Department',
    'ITE_DC_Total','ITE_DC_Cases','ITE_DC_Rate',
    'ITE_RDC_Total','ITE_RDC_Cases','ITE_RDC_Rate',
    'IPE_DG_Total','IPE_DG_Cases','IPE_DG_Rate',
    'IPT_Total','IPT_DA_Cases','IPT_DA_Rate','IPT_SP_Cases','IPT_SP_Rate','IPT_O_Cases','IPT_O_Rate']

    names_en_19=['Department',
    'ITE_DC_Total','ITE_DC_Cases','ITE_DC_Rate',
    'ITE_RDC_Total','ITE_RDC_Cases','ITE_RDC_Rate',
    'IPE_DG_Total','IPE_DG_Cases','IPE_DG_Rate',
    'IPT_Total','IPT_DA_Cases','IPT_DA_Rate',
    'IPT_RDA_Cases','IPT_RDA_Rate','IPT_SP_Cases','IPT_SP_Rate','IPT_O_Cases','IPT_O_Rate']

    names_en_22=['Department','Province','District','Ubigeous',
    'ITE_DC_Total','ITE_DC_Cases','ITE_DC_Rate',
    'ITE_RDC_Total','ITE_RDC_Cases','ITE_RDC_Rate',
    'IPE_DG_Total','IPE_DG_Cases','IPE_DG_Rate',
    'IPT_Total','IPT_DA_Cases','IPT_DA_Rate',
    'IPT_RDA_Cases','IPT_RDA_Rate','IPT_SP_Cases','IPT_SP_Rate','IPT_O_Cases','IPT_O_Rate']

#2022    
    names_en_20=['Department',
    'ITE_DC_Total','ITE_DC_Cases','ITE_DC_Rate',
    'ITE_RDC_Total','ITE_RDC_Cases','ITE_RDC_Rate',
    'IPE_DG_Total','IPE_DG_Cases','IPE_DG_Rate',
    'IPT_DA_Total','IPT_DA_Cases','IPT_DA_Rate',
    'IPT_Total','IPT_RDA_Cases','IPT_RDA_Rate','IPT_SP_Cases','IPT_SP_Rate','IPT_O_Cases','IPT_O_Rate']
    
    names_en_23=['Department','Province','District','Ubigeous',
    'ITE_DC_Total','ITE_DC_Cases','ITE_DC_Rate',
    'ITE_RDC_Total','ITE_RDC_Cases','ITE_RDC_Rate',
    'IPE_DG_Total','IPE_DG_Cases','IPE_DG_Rate',
    'IPT_DA_Total','IPT_DA_Cases','IPT_DA_Rate',
    'IPT_RDA_Total','IPT_RDA_Cases','IPT_RDA_Rate','IPT_SP_Cases','IPT_SP_Rate','IPT_O_Cases','IPT_O_Rate']
    
    names_an_10=['Department','Total',
    'AT_Cases','AT_Rate',
    'AL_Cases','AL_Rate',
    'AM_Cases','AM_Rate',
    'AS_Cases','AS_Rate']
    
    names_an_13=['Department','Province','District','Ubigeous','Total',
    'AT_Cases','AT_Rate',
    'AL_Cases','AL_Rate',
    'AM_Cases','AM_Rate',
    'AS_Cases','AS_Rate']
###########
    names_an_14=['Department','Total',
    'AT_Cases','AT_Rate',
    'AL_Cases','AL_Rate',
    'AM_Cases','AM_Rate',
    'AS_Cases','AS_Rate']
 #########
 # Gestantes_en
    names_imc_clap_13=['Department',
    'IMC_PG_Total','IMC_PG_BP_Cases','IMC_PG_BP_Rate','IMC_PG_SP_Cases','IMC_PG_SP_Rate','IMC_PG_O_Cases','IMC_PG_O_Rate',
    'CLAP_Total','CLAP_DP_Cases','CLAP_DP_Rate','CLAP_SP_Cases','CLAP_SP_Rate']
    
    names_imc_clap_16=['Department','Province','District','Ubigeous',
    'IMC_PG_Total','IMC_PG_BP_Cases','IMC_PG_BP_Rate','IMC_PG_SP_Cases','IMC_PG_SP_Rate','IMC_PG_O_Cases','IMC_PG_O_Rate',
    'CLAP_Total','CLAP_DP_Cases','CLAP_DP_Rate','CLAP_SP_Cases','CLAP_SP_Rate']
    
    if year=="2022" or year=="2021": 
        
        if category=="children" :
            if (("EN" in sheet)and("DEP" in sheet)):           
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
                
            elif (("EN" in sheet)and("DIRESA" in sheet)):        
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            
            elif ("EN" in sheet) and ("DISTRITO" in sheet):    
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=7
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in sheet) and ("DEP" in sheet)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in sheet) and ("DIRESA" in sheet)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in sheet) and ("DISTRITO" in sheet)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=5
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
                
            
        elif category=="foreign_children":
            
            if (("EN" in sheet)and("DEP" in sheet)):           
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("EN" in sheet)and("DIRESA" in sheet)):          
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif ("EN" in sheet) and ("DISTRITO" in sheet):
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=5
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in sheet) and ("DEP" in sheet)) :     
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in sheet) and ("DIRESA" in sheet)) :     
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in sheet) and ("DISTRITO" in sheet)) :        
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=3
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
        elif category=="VRAEM_children":    
            
            if (("EN" in sheet) and ("DISTRITO" in sheet)):      
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=6
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in sheet) and ("DISTRITO" in sheet)) :    
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=4
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
                
        elif category=="pregnant_women":
            
            if (("IMC_PG-CLAP" in sheet)and("DEP" in sheet)):            
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("IMC_PG-CLAP" in sheet)and("DIRESA" in sheet)):          
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=34
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
                
            elif (("IMC_PG-CLAP" in sheet) and ("DISTRITO" in sheet)):     
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=None
                skipfooter=7
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in sheet) and ("DEP" in sheet)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in sheet) and ("DIRESA" in sheet)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=34
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in sheet) and ("DISTRITO" in sheet)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=6
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            

            
