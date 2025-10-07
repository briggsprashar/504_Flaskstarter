# Flask Deployment Confirmations

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

<details>
  <summary>5. Connect to VM via SSH</summary>  

<br />

![Connect to VM via SSH](flask_images/2connected2VM.png)

</details>
<br />

<details>
  <summary>6. Sudo Updates</summary>  

<br />

![Sudo Updates](flask_images/3updatesuccessful.png)

</details>
<br />

<details>
  <summary>7. Update Python</summary>  

<br />

![Update Python](flask_images/4updatepython.png)

</details>

### Environment

<details>
  <summary>8. Create environment</summary>  

<br />

![Create environment](flask_images/5pythonenvironmentset.png)

</details>

### Github

<details>
  <summary>9. Clone to Github Repo & create local path </summary>  

<br />

![Clone to Github Repo](flask_images/6gitclone.png)

</details>

<br />

<details>
  <summary>10. Install requirements </summary>  

<br />

![Install requirements](flask_images/7installflask.png)

</details>

### Run Python App

<details>
  <summary>11. App Running </summary>  
<br />

![App Running](flask_images/8apprunning.png)

</details>
<br />

<details>
  <summary>12. URL Status </summary>  
<br />

![URL Status](flask_images/10urlstatuscodes.png)

</details>

<br />

<details>
  <summary>13. Webpage display </summary>  
<br />

![Webpage display](flask_images/9webpageconfirmationonport500.png)

</details>

### Confirmation

<details>
  <summary>14. Azure Shell</summary>  

<br />

![Connected to Azure shell](flask_images/10.1connectedtoazureshell.png)

</details>

<br />

<details>
  <summary>15. Azure status check prohibited</summary>  

<br />

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

#### All commands on the webpage display at 

> 40.67.149.37:5003