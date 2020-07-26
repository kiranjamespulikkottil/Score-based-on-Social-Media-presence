# Score-based-on-Social-Media-presence

	Please add the 'Social Score Assignment.xlsx' file here for successfull running

Requirements:

	Python 3.6.9
	Virtual Enviornment
	pandas
	matplotlib


Steps:

	1) Install Python3
    	sudo apt-get install python3

	2) create an Virtual Environment
    	sudo apt-get install python3-venv
    	python3 -m venv environmentName

	3) Install all the requirements in the environment
    	pip3 install -r requirements.txt

    4) Add the 'Social Score Assignment.xlsx' file here.
    	inputs are read from this file.

	5) Run the retailer_search_rank.py
    	python SMP_Score.py.py



OUTPUT FORMAT:

		Youtube popularity score for the month of December for three differnet brands 

         	brand  dislike   likes       views         total  popularity percentage  Channel
	0         dove   8367.0   11017  2822563337  2.822566e+09              64.190617  youtube
	1  lorealparis  56843.0  418639   762399851  7.627616e+08              17.346677  youtube
	2     tresemme  67918.0  114237   811788965  8.118353e+08              18.462707  youtube


	Facebook popularity score for the month of December for three differnet brands 

         brand    likes  shareCount      total  popularity percentage   Channel
	0         dove  2925629     22653.0  2948282.0                  82.62  Facebook
	1  lorealparis   599303      7250.0   606553.0                  17.00  Facebook
	2     tresemme    12349      1140.0    13489.0                   0.38  Facebook


	Twitter popularity score for the month of December for three differnet brands 

         brand   likes   retweet     total  popularity percentage  Channel
	0         dove   39412   21286.0   60698.0                   6.57  Twitter
	1  lorealparis  556043  275602.0  831645.0                  89.98  Twitter
	2     tresemme   25256    6648.0   31904.0                   3.45  Twitter


	Instagram popularity score for the month of December for three differnet brands 

         brand    views   likes    total  popularity percentage    Channel
	0         dove  7264822  108702  7373524                  79.68  Instagram
	1  lorealparis   756708   50072   806780                   8.72  Instagram
	2     tresemme  1067374    6052  1073426                  11.60  Instagram


	Brand Popularity in Social Media Platforms 

         brand  popularity percentage
	0         dove              58.265154
	1  lorealparis              33.261669
	2     tresemme               8.473177


