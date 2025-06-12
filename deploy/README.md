# Deploying the Streamlit app

1. Connect to the cluster. You can use an ephemeral cluster like https://console-openshift-console.apps.crcd01ue1.zmsj.p1.openshiftapps.com/k8s/cluster/projects
2. Switch to your project. If you don't have one, create it. If using ephemeral, you can use `NAMESPACE=$(bonfire namespace reserve)` (https://github.com/RedHatInsights/bonfire) or `oc new-project test-my-app`.
3. Create the `streamlit-secrets` secret with your own values:

```
oc create secret generic --from-file .streamlit/secrets.toml streamlit-secrets
```

4. Deploy the app:

```
oc apply -f deploy/deployment.yaml
oc apply -f deploy/network.yaml
```

5. Access the app:

```
oc get route streamlit-route -o jsonpath='{.spec.host}'
```

6. Check the app is up:

```
curl -k "https://$(oc get route streamlit-route -o jsonpath='{.spec.host}')/_stcore/metrics"
```