# Bertud
##Installation 
* Clone the repository: `git clone https://github.com/ivancheesecake/Bertud.git`
* Create a working branch: `git checkout -b work_branch_miyah`

###Install dependencies
* Add python and python scripts to PATH 
* `cd Bertud/dependencies`
* `install.bat`
* Extract LAStools in C:\
* Acquire LAStools license
* Open Pyro4 configuration file then add pickle to the entry "`self.SERIALIZERS_ACCEPTED`"<br />
	Sample location: "C:\Python27\ArcGIS10.2\Lib\site-packages\Pyro4-4.41-py2.7.egg\Pyro4\configuration.py"<br />
	`self.SERIALIZERS_ACCEPTED = "serpent,marshal,json,pickle"`
* Requires Internet connection

###Master configuration
Edit `config.json`.

Options:

* `ip` - IP address of master
* `pythonPath` - Path of Python libraries and executables
* `defaultInputFolder` - Where the laz files to process are located
* `defaultOutputFolder` - Where the output are placed

Sample `config.json`

`{
   "ip":"10.0.3.115",
   "pythonPath":"C:\\Python27\\ArcGIS10.3\\",
   "defaultInputFolder":"C:/bertud_inputs/",
   "defaultOutputFolder":"C:/bertud_outputs"  
 } 
`
###Slave configuration
Edit `slave_config.json`.

Options:
* `dispatcherIP` - The IP address of the server
* `workerID` - The statically assigned IP of the slave
* `tempFolder` - Path of temporary files

Sample `slave_config.json`

`{"dispatcherIP":"10.0.3.115","workerID":"1", "tempFolder":"C:/bertud_temp"}`

###Starting master/slave
Open command line(s)
* To run the master: `runserver.bat`
* To run slaves: `start bertud-slave-v2`
 
###Dashboard
* On the master, access http://127.0.0.1:5000 in your browser (pref. Chrome)

