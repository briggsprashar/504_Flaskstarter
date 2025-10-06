# Deploy Flask Starter Kit on Azure VM

  - SSH into VM from local terminal       
     > `ssh -i user@public-ip`

  - Update system
    > `sudo apt update`
        
  - Install Python venv
    > `sudo apt install python3.12-venv`
        
  - Create/activate venv
    > `python3 -m venv venv`   /   `source venv/bin/activate`
        
  - Clone repo / go to local folder
    > `git clone (github url)`    /     `cd (local folder)`  
        
  - Install dependencies
    > `pip install -r requirements.txt`
        
  - Run app
    > `python3 app.py`
        
  - Access on IP address
    > `(Public-IP):5003`

#  Role of VM's in U.S. Healthcare      

In today’s US healthcare environment, setting up and managing virtual machines isn’t just a technical task—it’s about giving care teams the tools to handle sensitive data and keep up with ever-changing IT policies and regulations. The process can feel daunting, especially as organizations strive for interoperability across countless systems, with federal incentives pushing for better data exchange and privacy.

Deploying apps in the cloud, like a Python Flask demo, highlights both the promise and realities of modern IT. While remote access, easy scaling, and automation are game changers, cost pressures and gaps in digital resources remain real hurdles—particularly for safety net providers and clinics serving marginalized populations. The right VM strategy can make it easier to stay compliant, keep expenses predictable, and tailor solutions for different communities.

    
Navigating these issues means not just meeting technical standards, but also recognizing where IT can foster equity and where it may unintentionally widen the divide. That’s why a thoughtful approach to VM management can go a long way—helping teams deliver care more efficiently, protect patient information, and adapt quickly to new policy or technology shifts.

</body>
</html>
