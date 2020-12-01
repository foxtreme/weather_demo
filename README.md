# weather_demo
REST API to get weather information from a city

<h2>How to run </h2>
<ul>
<li>Install any pending dependencies with pip3 install -r requirements.txt</li>
<li>cd to <i>weather_demo</i> folder</li>
<li>type in the terminal <code>python api.py</code></li>
</ul>

<h2>Testing with Postman</h2>
<h4>Testing by city and country code</h4>
 URL: http://127.0.0.1:5000/weather?city=medellin&country=CO
 <br>
 METHOD: GET
 <br>
 EXAMPLE OF RESPONSE:
 
 <h4>Testing forecast by city and country code</h4>
 The number at the end of the base url corresponds to the day between 0 and 6
 <br>
 URL: http://127.0.0.1:5000/weather/5?city=medellin&country=CO
 <br>
 METHOD: GET
 <br>
 EXAMPLE OF RESPONSE:

 