import json
data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
json.dumps(data, indent=4)
{
    "people": [
        {
            "website": "stackabuse.com", 
            "from": "Nebraska", 
            "name": "Scott"
        }
    ]
}

#sorting
json.dumps(data, sort_keys=True, indent=4)
{
    "people": [
        {
            "from": "Nebraska",
            "name": "Scott",
            "website": "stackabuse.com"
        }
    ]
}