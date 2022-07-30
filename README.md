# sprout
Apis for integrating with ML model
This project contains 3 apis with 2 apis exposed for the external use and one internal api. 
apis - 
1] http://localhost:5000 [external api]
2] http://localhost:5000/posts [external api]
3] http://localhost:5000/sentences [internal api]

1] http://localhost:5000 [external api] - 
This api can be used to get all records stored in the DB/list

2] http://localhost:5000/posts [external api]
This api allows user to post json object as shown below, which will allow user to post paragraaph or sentences to find the sentiment or to find the foul language.
curl -X 'POST' \
'http://127.0.0.1:5000/posts/' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"title": "This is an engaging title",
"paragraphs": [
"This is the first paragraph. It contains two sentences.",
"This is the second parapgraph. It contains two more sentences",
"Third paraphraph here."
]
}'

the response of the above apis is as follows - 
[{"hasFoulLanguage": true, "sentence": {"fragment": "This is the first paragraph. It contains two sentences."}}, {"hasFoulLanguage": false, "sentence": {"fragment": "This is the second parapgraph. It contains two more sentences"}}, {"hasFoulLanguage": false, "sentence": {"fragment": "Third paraphraph here."}}]

