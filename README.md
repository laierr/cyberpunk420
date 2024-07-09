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