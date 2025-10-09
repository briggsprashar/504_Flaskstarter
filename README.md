# Flask Deployment Confirmations

## Videos

> Attempted to embed an iframe but could not because, for security reasons, both VSCODE and Github disallow certain raw HTML tags including `iframe`.

> The `target="_blank"` attribute, that opens the video in a new tab, is ignored from the html code for both video. It seems Github disallows it.

<details>
  <summary>Video 1: Azure VM ☁️</summary>  
<br />
<div>
  <a href="https://www.loom.com/share/7651ee0f2b9242ae8211d40198849806" target="_blank" style="float: left;">
    <img style="max-width:100px;" src="https://cdn.loom.com/sessions/thumbnails/7651ee0f2b9242ae8211d40198849806-43d290c58ee666d3-full-play.gif" />
  </a>
  <div style="clear: both;"></div>
</div>

<br />

> Though the video was truncated at 5 minutes by loom, it captures the relevant content.

</details>

<br />

<details>
  <summary>Video 2: SSH Terminal config and app deployment ☁️</summary>  
 
Instead of the video the screenshots will showcase the full lifecycle. I will try and attempt to upload the video at somepoint again.

<br />

<div>
  <a href="url" target="_blank" style="float: left;">
    <img style="max-width:100px;" src="img" />
  </a>
  <div style="clear: both;"></div>
</div>
</details>

### Create Azure VM

<details>
  <summary>1. Deploy Azure VM</summary>  
 
<br />

 ![Azure VM deploying](flask_images/0.1_flask1.png)

<br />
</details>

<br />

 <details>
  <summary>2. Azure VM created</summary>  
 
<br />

 ![Azure VM created](flask_images/0.2_AzureVMcreated.png)

<br />
</details>

### Configure Azure VM

<details>
  <summary>3. Port Accessible from source IPs</summary>  

<br />

 ![Portt 22 accessible from source IPs](flask_images/0.3_Azure_port_accessible.png)

</details>
<br />

<details>
  <summary>4. Port 5003</summary>  

<br />

 ![Port 5003 created](flask_images/1Azure5003portcreated.png)

</details>

### Local terminal

> The flask started kit was deployed many times. So many ports were used. The screenshots might have different ports. Each screenshot will indicate the port. 

<br />

<details>
  <summary>5. Connect to VM via SSH</summary>  

<br />

> Fask1 > port: 40.67.149.37

<br />

![Connect to VM via SSH](flask_images/2connected2VM.png)

</details>

<br />

<details>
  <summary>6. Sudo Updates</summary>  

<br />

> Fask1 > port: 40.67.149.37


![Sudo Updates](flask_images/3updatesuccessful.png)

</details>
<br />

<details>
  <summary>7. Update Python</summary>  

<br />

> Fask1 > port: 40.67.149.37

![Update Python](flask_images/4updatepython.png)

</details>

### Environment

<details>
  <summary>8. Create environment</summary>  

<br />

> Fask1 > port: 40.67.149.37

![Create environment](flask_images/5pythonenvironmentset.png)

</details>

### Github

<details>
  <summary>9. Clone to Github Repo & create local path </summary>  

<br />

> Fask1 > port: 40.67.149.37

![Clone to Github Repo](flask_images/6gitclone.png)

</details>

<br />

<details>
  <summary>10. Install requirements </summary>  

<br />

> Fask1 > port: 40.67.149.37

![Install requirements](flask_images/7installflask.png)

</details>

### Run Python App

<details>
  <summary>11. App Running </summary>  

<br />

> Fask1 > port: 40.67.149.37

![App Running](flask_images/8apprunning.png)

</details>
<br />

<details>
  <summary>12. URL Status </summary>  

<br />

> This may be from a another deployment iteration.

![URL Status](flask_images/10urlstatuscodes.png)

</details>

<br />

<details>
  <summary>13. Webpage display </summary>  

<br />

> Fask1 > port: 40.67.149.37

![Webpage display](flask_images/9webpageconfirmationonport500.png)

</details>

### Confirmation

<details>
  <summary>14. Azure Shell</summary>  

<br />

> Fask1 > port: 40.67.149.37

![Connected to Azure shell](flask_images/10.1connectedtoazureshell.png)

</details>

<br />

<details>
  <summary>15. Azure status check prohibited</summary>  

<br />

> Fask1 > port: 40.67.149.37

![Access denied](flask_images/11azureshell_forbiddenaction.png)

</details>

### Cleanup

<details open>
  <summary>16. Cleanup local machine </summary>  

<br />

Terminate the connection with the VM on local terminal with `CTRL + C` followed by exiting all processes with `Exit`

</details>

<details open>
  <summary>17. Stop Azure VM </summary>  

<br />

In Azure, under Virtual machines List, select **Stop** under virtual machine configuration options. Then confirm that it is stopped by visiting the **Dashboard**.

</details>

### Terminal commands 

All terminal commands were listed in the webpage displayed (bullet 13 above) with the vm running. 

> VM name: Fask1

> Port: 40.67.149.37:5003

Screenhots evidence the full lifecycle. I will try and make the video again though.