#Virtual Environment allows you to maintain dependecies of your projects independently with each other .
# it prevent dependency conflicts between the projects and keep the origianl global python env safe
# It acts as a "sandbox", ensuring that dependencies installed for one project do not interfere with the global Python installation

# 3 steps : Create, ACtivate, Install, Verify
            using git move into the directory as "cd <folder name>"
        #Create : python -m venv projectA_env  |   python -m venv projectB_env   ==> it will create a folder with 'projectA_env' or 'projectB_env'
    
    #Activate :   projectA_env\Scripts\activate (Windows)     |      source projectA_env\bin\activate (mac)
       #now the project 'projectA_env' actiavted --> open  project 'projectA_env'
    
    #install : pip install numpy , pip install bs4
        # now these modules or packages will only be installed for 'projectA_env' other projects can't be able to access this installed package / module 
