FROM registry.access.redhat.com/ubi9/python-311

WORKDIR /app

COPY --chown=1001:0 . .

USER root

RUN pip3 install -r requirements.txt
RUN pip3 install .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

USER default

ENTRYPOINT ["streamlit", "run", "streamlit_redhat/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
