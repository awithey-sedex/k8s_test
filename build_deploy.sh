#! /bin/bash

if [ -z "$2" ]; then
    echo "Usage <api|service> <build / version number>"
fi

image="gcr.io/sedex-tech-test/is_prime/$1:$2"
echo Image: ${image}

pushd src/$1
docker build . -t ${image}
docker push ${image}
popd

sed "s IMAGE ${image} " is-prime-$1.yaml | kubectl apply -f -

kubectl get services
kubectl get pods
