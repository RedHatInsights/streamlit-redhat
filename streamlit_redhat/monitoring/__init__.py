"""
This module is a copy of the streamlit_extras.prometheus module.

https://github.com/arnaudmiribel/streamlit-extras/blob/main/src/streamlit_extras/prometheus/__init__.py#L87
"""

from typing import List, NamedTuple

from prometheus_client import CollectorRegistry
from prometheus_client.openmetrics.exposition import generate_latest
from streamlit.runtime.stats import CacheStatsProvider


class CustomStat(NamedTuple):
    metric_str: str = ""

    def to_metric_str(self) -> str:
        return self.metric_str

    def marshall_metric_proto(self, metric) -> None:
        """Custom OpenMetrics collected via protobuf is not currently supported."""
        # Included to be compatible with the RequestHandler's _stats_to_proto() method:
        # https://github.com/streamlit/streamlit/blob/1.29.0/lib/streamlit/web/server/stats_request_handler.py#L73
        # Fill in dummy values so protobuf format isn't broken
        label = metric.labels.add()
        label.name = "cache_type"
        label.value = "custom_metrics"

        label = metric.labels.add()
        label.name = "cache"
        label.value = "not_implemented"

        metric_point = metric.metric_points.add()
        metric_point.gauge_value.int_value = 0


class PrometheusMetricsProvider(CacheStatsProvider):
    def __init__(self, registry: CollectorRegistry):
        self.registry = registry

    def get_stats(self) -> List[CustomStat]:
        """
        Use generate_latest() method provided by prometheus to produce the
        appropriately formatted OpenMetrics text encoding for all the stored metrics.

        Then do a bit of string manipulation to package it in the format expected
        by Streamlit's stats handler, so the final output looks the way we expect.
        """
        DUPLICATE_SUFFIX = "\n# EOF\n"
        output_str = generate_latest(self.registry).decode(encoding="utf-8")
        if not output_str.endswith(DUPLICATE_SUFFIX):
            raise ValueError("Unexpected output from OpenMetrics text encoding")
        output = CustomStat(metric_str=output_str[: -len(DUPLICATE_SUFFIX)])
        return [output]


def streamlit_registry() -> CollectorRegistry:
    """
    Expose Prometheus metrics (https://prometheus.io) from your Streamlit app.

    Create and use Prometheus metrics in your app with `registry=streamlit_registry()`.
    The metrics will be exposed at Streamlit's existing `/_stcore/metrics` route.

    **Note:** This extra works best with Streamlit >= 1.31. There are known bugs with
    some earlier Streamlit versions, especially 1.30.0.

    See more example metrics in the Prometheus Python docs:
    https://prometheus.github.io/client_python/

    To produce accurate metrics, you are responsible to ensure that unique metric
    objects are shared across app runs and sessions. We recommend either 1) initialize
    metrics in a separate file and import them in the main app script, or 2) initialize
    metrics in a cached function (and ensure the cache is not cleared during execution).

    For an app running locally you can view the output with
    `curl localhost:8501/_stcore/metrics` or equivalent.
    """
    from streamlit import runtime

    stats = runtime.get_instance().stats_mgr

    # Did we already register it elsewhere? If so, return that copy
    for prv in stats._cache_stats_providers:
        if isinstance(prv, PrometheusMetricsProvider):
            return prv.registry

    # This is the function was called, so create the registry
    # and hook it into Streamlit stats
    registry = CollectorRegistry(auto_describe=True)
    prv = PrometheusMetricsProvider(registry=registry)
    stats.register_provider(prv)
    return registry
