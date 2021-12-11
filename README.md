# DetailsAPI
API for Details project 

Preparing the enviroment:
* install pyhton 3 on your computer and add it to the path enviroment
* open the project using vs code 
* open the terminal on vs code and right the following to create python enviroment with the required dependences:
  1.  python -m venv env <!--this will create a python enviroment named env-->
  2.  pip install --upgrade pip <!--this will update the pip-->
  3.  pip install -r requirements.txt <!--this command to activate the env - you must activate it before running the code-->
  4.  .\env\Scripts\activate <!--this will download all the dependences-->
* now you can run the main.py without problems
* Now go to http://127.0.0.1:9000/docs.

* You will see the automatic interactive API documentation (provided by Swagger UI):
![image](https://user-images.githubusercontent.com/73385791/145678676-841fe857-4e1b-48e6-bbd6-0c27dc804856.png)
* on this interactive API documentation you can try the API without using external tools like postman
* all the avilable requests types and paths will be shown there and will be ready for testing.

* Example of using the getRFM post request which require a file of the request body for analyzing and returing the analyzed data.
![image](https://user-images.githubusercontent.com/73385791/145678810-6e6094c8-67b8-4ced-b337-e4bce02c3ec5.png)
* note that on the Response section there is an example of the output

* Example of the output of analyzing data
![image](https://user-images.githubusercontent.com/73385791/145678960-06449808-2826-44a9-93f1-5109d5424d3b.png)
* also you can click download to download the JSON file.

