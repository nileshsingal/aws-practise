## EMR CREATION FOR sqoop

**1. Go to Services**.

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/1.png)

**2. Hit Create Cluster**.

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/2.png)

**3. GO to advanced option**.

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/3.png)

**4. Software configuration as shown below**.

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/4.png)

**5. Steps(optional) Leave it default.**

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/5.png)

**6. Hadoop configuration Leave it Default.**

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/6.png)

**7. Networking Leave it Default.**

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/7.png)

**8. * Cluster node and instances.**
1. For master Select instance type **m4.large** and instance count **1**
2. For core Select instance type **m4.large** and instance count **0**
3. And delete remaining types

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/8.png)

**9. Cluster Scaling : Uncheck cluster scaling **

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/9.png)

**10.  Give cluster Name **

**Uncheck logging and termination protection**
      
**Tags are optional**

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/10.png)

**11. Security option: Select your Availabe Ec-2 key pair And Hit CREATE CLUSTER.**


![](https://github.com/nileshsingal/BigData/blob/master/images/emr/12.png)

**12. It will take approximately 10-12 min till that time you can have a cup of tea**

![](https://github.com/nileshsingal/BigData/blob/master/images/emr/12.png)

**13. When your cluster state changes to Waiting From Starting that means you're cluster is created successfully and you can ssh now**








