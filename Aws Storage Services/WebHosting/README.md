## Hosting a static website on Amazon S3

You can use Amazon S3 to host a static website. On a static website, individual webpages include static content. 
They might also contain client-side scripts.

**Login to your aws account**
**Goto Services**
**Storage services**
**S3**


![](images/a.PNG)



* These Are buckets Available


![](images/b.PNG)


* We will create new folder named **Webhosting**


![](images/c.PNG)


* Folder is created


![](images/d.PNG)


* add our **.html** file in that folder


![](images/e.PNG)


* Hit Upload


![](images/f.PNG)


* File has been uploaded succesfully


![](images/g.PNG)


* Now Goto actions and choose **Make Public*
but in the Screen below you can see that make public is disable


![](images/h.PNG)


* next step is to make public 
goto overview


![](images/i.PNG)


* You will get this page
**you can see that all public access are blocked**


![](images/j.PNG)


* hit edit and uncheck **block all public access** and **save**


![](images/k.PNG)


*  I Got a Error, my account is restricted account that why i got exception


![](images/l.PNG)


* So we try alternate way to make public access

* goto properties
you will see this interface


![](images/m.PNG)


* Check Static Website hosting


![](images/n.PNG)


* type fileName.html
in our case the file name is welcome.html
and hit save


![](images/o.PNG)


* see that bucket hosting is checked


![](images/p.PNG)


* now go to file then action then make public


![](images/q.PNG)


* Hit make public


![](images/r.PNG)


* uncheck and check the file again
you will get a popup window


![](images/s.PNG)


* you can see object url thats the url to our website


![](images/t.PNG)


* Hit the url and we are done
This is our basic webpage we just hosted now



![](images/u.PNG)








