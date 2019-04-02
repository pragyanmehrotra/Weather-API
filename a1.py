'''
Name: Pragyan Mehrotra
Roll No: 2018168
section: A
group: 8
'''

import urllib.request
import datetime

# function to get weather response
def weather_response(location, API_key):
	try:
		query = "http://api.openweathermap.org/data/2.5/forecast?q=" +location+"&APPID="+API_key
		json = urllib.request.urlopen(query).read()
		return json
	except urllib.error.HTTPError as e:
		if (e.code==404):
			return "Invalid query, location not found"
		elif(e.code==401):
			return "Invalid query, Invalid API authorization error"
		else:
			return e
		

#function to get the queried date and time
def get_datetime(n,t):
	use_date = str(datetime.date.today() + datetime.timedelta(days=n))
	if len(t.split(":")) == 2:
		t += ':00'
		if len(t.split(":")[0])==1:
			t = '0' + t
	cur_date_time = use_date + ' ' + t
	return cur_date_time


# function to check for valid response 
def has_error(location,json):
	json = str(json)
	#get the index of the name
	name_index = json.find('"name":')
	#get the index of the comma
	com_index = json.find(',',name_index)
	#get the index of the colon 
	col_index = json.find(':',name_index)
	
	city_name = json[col_index+2:com_index-1]
	if location.lower() != city_name.lower():
		return True
	else:
		return False


# function to the temperature
def get_temperature (json, n=2,t="15:00"):
	#get the desired date
	cur_date_time = get_datetime(n,t)
	json = str(json)

	#get the index of desired date
	date_index = json.find(cur_date_time)
	if date_index==-1:
		return None

	#get the index of the temperature associated with the date
	temp_index = json.rfind('"temp":',0,date_index)

	#get the index of ':' since we know that the temperature starts from the colon
	col_index = json.find(':',temp_index)

	#get the index of the comma since we know that the temperature ends with a comma
	com_index = json.find(',',col_index)

	temperature = json[col_index+1:com_index]

	return float(temperature)
	
#function to get the humidity
def get_humidity(json, n=0,t="00:00:00"):
	#get the desired date
	cur_date_time = get_datetime(n,t)
	json = str(json)

	#get the index of desired date
	date_index = json.find(cur_date_time)
	if date_index==-1:
		return None

	#get the index of the humidity associated with the date
	temp_index = json.rfind('"humidity":',0,date_index)

	#get the index of ':' since we know that the humidity starts from the colon
	col_index = json.find(':',temp_index)

	#get the index of the comma since we know that the humidity ends with a comma
	com_index = json.find(',',col_index)

	humidity = json[col_index+1:com_index]

	return float(humidity)
	
#function to get the pressure
def get_pressure(json, n=0,t="00:00"):
	#get the desired date
	cur_date_time = get_datetime(n,t)
	json = str(json)

	#get the index of desired date
	date_index = json.find(cur_date_time)
	if date_index==-1:
		return None

	#get the index of the pressure associated with the date
	temp_index = json.rfind('"pressure":',0,date_index)

	#get the index of ':' since we know that the pressure starts from the colon
	col_index = json.find(':',temp_index)

	#get the index of the comma since we know that the pressure ends with a comma
	com_index = json.find(',',col_index)

	pressure = json[col_index+1:com_index]

	return float(pressure) 

#function to get the wind
def get_wind(json, n=0,t="00:00"):
	#get the desired date
	cur_date_time = get_datetime(n,t)
	json = str(json)

	#get the index of desired date
	date_index = json.find(cur_date_time)
	if date_index==-1:
		return None
	#get the index of the wind associated with the date
	temp_index = json.rfind('"wind":',0,date_index)

	#get the index of ':' since we know that the wind starts from the colon
	col_index = json.find(':',temp_index)
	#get the colon index again since we know that the wind speed begins from :
	col_index = json.find(':',col_index+1)

	#get the index of , since we know that the wind speed ends with a ,
	com_index = json.find(',',col_index)

	wind = json[col_index+1:com_index]

	return float(wind)

#function to get the sea_level
def get_sealevel(json, n=0,t="00:00"):
	#get the desired date
	cur_date_time = get_datetime(n,t)
	json = str(json)

	#get the index of desired date
	date_index = json.find(cur_date_time)
	if date_index==-1:
		return None

	#get the index of the sea level associated with the date
	temp_index = json.rfind('"sea_level":',0,date_index)

	#get the index of ':' since we know that the sea level starts from the colon
	col_index = json.find(':',temp_index)

	#get the index of the comma since we know that the sea level ends with a comma
	com_index = json.find(',',col_index)

	sea_level = json[col_index+1:com_index]

	return float(sea_level)

location = "Delhi"
API_key = "2ab136be1543b5789451a5994364c0d3"
n = 2 #day no
t = "03:00" # time
json = weather_response(location,API_key)

