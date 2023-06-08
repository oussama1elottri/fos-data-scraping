FROM python:latest
COPY . .
CMD python wS.py
# COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt





# WORKDIR /app

# COPY etl.py /app/etl.py

# RUN pip install requests pandas folium

# COPY cronjob /etc/cron.d/etl-cron
# RUN chmod 0644/etc/cron.d/etl-cron
# RUN crontab
# CMD cron -f