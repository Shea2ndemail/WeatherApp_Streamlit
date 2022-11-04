
FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV PORT=8501
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py"]