# bvik-proekt
 
 # Setting up env
 pip install libsecp256k1

 pip install hypercorn["trio"]

 pip install fastapi

 pip install aleph_client


 # starting the application
 Slednava komanda pisi ja vo backend fajlot

 hypercorn app.api:app --worker-class trio --reload
