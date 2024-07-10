# CYBERPUNK 420

## Deployment

Build an image 

#FIXME

## Deploy with HELM

``` bash 
helm upgrade --install flask-service .\helm\charts\flask-service\ --namespace cyberpunk420 --create-namespace --values .\helm\services\flask-service\values.yaml
```

## Testing

``` bash 
curl -Lw http://localhost:5000
```

## Local Development 

- Install requiremnets
```bash 
pip install -r .\requiremets.txt
```

- Run tests 
``` bash 
python -m unittest test_app.py
```

## TODO 

* subscrube to the same topic in Redis
* if number of subscrubers is at least 3 of 5, third become a leader
* when the messege is recieved everyone else send message [yes, let's do that]
* return message logs as a chatlog as json.
