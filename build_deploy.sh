#! /bin/bash

if [ -z "$2" ]; then
    echo "Usage <frontend|service> <build / version number>"
    exit 1
fi

IMAGEPREFIX="gcr.io/sedex-tech-test/is_prime/is_prime_"

NEWIMAGE="$IMAGEPREFIX$1:$2"

echo Image: ${NEWIMAGE}

pushd src/$1
docker build . -t ${NEWIMAGE}
docker push ${NEWIMAGE}
popd

sed -i .bak "s|image: .*|image: ${NEWIMAGE}|" is-prime-$1.yaml
kubectl apply -f is-prime-$1.yaml

kubectl get services
kubectl get pods
