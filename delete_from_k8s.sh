for k in services deployments; do
    for s in frontend backend; do
        kubectl delete $k is-prime-$s 
    done
done
