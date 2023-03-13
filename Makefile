
start:
	docker compose up --build -d --remove-orphans

stop:
	docker compose down

show-logs:
	docker compose logs

down-v:
	docker compose down -v

password.generate:
	docker exec -it password_generator sh -c 'cd /app/passwordGen && python3 password_gen.py'

process.monitor:
	docker run -it --pid host -v ./processMonitor:/app/processMonitor akkodis_process_monitor sh -c 'cd /app/processMonitor && python3 process_monitor.py'

contact.book:                                                                                                                              
	docker exec -it contact_book sh -c 'cd /app/contactBook && python3 contacts.py'
