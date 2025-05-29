import streamlit as st
from prometheus_client import Counter
from streamlit_redhat.monitoring import streamlit_registry


if __name__ == "__main__":

    @st.cache_resource
    def get_metric():
        registry = streamlit_registry()
        return Counter(
            name="my_counter",
            documentation="A cool counter",
            labelnames=("app_name",),
            registry=registry,  # important!!
        )

    SLIDER_COUNT = get_metric()

    app_name = st.text_input("App name", "prometheus_app")
    latest = st.slider("Latest value", 0, 20, 3)
    if st.button("Submit"):
        SLIDER_COUNT.labels(app_name).inc(latest)

    st.write(
        """
        View a fuller example that uses the (safer) import metrics method at:
        https://github.com/arnaudmiribel/streamlit-extras/tree/main/src/streamlit_extras/prometheus/example
        """
    )

    st.write(
        """
        ### Example output at `{host:port}/_stcore/metrics`
        ```
        # TYPE my_counter counter
        # HELP my_counter A cool counter
        my_counter_total{app_name="prometheus_app"} 14.0
        my_counter_created{app_name="prometheus_app"} 1.7042185907557938e+09
        ```
        """
    )
