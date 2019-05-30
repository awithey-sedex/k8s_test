#! /bin/bash

if [ -z "$2" ]; then
    echo "Usage <api|service> <build / version number>"
    exit 1
fi

IMAGEPREFIX="gcr.io/sedex-tech-test/is_prime"

NEWIMAGE="$IMAGEPREFIX/$1:$2"

echo Image: ${NEWIMAGE}

pushd src/$1
docker build . -t ${NEWIMAGE}
docker push ${NEWIMAGE}
popd

sed "s|image: .*|image: ${NEWIMAGE}|" is-prime-$1.yaml | kubectl apply -f -

kubectl get services
kubectl get pods
