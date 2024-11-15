from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # The HTML file containing your form.

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    user_email = request.form['email']
    phone = request.form['phone']
    city = request.form['city']

    # Construct the email message to be sent to the user's email
    msg = MIMEMultipart()
    msg['From'] = '05panchalshweta@gmail.com'  # Your email address
    msg['To'] = user_email  # Send to the email provided by the user in the form
    msg['Subject'] = 'Form Submission Confirmation'

    # Email body with the submitted information
    body = f"""
    Hi {name},

    Thank you for submitting your details. Here are the details you provided:

    Name: {name}
    Email: {user_email}
    Phone: {phone}
    City: {city}

    Regards,
    Your Company
    """
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('05panchalshweta@gmail.com', 'cpnv fucr gfan hcnt')  # Your email and password(security -> two-step verification ->app passwords --create any app name , there u will get password )
        server.send_message(msg)
        server.quit()
        return "Form submitted successfully, and email sent!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)


