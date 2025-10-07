# Deploy Flask Starter Kit on Azure VM (Apple OS 12+)

  - SSH into VM from local terminal       
     > `ssh user@public-ip`

     with private key
     > `ssh -i /path/to/private-key user@public-ip`


  - Update system
    > `sudo apt update`
        
  - Install Python venv
    > `sudo apt install python3.12-venv`
        
  - Create/activate venv
    > `python3 -m venv venv`   /   `source venv/bin/activate`
        
  - Clone repo / go to local folder
    > `git clone (github url)`    /     `cd (local folder)`  
        
  - Install dependencies
    > `pip3 install -r requirements.txt`
        
  - Run app
    > `python3 app.py`
        
  - Access on IP address
    > `(Public-IP):5003`