from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



app = Flask(__name__)

@app.route('/submit-form', methods=['POST', 'OPTIONS'])
def submit_form():
   if request.method == 'OPTIONS':
       # Handle CORS preflight request
       response = app.make_default_options_response()
   elif request.method == 'POST':
       form_data = request.json  # Parses JSON data sent in the request body
       print(form_data)  # Outputs the parsed JSON object (Python dict) 
       
       def send_email(sender_email = "se30166n@pace.edu", smtp2go_username = "dhruv_joshi", smtp2go_password = "fcKUohdRqzuQJOVD", receiver_email = "info@thewiry.com", subject = "Test Email", body=""):
           # Set up the SMTP2GO server
           smtp_server = "mail.smtp2go.com"
           smtp_port = 587

           # Create the email
           message = MIMEMultipart()
           message["From"] = sender_email
           message["To"] = receiver_email
           message["Subject"] = subject
           message.attach(MIMEText(body, "plain"))

           try:
               # Connect to the SMTP2GO server and start TLS encryption
               server = smtplib.SMTP(smtp_server, smtp_port)
               server.starttls()

               # Login to the SMTP2GO server
               server.login(smtp2go_username, smtp2go_password)

               # Send the email
               server.sendmail(sender_email, receiver_email, message.as_string())
               print("Email sent successfully!")

           except Exception as e:
               print(f"Error: {e}")

           finally:
               # Quit the SMTP2GO server
               server.quit()
       
       body = str(form_data)
       send_email(body=body)
        
       response = jsonify({'message': 'Form data received successfully'})
   else:
       response = jsonify({'error': 'Method not allowed'})

   response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000', 'https://www.thewiry.com')  # Replace with your React app URL
   response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
   response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
         
   return response

if __name__ == '__main__':
    app.run(debug=True, port = 6969, host = '0.0.0.0')
