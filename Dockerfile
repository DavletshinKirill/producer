FROM python3.12.8
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8081
CMD ["python", "main.py"]