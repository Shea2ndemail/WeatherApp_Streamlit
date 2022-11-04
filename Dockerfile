
FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV PORT=8080
EXPOSE 8080
ENTRYPOINT ["streamlit", "run", "app.py"]