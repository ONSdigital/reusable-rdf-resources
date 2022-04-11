# How to add a Resource class to gather urls from a different page.

In instances where more urls are to be appended to json files from different
pages, all you need to do is add to the 'RESOURCES' list in 'populatejsonfiles.py'
and type up the appropriate SPARQL query in the 'SPARQL_QUERIES' class 
within the same file.

To add to the 'RESOURCES' list, all you need to enter is the url of the web 
page you're gathering the urls from, as well as the json file you want to 
store these urls to, as well as the name to the SPARQL query (from the 
constants in the 'SPARQL_QUERIES' class) you are going to set up and use to
fetch those url from the web page. Finally you just need to add the SPARQL 
command to the constant that you would have set up to be called from the 
'SPARQL_QUERIES' class.