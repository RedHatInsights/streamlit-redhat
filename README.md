[![Docker Repository on Quay](https://quay.io/repository/jdiazsua/streamlit-redhat/status "Docker Repository on Quay")](https://quay.io/repository/jdiazsua/streamlit-redhat)

# Streamlit for Red Hat

This package contains utility functions to be imported on streamlit if you
are a Red Hat employee.

You can install it like `pip install -e .` as it's not published yet.

## Local deployment

You can use `streamlit run streamlit_redhat/app.py` or any other python
scripts like `streamlit_redhat/sso/example.py`.
``
Or you can use containers:
1. Build the container with `podman build . -t streamlit-redhat:latest`
2. Run it with `podman run --rm -p 8501:8501 streamlit-redhat:latest`

Note that the `.streamlit/secrets.toml` needs to be filled in manually
with yours.

## SSO

You should follow [these docs](https://docs.streamlit.io/develop/concepts/connections/authentication)
in order to add authentication to your Streamlit app.

Inside the company, there is the policy that only stage auth is allowed for
apps running on localhost, so you may need a CNAME in order to request auth
for sso.redhat.com or auth.redhat.com.

Your `.streamlit/secrets.toml` file should look like
```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.stage]
client_id = "streamlit-redhat-sso-demo"
client_secret = "xxx"
server_metadata_url = "https://auth.stage.redhat.com/auth/realms/EmployeeIDP/.well-known/openid-configuration"

[auth.prod]
client_id = "streamlit-redhat-sso-demo"
client_secret = "xxx"
server_metadata_url = "https://sso.redhat.com/auth/realms/redhat-external/.well-known/openid-configuration"
```

where the `client_secret` is provided by the CIAM team, by opening a ticket
(see the links below).

You can try an example running `streamlit run streamlit_redhat/sso/example.py`.

Adding it to your app is as simple as calling
```python
from streamlit_redhat.sso import user_info
```

This will take care of the log in redirect and then provide a `user_info` dict
with all the user information, such as email, name, etc.

---

Relevant links:

- https://source.redhat.com/groups/public/ciams/docs/client_integration_faq
- [Instructions how to get internal SSO for your app](https://source.redhat.com/groups/public/identity-access-management/it_iam_internal_sso_int_idp_wiki/how_to_get_sso_for_your_application_or_vendor)
- [Plans on a self-serviceable SSO enablement](https://source.redhat.com/groups/public/ciams/docs/company_single_sign_on_enablement_guide_3rd_party_idpsaml_federation_for_customers)
- [Self service external SSO integration](https://source.redhat.com/groups/public/ciams/docs/draft_self_service_client_configuration_management~1)
- Sample ticket requesting an app for auth.stage.redhat.com: [RITM2075444](https://redhat.service-now.com/help?id=rh_ticket&table=sc_req_item&sys_id=28e0293d3b05ae58aa748c9c24e45ab3)

## Monitoring

You can use the `streamlit_redhat.monitoring` module to expose Prometheus metrics
to the Streamlit app.

You can try an example running `streamlit run streamlit_redhat/monitoring/example.py`.

It's a copy of the [streamlit_extras.prometheus](https://github.com/arnaudmiribel/streamlit-extras/tree/main/src/streamlit_extras/prometheus) module.
