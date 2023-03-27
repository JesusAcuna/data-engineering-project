def read_excel_parameters(year,category,dep,max_column):

    n_columns=max_column-1
#2021
    names_en_17=['Department',
    'ITE_DC:Total','ITE_DC:Cases','ITE_DC:Rate',
    'ITE_RDC:Total','ITE_RDC:Cases','ITE_RDC:Rate',
    'IPE_DG:Total','IPE_DG:Cases','IPE_DG:Rate',
    'IPT:Total','IPT_DA:Cases','IPT_DA:Rate','IPT_SP:Cases','IPT_SP:Rate','IPT_O:Cases','IPT_O:Rate']

    names_en_19=['Department',
    'ITE_DC:Total','ITE_DC:Cases','ITE_DC:Rate',
    'ITE_RDC:Total','ITE_RDC:Cases','ITE_RDC:Rate',
    'IPE_DG:Total','IPE_DG:Cases','IPE_DG:Rate',
    'IPT:Total','IPT_DA:Cases','IPT_DA:Rate',
    'IPT_RDA:Cases','IPT_RDA:Rate','IPT_SP:Cases','IPT_SP:Rate','IPT_O:Cases','IPT_O:Rate']

    names_en_22=['Department','Province','District','Ubigeous',
    'ITE_DC:Total','ITE_DC:Cases','ITE_DC:Rate',
    'ITE_RDC:Total','ITE_RDC:Cases','ITE_RDC:Rate',
    'IPE_DG:Total','IPE_DG:Cases','IPE_DG:Rate',
    'IPT:Total','IPT_DA:Cases','IPT_DA:Rate',
    'IPT_RDA:Cases','IPT_RDA:Rate','IPT_SP:Cases','IPT_SP:Rate','IPT_O:Cases','IPT_O:Rate']

#2022    
    names_en_20=['Department',
    'ITE_DC:Total','ITE_DC:Cases','ITE_DC:Rate',
    'ITE_RDC:Total','ITE_RDC:Cases','ITE_RDC:Rate',
    'IPE_DG:Total','IPE_DG:Cases','IPE_DG:Rate',
    'IPT_DA:Total','IPT_DA:Cases','IPT_DA:Rate',
    'IPT:Total','IPT_RDA:Cases','IPT_RDA:Rate','IPT_SP:Cases','IPT_SP:Rate','IPT_O:Cases','IPT_O:Rate']
    
    names_en_23=['Department','Province','District','Ubigeous',
    'ITE_DC:Total','ITE_DC:Cases','ITE_DC:Rate',
    'ITE_RDC:Total','ITE_RDC:Cases','ITE_RDC:Rate',
    'IPE_DG:Total','IPE_DG:Cases','IPE_DG:Rate',
    'IPT_DA:Total','IPT_DA:Cases','IPT_DA:Rate',
    'IPT_RDA:Total','IPT_RDA:Cases','IPT_RDA:Rate','IPT_SP:Cases','IPT_SP:Rate','IPT_O:Cases','IPT_O:Rate']
    
    names_an_10=['Department','Total',
    'AT:Cases','AT:Rate',
    'AL:Cases','AL:Rate',
    'AM:Cases','AM:Rate',
    'AS:Cases','AS:Rate']
    
    names_an_13=['Department','Province','District','Ubigeous','Total',
    'AT:Cases','AT:Rate',
    'AL:Cases','AL:Rate',
    'AM:Cases','AM:Rate',
    'AS:Cases','AS:Rate']
###########
    names_an_14=['Department','Total',
    'AT:Cases','AT:Rate',
    'AL:Cases','AL:Rate',
    'AM:Cases','AM:Rate',
    'AS:Cases','AS:Rate']
 #########
 # Gestantes_en
    names_imc_clap_13=['Department',
    'IMC_PG:Total','IMC_PG_BP:Cases','IMC_PG_BP:Rate','IMC_PG_SP:Cases','IMC_PG_SP:Rate','IMC_PG_O:Cases','IMC_PG_O:Rate',
    'CLAP:Total','CLAP_DP:Cases','CLAP_DP:Rate','CLAP_SP:Cases','CLAP_SP:Rate']
    
    names_imc_clap_16=['Department','Province','District','Ubigeous',
    'IMC_PG:Total','IMC_PG_BP:Cases','IMC_PG_BP:Rate','IMC_PG_SP:Cases','IMC_PG_SP:Rate','IMC_PG_O:Cases','IMC_PG_O:Rate',
    'CLAP:Total','CLAP_DP:Cases','CLAP_DP:Rate','CLAP_SP:Cases','CLAP_SP:Rate']
    
    if year=="2022": 
        
        if category=="children" :
            if (("EN" in dep)and("DEP" in dep)):           
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
                
            elif (("EN" in dep)and("DIRESA" in dep)):        
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            
            elif ("EN" in dep) and ("DISTRITO" in dep):    
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=7
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DEP" in dep)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DIRESA" in dep)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=5
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
                
            
        elif category=="foreign_children":
            
            if (("EN" in dep)and("DEP" in dep)):           
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("EN" in dep)and("DIRESA" in dep)):          
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif ("EN" in dep) and ("DISTRITO" in dep):
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=5
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DEP" in dep)) :     
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DIRESA" in dep)) :     
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :        
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=3
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
        elif category=="VRAEM_children":    
            
            if (("EN" in dep) and ("DISTRITO" in dep)):      
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=6
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :    
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=4
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
                
        elif category=="pregnant_women":
            
            if (("IMC_PG-CLAP" in dep)and("DEP" in dep)):            
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("IMC_PG-CLAP" in dep)and("DIRESA" in dep)):          
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=34
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
                
            elif (("IMC_PG-CLAP" in dep) and ("DISTRITO" in dep)):     
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=None
                skipfooter=7
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DEP" in dep)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DIRESA" in dep)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=34
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=6
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            

    if year=="2021": 
        
        if category=="children" :
            if (("EN" in dep)and("DEP" in dep)):           
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
                
            elif (("EN" in dep)and("DIRESA" in dep)):        
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            
            elif ("EN" in dep) and ("DISTRITO" in dep):    
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=7
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DEP" in dep)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DIRESA" in dep)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=5
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
                
            
        elif category=="foreign_children":
            
            if (("EN" in dep)and("DEP" in dep)):           
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("EN" in dep)and("DIRESA" in dep)):          
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif ("EN" in dep) and ("DISTRITO" in dep):
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=5
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DEP" in dep)) :     
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DIRESA" in dep)) :     
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :        
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=3
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
        elif category=="VRAEM_children":    
            
            if (("EN" in dep) and ("DISTRITO" in dep)):      
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=6
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :    
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=4
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
                
        elif category=="pregnant_women":
            
            if (("IMC_PG-CLAP" in dep)and("DEP" in dep)):            
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("IMC_PG-CLAP" in dep)and("DIRESA" in dep)):          
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=34
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
                
            elif (("IMC_PG-CLAP" in dep) and ("DISTRITO" in dep)):     
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=None
                skipfooter=7
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DEP" in dep)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DIRESA" in dep)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=34
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=6
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
    if year=="2020": 
        
        if category=="children" :
            if (("EN" in dep)and("DEP" in dep)):           
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
                
            elif (("EN" in dep)and("DIRESA" in dep)):        
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            
            elif ("EN" in dep) and ("DISTRITO" in dep):    
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=7
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DEP" in dep)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DIRESA" in dep)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :       
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=5
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
                
            
        elif category=="foreign_children":
            
            if (("EN" in dep)and("DEP" in dep)):           
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("EN" in dep)and("DIRESA" in dep)):          
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif ("EN" in dep) and ("DISTRITO" in dep):
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=5
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DEP" in dep)) :     
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DIRESA" in dep)) :     
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=29
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :        
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=3
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
        elif category=="VRAEM_children":    
            
            if (("EN" in dep) and ("DISTRITO" in dep)):      
                skiprows=7
                names=eval(f"names_en_{n_columns}")
                nrows=None
                skipfooter=6
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :    
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=4
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
                
        elif category=="pregnant_women":
            
            if (("IMC_PG-CLAP" in dep)and("DEP" in dep)):            
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("IMC_PG-CLAP" in dep)and("DIRESA" in dep)):          
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=34
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
                
            elif (("IMC_PG-CLAP" in dep) and ("DISTRITO" in dep)):     
                skiprows=7
                names=eval(f"names_imc_clap_{n_columns}")
                nrows=None
                skipfooter=7
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            
            elif (("Anemia" in dep) and ("DEP" in dep)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=25
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DIRESA" in dep)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=34
                skipfooter=0
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols
            elif (("Anemia" in dep) and ("DISTRITO" in dep)) :
                skiprows=6
                names=eval(f"names_an_{n_columns}")
                nrows=None
                skipfooter=6
                usecols=range(1,len(names)+1)
                return skiprows,names,nrows,skipfooter,usecols