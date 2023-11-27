# Gunicorn configuration file

# Worker Processes
workers = 4

# The number of threads for handling requests
threads = 2

# Binding Address
bind = '0.0.0.0:8000'

# Logging
accesslog = '-'
errorlog = '-'

# Other configurations can be added here...