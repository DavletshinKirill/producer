FROM python3.12.8
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]